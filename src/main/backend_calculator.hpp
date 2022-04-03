#ifndef BACKEND_CALCULATOR_HPP_
# define BACKEND_CALCULATOR_HPP_

# include <string>
# include <string_view>
# include <optional>
# include <exception>

# include "crti_broadcaster.hpp"

namespace calculator
{
    struct cl_arguments;

    class backend_calculator
    {
    public :
        backend_calculator(const cl_arguments& cl_args) noexcept;
        std::pair<bool, std::string> process_line(std::string_view line);

    private :
        const cl_arguments& _cl_args;
        std::optional<network::crti_broadcaster> _crti_broadcaster;

        void sort_crti_and_forward(std::string_view line,
                                   std::string_view res,
                                   double exec_time,
                                   std::exception_ptr except_ptr);

    };
}

#endif
