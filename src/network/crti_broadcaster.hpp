#ifndef CRTI_BROADCASTER_HPP_
# define CRTI_BROADCASTER_HPP_

# include <string_view>
# include <thread>
# include <unordered_set>

# include "server_unix_socket.hpp"

namespace calculator::network
{
    struct crti_data;

    // crti : calculator real time information
    class crti_broadcaster
    {
    public :
        crti_broadcaster();
        ~crti_broadcaster();
        void forward_to_all(const crti_data& data);

    private :
        std::thread _entry_conn_monitoring_thread;
        utils::server_unix_socket _server_sock;
        std::unordered_set<int> _pipe_write_end_fds;

        void entry_conn_monitoring_thread();
    };
}

#endif
