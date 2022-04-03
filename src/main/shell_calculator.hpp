#ifndef SHELL_CALCULATOR_HPP_
# define SHELL_CALCULATOR_HPP_

namespace calculator
{
    struct cl_arguments;
    class backend_calculator;

    class shell_calculator
    {
    public :
        shell_calculator(const cl_arguments& cl_args,
                         backend_calculator& backend_calc) noexcept;
        void start();

    private :
        const cl_arguments& _cl_args;
        backend_calculator& _backend_calc;
    };
}

#endif
