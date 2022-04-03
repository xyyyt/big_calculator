#include <system_error>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <string.h>
#include <cstdio>
#include <filesystem>

#include "server_unix_socket.hpp"

namespace calculator::utils
{
    server_unix_socket::server_unix_socket(const char *socketfile) noexcept :
        _socketfile(socketfile)
    { }

    server_unix_socket::~server_unix_socket()
    {
        close(_fd);
        this->remove_socketfile();
    }

    void server_unix_socket::socket()
    {
        _fd = ::socket(AF_UNIX, SOCK_STREAM, 0);

        if (_fd == -1)
        {
            throw std::system_error(errno, std::generic_category());
        }
    }

    void server_unix_socket::bind() const
    {
        sockaddr_un addr;

        memset(&addr, 0, sizeof(addr));
        addr.sun_family = AF_UNIX;

        strncpy(addr.sun_path, _socketfile, sizeof(addr.sun_path) - 1);

        this->remove_socketfile();

        if (::bind(_fd,
                 reinterpret_cast<sockaddr *>(&addr),
                 sizeof(sockaddr_un))
            == -1)
        {
            throw std::system_error(errno, std::generic_category());
        }
    }

    void server_unix_socket::listen(int backlog) const
    {
        if (::listen(_fd, backlog) == -1)
        {
            throw std::system_error(errno, std::generic_category());
        }
    }

    int server_unix_socket::accept() const
    {
        int connection_sock = ::accept(_fd, nullptr, nullptr);

        if (connection_sock == -1)
        {
            throw std::system_error(errno, std::generic_category());
        }

        return connection_sock;
    }

    void server_unix_socket::shutdown() const
    {
        if (::shutdown(_fd, SHUT_RDWR) == -1)
        {
            throw std::system_error(errno, std::generic_category());
        }
    }

    void server_unix_socket::remove_socketfile() const
    {
        if (std::filesystem::exists(_socketfile))
        {
            unlink(_socketfile);
        }
    }
}
