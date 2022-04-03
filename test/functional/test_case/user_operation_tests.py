from utils.test_utils import test_case

@test_case
def test_operation(calculator_pexpect):
    calculator_pexpect.sendline("7")
    calculator_pexpect.expect_exact("7")
    calculator_pexpect.expect_exact("7")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation2(calculator_pexpect):
    calculator_pexpect.sendline("-21")
    calculator_pexpect.expect_exact("-21")
    calculator_pexpect.expect_exact("-21")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation3(calculator_pexpect):
    calculator_pexpect.sendline("(766)")
    calculator_pexpect.expect_exact("(766)")
    calculator_pexpect.expect_exact("766")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation4(calculator_pexpect):
    calculator_pexpect.sendline("(-42)")
    calculator_pexpect.expect_exact("(-42)")
    calculator_pexpect.expect_exact("-42")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation5(calculator_pexpect):
    calculator_pexpect.sendline("(\t\t-352\t\t)")
    calculator_pexpect.expect_exact("(\t\t-352\t\t)")
    calculator_pexpect.expect_exact("-352")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation6(calculator_pexpect):
    calculator_pexpect.sendline("((((99999999999999999999))))")
    calculator_pexpect.expect_exact("((((99999999999999999999))))")
    calculator_pexpect.expect_exact("99999999999999999999")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation7(calculator_pexpect):
    calculator_pexpect.sendline("((((((((((-000001234567890000))))))))))")
    calculator_pexpect.expect_exact("((((((((((-000001234567890000))))))))))")
    calculator_pexpect.expect_exact("-1234567890000")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation8(calculator_pexpect):
    calculator_pexpect.sendline("95 -   32")
    calculator_pexpect.expect_exact("95 -   32")
    calculator_pexpect.expect_exact("63")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation9(calculator_pexpect):
    calculator_pexpect.sendline("  0 - -0")
    calculator_pexpect.expect_exact("  0 - -0")
    calculator_pexpect.expect_exact("0")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation10(calculator_pexpect):
    calculator_pexpect.sendline("-52 --52")
    calculator_pexpect.expect_exact("-52 --52")
    calculator_pexpect.expect_exact("0")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation11(calculator_pexpect):
    calculator_pexpect.sendline("-532 -  \t-194")
    calculator_pexpect.expect_exact("-532 -  \t-194")
    calculator_pexpect.expect_exact("-338")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation12(calculator_pexpect):
    calculator_pexpect.sendline("  80 / -50   ")
    calculator_pexpect.expect_exact("  80 / -50   ")
    calculator_pexpect.expect_exact("-1")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation13(calculator_pexpect):
    calculator_pexpect.sendline("999999999999999 * 999999999")
    calculator_pexpect.expect_exact("999999999999999 * 999999999")
    calculator_pexpect.expect_exact("999999998999999000000001")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation14(calculator_pexpect):
    calculator_pexpect.sendline("-427429874974123139 - 0000323291881313003")
    calculator_pexpect.expect_exact(
        "-427429874974123139 - 0000323291881313003")
    calculator_pexpect.expect_exact("-427753166855436142")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation15(calculator_pexpect):
    calculator_pexpect.sendline("9913332429474297492749 / 1")
    calculator_pexpect.expect_exact("9913332429474297492749 / 1")
    calculator_pexpect.expect_exact("9913332429474297492749")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation16(calculator_pexpect):
    calculator_pexpect.sendline("\t    -654 % 4")
    calculator_pexpect.expect_exact("\t    -654 % 4")
    calculator_pexpect.expect_exact("-2")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation17(calculator_pexpect):
    calculator_pexpect.sendline("2 + 6 - 1")
    calculator_pexpect.expect_exact("2 + 6 - 1")
    calculator_pexpect.expect_exact("7")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation18(calculator_pexpect):
    calculator_pexpect.sendline("-0-1-2-3-4-5-6")
    calculator_pexpect.expect_exact("-0-1-2-3-4-5-6")
    calculator_pexpect.expect_exact("-21")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation19(calculator_pexpect):
    calculator_pexpect.sendline("  ((1+2) * 4)   + 3")
    calculator_pexpect.expect_exact("  ((1+2) * 4)   + 3")
    calculator_pexpect.expect_exact("15")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation20(calculator_pexpect):
    calculator_pexpect.sendline("5   *   3 + 4 \t")
    calculator_pexpect.expect_exact("5   *   3 + 4 \t")
    calculator_pexpect.expect_exact("19")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation21(calculator_pexpect):
    calculator_pexpect.sendline("52 * ((52))")
    calculator_pexpect.expect_exact("52 * ((52))")
    calculator_pexpect.expect_exact("2704")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation22(calculator_pexpect):
    calculator_pexpect.sendline(" \t   \t  (-5) / (-42)-99")
    calculator_pexpect.expect_exact(" \t   \t  (-5) / (-42)-99")
    calculator_pexpect.expect_exact("-99")
    calculator_pexpect.expect_exact("?> ")
