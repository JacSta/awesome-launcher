from page_objects.automationpractice.base_page import BasePage


class BaseSnippet(object):
    """All snippets inherit from this"""

    def __init__(self, selenium, data_helper):
        self.selenium = selenium
        self.data_helper = data_helper
        self.base_page = BasePage(selenium, data_helper)
        self.locator = self.base_page.locator

    @property
    def register_snippet(self):
        from .register_snippet import RegisterSnippet
        return RegisterSnippet(self.selenium, self.data_helper)
