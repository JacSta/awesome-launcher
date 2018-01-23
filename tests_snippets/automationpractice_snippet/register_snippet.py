from tests_support.decorator import *
from tests_snippets.automationpractice_snippet.base_snippet import BaseSnippet


@decorate_all_functions(print_on_call)
class RegisterSnippet(BaseSnippet):
    def __init__(self, selenium, data_helper):
        super(RegisterSnippet, self).__init__(selenium, data_helper)

    def start_creating_account(self, purchaser_details):
        """Gets through first phase"""
        self.base_page.register_page.click_signin()
        self.base_page.register_page.fill_in_email_address(purchaser_details)

    def create_account(self, purchaser_details):
        """Gets through registry main form"""
        self.base_page.register_page.click_create_an_account()
        self.base_page.register_page.fill_in_personal_information_form(purchaser_details)
        self.base_page.register_page.assert_order_history_is_visible()
