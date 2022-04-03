from utils.test_utils import test_case

@test_case
def test_invalid_operation(calculator_pexpect):
    calculator_pexpect.sendline("")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation2(calculator_pexpect):
    calculator_pexpect.sendline("\t\t   ")
    calculator_pexpect.expect_exact("\t\t   ")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation3(calculator_pexpect):
    calculator_pexpect.sendline("     ")
    calculator_pexpect.expect_exact("     ")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation4(calculator_pexpect):
    calculator_pexpect.sendline(") 2000 (")
    calculator_pexpect.expect_exact(") 2000 (")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation5(calculator_pexpect):
    calculator_pexpect.sendline(")45  ")
    calculator_pexpect.expect_exact(")45  ")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation6(calculator_pexpect):
    calculator_pexpect.sendline("     +17")
    calculator_pexpect.expect_exact("     +17")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation7(calculator_pexpect):
    calculator_pexpect.sendline("- 9999    \t")
    calculator_pexpect.expect_exact("- 9999    \t")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation8(calculator_pexpect):
    calculator_pexpect.sendline("*32    ")
    calculator_pexpect.expect_exact("*32    ")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation9(calculator_pexpect):
    calculator_pexpect.sendline("   / 4")
    calculator_pexpect.expect_exact("   / 4")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation10(calculator_pexpect):
    calculator_pexpect.sendline("% 87")
    calculator_pexpect.expect_exact("% 87")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation11(calculator_pexpect):
    calculator_pexpect.sendline("a + b")
    calculator_pexpect.expect_exact("a + b")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation12(calculator_pexpect):
    calculator_pexpect.sendline("    p12345")
    calculator_pexpect.expect_exact("    p12345")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation13(calculator_pexpect):
    calculator_pexpect.sendline("\tn000000")
    calculator_pexpect.expect_exact("\tn000000")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation14(calculator_pexpect):
    calculator_pexpect.sendline(" \t   M16")
    calculator_pexpect.expect_exact(" \t   M16")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation15(calculator_pexpect):
    calculator_pexpect.sendline("     42abcd")
    calculator_pexpect.expect_exact("     42abcd")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation16(calculator_pexpect):
    calculator_pexpect.sendline("  42  a")
    calculator_pexpect.expect_exact("  42  a")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation17(calculator_pexpect):
    calculator_pexpect.sendline("13 \t   (42)")
    calculator_pexpect.expect_exact("13 \t   (42)")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation18(calculator_pexpect):
    calculator_pexpect.sendline("5 +")
    calculator_pexpect.expect_exact("5 +")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation19(calculator_pexpect):
    calculator_pexpect.sendline("5 \t-")
    calculator_pexpect.expect_exact("5 \t-")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation20(calculator_pexpect):
    calculator_pexpect.sendline("    5     *")
    calculator_pexpect.expect_exact("    5     *")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation21(calculator_pexpect):
    calculator_pexpect.sendline("   (5)/")
    calculator_pexpect.expect_exact("   (5)/")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation22(calculator_pexpect):
    calculator_pexpect.sendline("       5 %")
    calculator_pexpect.expect_exact("       5 %")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation23(calculator_pexpect):
    calculator_pexpect.sendline("  5 +)")
    calculator_pexpect.expect_exact("  5 +)")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation24(calculator_pexpect):
    calculator_pexpect.sendline("5 -/")
    calculator_pexpect.expect_exact("5 -/")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation25(calculator_pexpect):
    calculator_pexpect.sendline("5 **")
    calculator_pexpect.expect_exact("5 **")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation26(calculator_pexpect):
    calculator_pexpect.sendline("5 /   )")
    calculator_pexpect.expect_exact("5 /   )")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation27(calculator_pexpect):
    calculator_pexpect.sendline(" 5 %   % 5")
    calculator_pexpect.expect_exact(" 5 %   % 5")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation28(calculator_pexpect):
    calculator_pexpect.sendline("2---2")
    calculator_pexpect.expect_exact("2---2")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation29(calculator_pexpect):
    calculator_pexpect.sendline("3 *(5) + --42")
    calculator_pexpect.expect_exact("3 *(5) + --42")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation30(calculator_pexpect):
    calculator_pexpect.sendline("(")
    calculator_pexpect.expect_exact("(")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation31(calculator_pexpect):
    calculator_pexpect.sendline("   4/5   *(")
    calculator_pexpect.expect_exact("   4/5   *(")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation32(calculator_pexpect):
    calculator_pexpect.sendline(" 4 / 2 %(+")
    calculator_pexpect.expect_exact(" 4 / 2 %(+")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation33(calculator_pexpect):
    calculator_pexpect.sendline("\t9+2/(   -")
    calculator_pexpect.expect_exact("\t9+2/(   -")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation34(calculator_pexpect):
    calculator_pexpect.sendline("(**)")
    calculator_pexpect.expect_exact("(**)")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation35(calculator_pexpect):
    calculator_pexpect.sendline("12 )")
    calculator_pexpect.expect_exact("12 )")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation36(calculator_pexpect):
    calculator_pexpect.sendline("((4 + 2) ) )")
    calculator_pexpect.expect_exact("((4 + 2) ) )")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation37(calculator_pexpect):
    calculator_pexpect.sendline(" ((((1))))))))")
    calculator_pexpect.expect_exact(" ((((1))))))))")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation38(calculator_pexpect):
    calculator_pexpect.sendline("  (1)  42")
    calculator_pexpect.expect_exact("  (1)  42")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation39(calculator_pexpect):
    calculator_pexpect.sendline("(1 * 3) 5")
    calculator_pexpect.expect_exact("(1 * 3) 5")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation40(calculator_pexpect):
    calculator_pexpect.sendline("(((5)))          3333")
    calculator_pexpect.expect_exact("(((5)))          3333")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation41(calculator_pexpect):
    calculator_pexpect.sendline("((12")
    calculator_pexpect.expect_exact("((12")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation42(calculator_pexpect):
    calculator_pexpect.sendline("1 * ((2+3) * 4")
    calculator_pexpect.expect_exact("1 * ((2+3) * 4")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation43(calculator_pexpect):
    calculator_pexpect.sendline("(12 + 3) / (3 + 5")
    calculator_pexpect.expect_exact("(12 + 3) / (3 + 5")
    calculator_pexpect.expect_exact("syntax error")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation44(calculator_pexpect):
    calculator_pexpect.sendline("(1/0-5) + 5")
    calculator_pexpect.expect_exact("(1/0-5) + 5")
    calculator_pexpect.expect_exact("attempted to divide by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation45(calculator_pexpect):
    calculator_pexpect.sendline("(3523) * -4 /-0")
    calculator_pexpect.expect_exact("(3523) * -4 /-0")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to divide by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation46(calculator_pexpect):
    calculator_pexpect.sendline("13 / 0")
    calculator_pexpect.expect_exact("13 / 0")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to divide by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation47(calculator_pexpect):
    calculator_pexpect.sendline("1+2+3+4+5+6+7/0%0%0/0")
    calculator_pexpect.expect_exact("1+2+3+4+5+6+7/0%0%0/0")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to divide by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation48(calculator_pexpect):
    calculator_pexpect.sendline("5555555 * (999999999) * 0 % 0 - 42")
    calculator_pexpect.expect_exact("5555555 * (999999999) * 0 % 0 - 42")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to modulo by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation49(calculator_pexpect):
    calculator_pexpect.sendline("((((((42)))))) % 0")
    calculator_pexpect.expect_exact("((((((42)))))) % 0")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to modulo by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation50(calculator_pexpect):
    calculator_pexpect.sendline("-4-6-7-8%-0")
    calculator_pexpect.expect_exact("-4-6-7-8%-0")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to modulo by zero")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_invalid_operation51(calculator_pexpect):
    calculator_pexpect.sendline("3 - 5 * ((((524))))%0 -2367")
    calculator_pexpect.expect_exact("3 - 5 * ((((524))))%0 -2367")
    calculator_pexpect.expect_exact(
        "arithmetic error: attempted to modulo by zero")
    calculator_pexpect.expect_exact("?> ")
