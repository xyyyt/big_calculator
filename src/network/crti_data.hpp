#ifndef CRTI_DATA_HPP_
# define CRTI_DATA_HPP_

# include <string>

namespace calculator::network
{
    struct crti_data
    {
        std::string line;
        std::string result;
        double exec_time;
    };
}

#endif
