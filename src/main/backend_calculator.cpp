#include <list>
#include <chrono>
#include <exception>

#include "cl_arguments.hpp"
#include "custom_exceptions.hpp"
#include "arithmetic_expression_parser.hpp"
#include "reverse_polish_notation.hpp"
#include "arithmetic_operation.hpp"
#include "crti_data.hpp"
#include "backend_calculator.hpp"

using namespace std::string_view_literals;

namespace calculator
{
    backend_calculator::backend_calculator(const cl_arguments& cl_args)
        noexcept : _cl_args(cl_args),
                   _crti_broadcaster(cl_args.local_crti ?
                       std::make_optional<network::crti_broadcaster>()
                                     : std::nullopt)
    { }

    std::pair<bool, std::string> backend_calculator::process_line(
        std::string_view line)
    {
        struct arithmetic_operations
        {
            std::string add(std::string_view s, std::string_view s2) const
            {
                return arithmetic::add(s, s2);
            }

            std::string sub(std::string_view s, std::string_view s2) const
            {
                return arithmetic::sub(s, s2);
            }

            std::string mult(std::string_view s, std::string_view s2) const
            {
                return arithmetic::mult(s, s2);
            }

            std::string div(std::string_view s, std::string_view s2) const
            {
                return arithmetic::div(s, s2);
            }

            std::string mod(std::string_view s, std::string_view s2) const
            {
                return arithmetic::mod(s, s2);
            }
        } operations;
        bool success = false;
        std::string res;
        std::exception_ptr except_ptr;

        auto start = std::chrono::steady_clock::now();

        try
        {
            arithmetic::is_arithmetic_expression(line);

            std::list<std::string_view> rpn_expression =
                arithmetic::to_rpn(line);

            res = arithmetic::rpn_evaluate(operations, rpn_expression);
            success = true;
        }
        catch (const custom_exceptions::parsing_error& e)
        {
            except_ptr = std::current_exception();
            res = "syntax error";
        }
        catch (const custom_exceptions::arithmetic_error& e)
        {
            except_ptr = std::current_exception();

            auto arithmetic_error_msg_sv = "arithmetic error: "sv;
            std::string_view arithmetic_error_what_msg_sv = e.what();

            res.reserve(arithmetic_error_msg_sv.length()
                        + arithmetic_error_what_msg_sv.length());
            res.append(arithmetic_error_msg_sv.data())
                .append(arithmetic_error_what_msg_sv.data());
        }

        auto end = std::chrono::steady_clock::now();

        if (_cl_args.local_crti)
        {
            this->sort_crti_and_forward(
                line,
                res,
                std::chrono::duration_cast<std::chrono::microseconds>(
                    end - start).count(),
                except_ptr);
        }

        return {success, res};
    }

    void backend_calculator::sort_crti_and_forward(
        std::string_view line,
        std::string_view res,
        double exec_time,
        std::exception_ptr except_ptr)
    {
        std::string reformated_result;

        if (except_ptr)
        {
            try
            {
                std::rethrow_exception(except_ptr);
            }
            catch (const custom_exceptions::parsing_error& e)
            {
                reformated_result.assign(e.what());
            }
            catch (const custom_exceptions::arithmetic_error& e)
            {
                auto substr = res.substr(res.find_first_of(':') + 1);

                substr = substr.substr(substr.find_first_not_of(' '));
                reformated_result.assign(substr.data(), substr.length());
            }
        }
        else
        {
            reformated_result.assign(res.data(), res.length());
        }

        _crti_broadcaster->forward_to_all(
            {std::string(line.data(), line.length()),
             std::move(reformated_result),
             exec_time});
    }
}
