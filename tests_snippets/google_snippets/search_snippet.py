from tests_support.decorator import *
from tests_snippets.google_snippets.base_snippet import BaseSnippet


@decorate_all_functions(print_on_call)
class GoogleSnippet(BaseSnippet):
    def __init__(self, selenium, data_helper):
        super(GoogleSnippet, self).__init__(selenium, data_helper)

    def search_phrase(self, search_phrase):
        """Search for :param search_phrase:"""
        self.base_page.search_page.fill_search_bar(search_phrase)
        self.base_page.search_page.send_enter_key()
