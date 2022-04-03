#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <system_error>

#include "crti_child_process_handler.hpp"

namespace calculator::network
{
    crti_child_process_handler::crti_child_process_handler(
        int connection_sock, int pipe_read_end_fd) noexcept :
        _connection_sock(connection_sock), _pipe_read_end_fd(pipe_read_end_fd)
    { }

    void crti_child_process_handler::handle()
    {
        char buffer[1024];

        while (1)
        {
            ssize_t size = read(_pipe_read_end_fd, buffer, sizeof(buffer));

            if (size == -1)
            {
                throw std::system_error(errno, std::generic_category());
            }
            else if (!size)
            {
                break;
            }

            buffer[size] = '\0';

            if (send(_connection_sock, buffer, size, MSG_DONTWAIT) == -1)
            {
                if (errno == EAGAIN || errno == EWOULDBLOCK)
                {
                    continue;
                }
                else if (errno == EPIPE)
                {
                    break;
                }

                throw std::system_error(errno, std::generic_category());
            }
        }
    }
}
