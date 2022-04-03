#ifndef COMMAND_LINE_ARGUMENTS_PARSER_HPP_
# define COMMAND_LINE_ARGUMENTS_PARSER_HPP_

# include "cl_arguments.hpp"

namespace calculator
{
    class command_line_argument_parser
    {
    public :
        command_line_argument_parser(int argc, char **argv) noexcept;
        cl_arguments parse_arguments();

    private :
        int _argc;
        char **_argv;
    };
}

#endif
