from page_objects.google.locators.base_locators import BaseLocators


class BasePage(object):
    """All page objects inherit from this"""

    def __init__(self, selenium, data_helper):
        self.selenium = selenium
        self.data_helper = data_helper
        self.locator = BaseLocators()

    @property
    def search_page(self):
        from .search_page import SearchPage
        return SearchPage(self.selenium, self.data_helper)
