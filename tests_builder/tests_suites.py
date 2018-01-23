from tests_environment.set_env_config import SetEnvConfig
from tests_cases import TestsCases


class TestsSuites:
    @staticmethod
    def __test_cases_list():
        return TestsCases().test_cases()

    def set_test_suite(self):
        for key, value in self.__test_cases_list().items():
            if SetEnvConfig().set_test_case() == key:
                return value
            elif SetEnvConfig().set_test_case() not in self.__test_cases_list():
                print("Test case not found\n")
                break
