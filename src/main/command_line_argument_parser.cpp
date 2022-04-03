#include <boost/program_options.hpp>
#include <iostream>
#include <errno.h>
#include <stdexcept>

#include "command_line_argument_parser.hpp"

namespace po = boost::program_options;

namespace calculator
{
    command_line_argument_parser::command_line_argument_parser(
        int argc, char **argv) noexcept : _argc(argc), _argv(argv)
    { }

    cl_arguments command_line_argument_parser::parse_arguments()
    {
        po::options_description desc("allowed options");

        desc.add_options()
            ("help,h",
             "show this help and exit")
            ("local_crti,l",
             "enable calculator real time info sending "
             "to local python script only");
            // ("remote_crti,r",
            //  "enable calculator real time info sending "
            //  "to remote python script [to use with -i, -p options]")
            // ("remote_crti_ip,i",
            //  po::value<std::string>(),
            //  "ip address where server runs to enable remote "
            //  "python script to connect")
            // ("remote_crti_port,p",
            //  po::value<uint16_t>(),
            //  "port where server runs to enable remote python "
            //  "script to connect");

        po::variables_map vm;

        po::store(po::parse_command_line(_argc, _argv, desc), vm);
        po::notify(vm);

        //cl_arguments cl_args{false, false, false, "", 0};
        cl_arguments cl_args{false, false};

        if (vm.count("help"))
        {
            std::cout << "usage: ./" << program_invocation_short_name
                      // << " [-h] [-l] [-r] [-i] [-p]\n\n"
                      << " [-h] [-l]\n\n"
                      << desc
                      << std::flush;
            cl_args.help = true;
        }

        // if (vm.count("local_crti") && vm.count("remote_crti"))
        // {
        //     throw std::invalid_argument("use either -l or -r options");
        // }
        // else if (vm.count("local_crti"))
        // {
        //     cl_args.local_crti = true;
        // }
        // else if (vm.count("remote_crti"))
        // {
        //     cl_args.remote_crti = true;

        //     if (vm.count("remote_crti_ip"))
        //     {
        //         cl_args.remote_crti_ip =
        //             vm["remote_crti_ip"].as<std::string>();
        //     }
        //     else
        //     {
        //         throw std::invalid_argument("missing -i option");
        //     }

        //     if (vm.count("remote_crti_port"))
        //     {
        //         cl_args.remote_crti_port =
        //             vm["remote_crti_port"].as<unsigned short>();
        //     }
        //     else
        //     {
        //         throw std::invalid_argument("missing -p option");
        //     }
        // }
        if (vm.count("local_crti"))
        {
            cl_args.local_crti = true;
        }

        return cl_args;
    }
}
