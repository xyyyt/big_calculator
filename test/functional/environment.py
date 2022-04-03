import pexpect
import inspect
from utils import utils
from utils import test_utils
from utils.color import color
from test_case import user_operation_tests, user_invalid_operation_tests, \
    user_special_cmd_tests

class environment:
    def __init__(self, calculator_exec_path):
        self._calculator_exec_path = calculator_exec_path
        self._calculator_pexpect = None
        self._tests = []

        self._get_all_tests()

    def __del__(self):
        if self._calculator_pexpect.isalive():
            self._calculator_pexpect.close()

    def get_nb_test(self):
        return len(self._tests)

    def execute_all_tests(self):
        self._spawn_calculator_process()

        for testname, test in self._tests:
            if not self._calculator_pexpect.isalive():
                self._spawn_calculator_process()

            print(f"{testname} : running...")

            success, _, elapsed_time = test(self._calculator_pexpect)
            test_status_msg = f"{color.GREEN}OK !{color.END}" \
                if success else f"{color.RED}FAILED...{color.END}"

            print(f"\033[F{testname} : {test_status_msg} "
                  f"({elapsed_time} ms)")

    def _get_all_tests(self):
        test_case_modules = list(dict.fromkeys(
            [user_operation_tests,
             user_invalid_operation_tests,
             user_special_cmd_tests]))
        tests = []

        for test_case_module in test_case_modules:
            tests.extend(
                environment._get_all_tests_from_module(test_case_module))

        if utils.check_list_has_duplicates(
                [funcname for funcname, _ in tests]):
            print(f"[MIDDLE STATUS] {color.YELLOW}WARNING : test name "
                  "duplication found, these tests will not be included on "
                  f"execution !!!{color.END}")

        self._tests = list(dict.fromkeys(tests))

    @staticmethod
    def _get_all_tests_from_module(test_case_module):
        test_case_module_funcs = \
            [o for o in inspect.getmembers(
                test_case_module, inspect.isfunction)]
        tests = []

        test_case_module_funcs.sort(
            key=lambda o : inspect.getsourcelines(o[1])[1])

        for funcname, func in test_case_module_funcs:
            if test_utils.has_test_case_decorator(test_utils.unwrap(func)):
                tests.append((funcname, func))

        return tests

    def _spawn_calculator_process(self):
        try:
            self._calculator_pexpect = pexpect.spawn(
                self._calculator_exec_path, timeout=10)
            self._calculator_pexpect.expect_exact(
                'Large integral number calculator made by "xyyyt".')
            self._calculator_pexpect.expect_exact(
                'Type "quit" if you want to stop program.')
            self._calculator_pexpect.expect_exact("?> ")
        except (pexpect.exceptions.EOF, pexpect.exceptions.TIMEOUT):
            raise RuntimeError("no matching user welcome message")
