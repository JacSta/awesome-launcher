from functional_tests import *
from tests_builder.tests_runner import TestsRunner


class TestsCases:
    def test_cases(self):
        return {
            ExampleTestCases().example_smoke_test_search.__name__: ExampleTestCases().example_smoke_test_search(),
            ExampleTestCases().example_smoke_test_register.__name__: ExampleTestCases().example_smoke_test_register()
        }


class ExampleTestCases:
    @staticmethod
    def example_smoke_test_search():
        return [
            TestsRunner().test_case_loader(example_smoke_test.ExampleTest)
        ]

    @staticmethod
    def example_smoke_test_register():
        return [
            TestsRunner().test_case_loader(example_smoke_test.RegistrationExampleTest)
        ]
