#ifndef SERVER_UNIX_SOCKET_HPP_
# define SERVER_UNIX_SOCKET_HPP_

namespace calculator::utils
{
    class server_unix_socket
    {
    public :
        server_unix_socket(const char *socketfile) noexcept;
        ~server_unix_socket();
        void socket();
        void bind() const;
        void listen(int backlog) const;
        int accept() const;
        void shutdown() const;

    private :
        const char *_socketfile;
        int _fd;

        void remove_socketfile() const;
    };
}

#endif
