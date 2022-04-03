#include <sys/types.h>
#include <sys/socket.h>
#include <poll.h>
#include <unistd.h>
#include <string.h>
#include <memory>
#include <utility>
#include <system_error>

#include "crti_data.hpp"
#include "crti_child_process_handler.hpp"
#include "crti_broadcaster.hpp"

namespace calculator::network
{
    namespace
    {
        using serialized_data_t = std::pair<size_t, std::unique_ptr<char[]>>;

        serialized_data_t serialize(const crti_data& data)
        {
            size_t size = sizeof(data.line.length())
                + data.line.length()
                + sizeof(data.result.length())
                + data.result.length()
                + sizeof(data.exec_time);
            std::unique_ptr<char[]> serialized_data =
                std::make_unique<char[]>(size);
            auto ptr = serialized_data.get();

            // "line" field
            *reinterpret_cast<size_t *>(ptr) = data.line.length();
            ptr += sizeof(data.line.length());

            for (auto c : data.line)
            {
                *ptr++ = c;
            }


            // "result" field
            *reinterpret_cast<size_t *>(ptr) = data.result.length();
            ptr += sizeof(data.result.length());

            for (auto c : data.result)
            {
                *ptr++ = c;
            }


            // "exec_time" field
            *reinterpret_cast<double *>(ptr) = data.exec_time;
            ptr += sizeof(data.exec_time);

            return {size, std::move(serialized_data)};
        }
    }

    crti_broadcaster::crti_broadcaster() :
        _entry_conn_monitoring_thread(
            &crti_broadcaster::entry_conn_monitoring_thread, this),
        _server_sock("crti.sock")
    { }

    crti_broadcaster::~crti_broadcaster()
    {
        _server_sock.shutdown();
        _entry_conn_monitoring_thread.join();
    }

    void crti_broadcaster::forward_to_all(const crti_data& data)
    {
        if (_pipe_write_end_fds.empty())
        {
            return;
        }

        pollfd pfds[_pipe_write_end_fds.size()];

        memset(pfds, 0, sizeof(pfds));

        uint32_t n = 0;

        for (auto pipe_write_end_fd : _pipe_write_end_fds)
        {
            pfds[n].fd = pipe_write_end_fd;
            pfds[n].events = POLLOUT;
            ++n;
        }

        int ret = poll(pfds, sizeof(pfds) / sizeof(*pfds), 0);

        if (ret == -1)
        {
            if (errno == EINTR)
            {
                return;
            }

            throw std::system_error(errno, std::generic_category());
        }
        else if (!ret)
        {
            return;
        }

        auto [serialized_data_size, serialized_data] = serialize(data);

        for (const auto& pfd : pfds)
        {
            if (pfd.revents & (POLLERR | POLLHUP | POLLNVAL))
            {
                _pipe_write_end_fds.erase(pfd.fd);
                close(pfd.fd);
                continue;
            }

            if (pfd.revents & POLLOUT
                && write(pfd.fd, serialized_data.get(), serialized_data_size)
                == -1)
            {
                throw std::system_error(errno, std::generic_category());
            }
        }
    }

    void crti_broadcaster::entry_conn_monitoring_thread()
    {
        try
        {
            _server_sock.socket();
            _server_sock.bind();
            _server_sock.listen(10);

            while (1)
            {
                int connection_sock;

                try
                {
                    connection_sock = _server_sock.accept();
                }
                catch (const std::system_error& e)
                {
                    int error = e.code().value();

                    if (error == EINTR || error == EINVAL)
                    {
                        break;
                    }

                    throw e;
                }

                int pipefd[2];

                if (pipe(pipefd) == -1)
                {
                    throw std::system_error(errno, std::generic_category());
                }

                pid_t pid = fork();

                if (pid == -1)
                {
                    throw std::system_error(errno, std::generic_category());
                }
                else if (!pid)
                {
                    close(pipefd[1]);

                    int status = 0;
                    crti_child_process_handler handler(
                        connection_sock, pipefd[0]);

                    try
                    {
                        handler.handle();
                    }
                    catch (const std::exception&)
                    {
                        // std::cerr << "crti child process: "
                        //           << e.what() << '\n';
                        status = -1;
                    }
                    catch (...)
                    {
                        // std::cerr << "crti child process: "
                        //     "unknown caught exception\n";
                        status = -1;
                    }

                    handler.~crti_child_process_handler();
                    close(pipefd[0]);
                    exit(status);
                }

                close(pipefd[0]);
                _pipe_write_end_fds.emplace(pipefd[1]);
            }
        }
        catch (const std::exception&)
        {
            // std::cerr << "crti entry connection monitoring thread: "
            //           << e.what() << '\n';
        }
        catch (...)
        {
            // std::cerr << "entry connection monitoring thread: "
            //     "unknown caught exception\n";
        }
    }
}
