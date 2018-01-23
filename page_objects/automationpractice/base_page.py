from page_objects.automationpractice.locators.base_locators import BaseLocators


class BasePage(object):
    """All page objects inherit from this"""

    def __init__(self, selenium, data_helper):
        self.selenium = selenium
        self.data_helper = data_helper
        self.locator = BaseLocators()

    @property
    def register_page(self):
        from .register_page import RegisterPage
        return RegisterPage(self.selenium, self.data_helper)
