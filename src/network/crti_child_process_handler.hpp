#ifndef CRTI_CHILD_PROCESS_HANDLER_HPP_
# define CRTI_CHILD_PROCESS_HANDLER_HPP_

namespace calculator::network
{
    class crti_child_process_handler
    {
    public :
        crti_child_process_handler(int connection_sock, int pipe_read_end_fd)
            noexcept;
        void handle();

    private :
        int _connection_sock;
        int _pipe_read_end_fd;
    };
}

#endif