@test_case
def test_operation23(calculator_pexpect):
    calculator_pexpect.sendline("3 * ((1 + 4)    *6) /42")
    calculator_pexpect.expect_exact("3 * ((1 + 4)    *6) /42")
    calculator_pexpect.expect_exact("2")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation24(calculator_pexpect):
    calculator_pexpect.sendline("(12      + 4)")
    calculator_pexpect.expect_exact("(12      + 4)")
    calculator_pexpect.expect_exact("16")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation25(calculator_pexpect):
    calculator_pexpect.sendline("(5/3)    + (((5 * 9)))%42")
    calculator_pexpect.expect_exact("(5/3)    + (((5 * 9)))%42")
    calculator_pexpect.expect_exact("4")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation26(calculator_pexpect):
    calculator_pexpect.sendline("    (5) * ((((8 -    3))))")
    calculator_pexpect.expect_exact("    (5) * ((((8 -    3))))")
    calculator_pexpect.expect_exact("25")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation27(calculator_pexpect):
    calculator_pexpect.sendline("5*(8-3)*3+((3-1)*2)/3")
    calculator_pexpect.expect_exact("5*(8-3)*3+((3-1)*2)/3")
    calculator_pexpect.expect_exact("76")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation28(calculator_pexpect):
    calculator_pexpect.sendline("   (21+ (42 / 9)-76   % -2)")
    calculator_pexpect.expect_exact("   (21+ (42 / 9)-76   % -2)")
    calculator_pexpect.expect_exact("25")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation29(calculator_pexpect):
    calculator_pexpect.sendline("-6 -18 *    4 % 10 + (-5 - -9) * -42")
    calculator_pexpect.expect_exact("-6 -18 *    4 % 10 + (-5 - -9) * -42")
    calculator_pexpect.expect_exact("-176")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation30(calculator_pexpect):
    calculator_pexpect.sendline("4242 % 4242 +  (   50 -  50  \t) / 50 -9")
    calculator_pexpect.expect_exact("4242 % 4242 +  (   50 -  50  \t) / 50 -9")
    calculator_pexpect.expect_exact("-9")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation31(calculator_pexpect):
    calculator_pexpect.sendline(
        "  \t   \t(((800)))*(1 - 2)     / 43 % 57 + ((32 * 9999) * -42)")
    calculator_pexpect.expect_exact(
        "  \t   \t(((800)))*(1 - 2)     / 43 % 57 + ((32 * 9999) * -42)")
    calculator_pexpect.expect_exact("-13438674")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation32(calculator_pexpect):
    calculator_pexpect.sendline(
        "3 + (5 - 9 * 45225525525) % 12 + 9999999999999999")
    calculator_pexpect.expect_exact(
        "3 + (5 - 9 * 45225525525) % 12 + 9999999999999999")
    calculator_pexpect.expect_exact("9999999999999998")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation33(calculator_pexpect):
    calculator_pexpect.sendline(
        "111111*22222222*333333333*444444444*55555555555555*66666666")
    calculator_pexpect.expect_exact(
        "111111*22222222*333333333*444444444*55555555555555*66666666")
    calculator_pexpect.expect_exact(
        "1354805640061660168348427617441528359717658213075920")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation34(calculator_pexpect):
    calculator_pexpect.sendline(
        "1354805640061660168348427617441528359717658213075920/   6")
    calculator_pexpect.expect_exact(
        "1354805640061660168348427617441528359717658213075920/   6")
    calculator_pexpect.expect_exact(
        "225800940010276694724737936240254726619609702179320")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation35(calculator_pexpect):
    calculator_pexpect.sendline(
    "3232830238393028330823823038290893203"
        " * 32832382038320832038238298328328323230298303"
        " + 4248240814810984199999999999"
        " * 9999999999999999999"
        " - 131813018310938")
    calculator_pexpect.expect_exact(
    "3232830238393028330823823038290893203"
        " * 32832382038320832038238298328328323230298303"
        " + 4248240814810984199999999999"
        " * 9999999999999999999"
        " - 131813018310938")
    calculator_pexpect.expect_exact(
        "106141517451955716868027248430820809388855035"
        "049254374964710458392669280986823572")
    calculator_pexpect.expect_exact("?> ")

@test_case
def test_operation36(calculator_pexpect):
    calculator_pexpect.sendline(
        "-9090792873973739233"
        " + 31312812018242424"
        " * 9993939392192939393"
        " % 355525"
        " * -999999999999999999999999999999")
    calculator_pexpect.expect_exact(
        "-9090792873973739233"
        " + 31312812018242424"
        " * 9993939392192939393"
        " % 355525"
        " * -999999999999999999999999999999")
    calculator_pexpect.expect_exact(
        "-239282000000000009090792873973499951")
    calculator_pexpect.expect_exact("?> ")
