#include <iostream>
#include <system_error>
#include <errno.h>
#include <unistd.h>

#include "cl_arguments.hpp"
#include "command_line_argument_parser.hpp"
#include "backend_calculator.hpp"
#include "shell_calculator.hpp"

namespace
{
    std::string_view trim(std::string_view line)
    {
        size_t start_pos = line.find_first_not_of(" \t");
        size_t end_pos = line.find_last_not_of(" \t") + 1;
        size_t pos = 0;
        size_t count = std::string_view::npos;

        if (start_pos == std::string_view::npos
            && end_pos != std::string_view::npos)
        {
            count = end_pos;
        }
        else if (start_pos != std::string_view::npos
                 && end_pos == std::string_view::npos)
        {
            pos = start_pos;
        }
        else if (start_pos != std::string_view::npos
                 && end_pos != std::string_view::npos)
        {
            pos = start_pos;
            count = end_pos - start_pos;
        }

        return line.substr(pos, count);
    }
}

namespace calculator
{
    shell_calculator::shell_calculator(const cl_arguments& cl_args,
                                       backend_calculator& backend_calc)
        noexcept : _cl_args(cl_args), _backend_calc(backend_calc)
    { }

    void shell_calculator::start()
    {
        constexpr const char *AUTHORS = "xyyyt";

        std::cout << "Large integral number calculator made by \""
                  << AUTHORS
                  << "\".\nType \"quit\" if you want to stop program.\n"
                  << std::endl;

        constexpr const char *PROMPT = "?>";
        char buffer[2048];

        while (1)
        {
            std::cout << PROMPT << " " << std::flush;

            ssize_t size = read(0, buffer, sizeof(buffer));

            if (size == -1)
            {
                if (errno == EINTR)
                {
                    std::cout << std::endl;

                    break;
                }

                throw std::system_error(errno, std::generic_category());
            }
            else if (!size)
            {
                // On EOF
                std::cout << std::endl;

                break;
            }

            // size - 1 : to remove '\n' character
            buffer[size - 1] = '\0';

            auto line = std::string_view(buffer, size - 1);
            auto trimmed_line = trim(line);

            if (trimmed_line.empty())
            {
                continue;
            }
            else if (trimmed_line == "quit")
            {
                break;
            }

            auto [success, res] = _backend_calc.process_line(trimmed_line);
            std::ostream& os = (success) ? std::cout : std::cerr;

            os << res << std::endl;
        }
    }
}
