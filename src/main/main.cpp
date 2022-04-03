#include <iostream>
#include <exception>
#include <system_error>
#include <signal.h>
#include <string.h>
#include <sys/types.h>

#include "command_line_argument_parser.hpp"
#include "cl_arguments.hpp"
#include "custom_exceptions.hpp"
#include "backend_calculator.hpp"
#include "shell_calculator.hpp"

using namespace calculator;

void sighandler(int signum)
{
    if (signum == SIGINT);
    else
    {
        throw std::invalid_argument("signal not handled");
    }
}

void handle_signals()
{
    // SIGINT signal
    struct sigaction sigint_act;

    memset(&sigint_act, 0, sizeof(sigint_act));

    sigint_act.sa_handler = &sighandler;

    if (sigaction(SIGINT, &sigint_act, nullptr) == -1)
    {
        throw std::system_error(errno, std::generic_category());
    }


    // SIGPIPE signal
    struct sigaction sigpipe_act;

    memset(&sigpipe_act, 0, sizeof(sigpipe_act));

    sigpipe_act.sa_handler = SIG_IGN;

    if (sigaction(SIGPIPE, &sigpipe_act, nullptr) == -1)
    {
        throw std::system_error(errno, std::generic_category());
    }


    // SIGCHLD signal
    struct sigaction sigchld_act;

    memset(&sigchld_act, 0, sizeof(sigchld_act));

    sigchld_act.sa_handler = SIG_IGN;

    if (sigaction(SIGCHLD, &sigchld_act, nullptr) == -1)
    {
        throw std::system_error(errno, std::generic_category());
    }
}

int main(int argc, char **argv)
{
    try
    {
        command_line_argument_parser cl_arg_parser(argc, argv);
        cl_arguments cl_args = cl_arg_parser.parse_arguments();

        if (cl_args.help)
        {
            return 0;
        }

        // if (cl_args.remote_crti)
        // {
        //     throw custom_exceptions::not_implemented_error(
        //         "remote crti mode not implemented yet");
        // }

        handle_signals();

        backend_calculator backend_calc(cl_args);
        shell_calculator shell_calc(cl_args, backend_calc);

        shell_calc.start();
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return -1;
    }
    catch (...)
    {
        std::cerr << "unknown caught exception\n";
        return -1;
    }

    return 0;
}
