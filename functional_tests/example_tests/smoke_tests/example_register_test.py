from tests_support.decorator import *
from tests_environment.tests_setup import *


@decorate_all_functions(print_scenario_on_fail)
class RegistrationExampleTest(TestsSetup):
    def test_registration(self):
        """
        | Example Scenario
        | Scenario:
        |   1. Starts registering process
        |   2. Fills in register form
        |   3. Checks that registration was successful
        """
        purchaser_details = self.data_helper.purchaser_details_array()

        self.snippet.register_snippets.register_snippet.start_creating_account(purchaser_details)
        self.snippet.register_snippets.register_snippet.create_account(purchaser_details)
