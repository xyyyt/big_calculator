import pexpect
from utils.test_utils import test_case, test_case_error

@test_case
def test_help_user_command(calculator_pexpect):
    calculator_pexpect.sendline("quit")
    calculator_pexpect.expect_exact("quit")
    calculator_pexpect.expect_exact(pexpect.EOF)

    if calculator_pexpect.isalive():
        raise test_case_error("calculator process still alive")
