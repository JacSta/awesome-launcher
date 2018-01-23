import sys
from tests_cases import TestsCases
from tests_builder.tests_suites import TestsSuites
from tests_builder.tests_runner import TestsRunner
from tests_environment.set_env_config import SetEnvConfig


class TestsExecutor:
    def __init__(self):
        if SetEnvConfig().set_test_case() != 'print':
            print(SetEnvConfig().set_env_config())
            print("--- Run %s for resolution %s ---"
                  % (SetEnvConfig().set_test_case().upper(),
                     SetEnvConfig().set_original_resolution()))

    @staticmethod
    def executor():
        if SetEnvConfig().set_test_case() == 'print':
            # Print all available test cases
            print("-- All available test cases --")
            for key in TestsCases().test_cases():
                print("    " + key)
        else:
            # Run selected test case
            tests = TestsSuites().set_test_suite()
            result = TestsRunner().test_runner(tests)
            return sys.exit(result)


TestsExecutor().executor()
