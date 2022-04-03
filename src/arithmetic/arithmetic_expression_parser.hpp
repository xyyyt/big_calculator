#ifndef ARITHMETIC_EXPRESSION_PARSER_HPP_
# define ARITHMETIC_EXPRESSION_PARSER_HPP_

# include <string_view>

namespace calculator::arithmetic
{
    void is_arithmetic_expression(std::string_view line);
}

#endif
