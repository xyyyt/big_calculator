import pexpect.exceptions
import os
import errno
import functools
from time import time
import inspect
from utils.timeout import timeout, timeout_error

class test_case_error(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

# "test_case" decorator usages :
# - @test_case
# - @test_case()
# - @test_case(timeout_seconds=42)
# - @test_case(timeout_seconds=42, timeout_error_message="test")
#
# any other use will be ignored about arguments
def test_case(*args, **kwargs):
    def decorator(test):
        @functools.wraps(test)
        def wrapper(calculator_pexpect):
            timeout_seconds = kwargs.get("timeout_seconds", 10)
            timeout_error_message = kwargs.get(
                "timeout_error_message", os.strerror(errno.ETIME))
            success = False
            test_error_info = None
            start_time = time()

            try:
                timeout(timeout_seconds, timeout_error_message)(test)(
                    calculator_pexpect)
            except (test_case_error, timeout_error,
                    pexpect.exceptions.EOF, pexpect.exceptions.TIMEOUT) as e:
                test_error_info = e
            else:
                success = True

            end_time = time()

            return success, test_error_info, (end_time - start_time) * 1000

        return wrapper

    return decorator(args[0]) \
        if len(args) == 1 and callable(args[0]) and not len(kwargs) \
        else decorator

def has_test_case_decorator(func):
    source_code_text = inspect.getsource(func)
    def_keyword_index = source_code_text.find("def ")

    for line in source_code_text[:def_keyword_index].splitlines():
        if line.strip().startswith("@test_case"):
            return True

    return False

def unwrap(func):
    if hasattr(func, "__wrapped__"):
        func = func.__wrapped__

    return func
