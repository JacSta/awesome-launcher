from page_objects.google.base_page import BasePage


class BaseSnippet(object):
    """All snippets inherit from this"""

    def __init__(self, selenium, data_helper):
        self.selenium = selenium
        self.data_helper = data_helper
        self.base_page = BasePage(selenium, data_helper)
        self.locator = self.base_page.locator

    @property
    def search(self):
        from .search_snippet import GoogleSnippet
        return GoogleSnippet(self.selenium, self.data_helper)
