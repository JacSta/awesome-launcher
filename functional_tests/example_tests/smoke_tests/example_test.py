from tests_support.decorator import *
from tests_environment.tests_setup import *


@decorate_all_functions(print_scenario_on_fail)
class ExampleTest(TestsSetup):
    def test_example(self):
        """
        | Example Scenario
        | Scenario:
        |   1. Step1
        |   2. Step2
        """
        self.snippet.google_snippets.search.search_phrase("pizza")
