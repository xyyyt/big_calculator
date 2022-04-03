#ifndef CL_ARGUMENTS_HPP_
# define CL_ARGUMENTS_HPP_

# include <string>

namespace calculator
{
    struct cl_arguments
    {
        bool help;
        bool local_crti;
        // bool remote_crti;
        // std::string remote_crti_ip;
        // uint16_t remote_crti_port;
    };
}

#endif
