from tests_support.decorator import *
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


@decorate_all_functions(print_on_call)
class SearchPage(BasePage):
    def __init__(self, selenium, data_helper):
        super(SearchPage, self).__init__(selenium, data_helper)

    def fill_search_bar(self, search_phrase):
        """Fill search field"""
        self.selenium.wait_for_element_visible(self.locator.google_locators.ELEMENT_logo)
        self.selenium.send_keys(self.locator.google_locators.INPUT_search, search_phrase)
        self.selenium.sleep(0.5)

    def click_search_button(self):
        """Click search button"""
        self.selenium.click(self.locator.google_locators.BTN_search)
        self.selenium.sleep(0.5)

    def send_enter_key(self):
        self.selenium.send_keys(self.locator.google_locators.INPUT_search, Keys.RETURN)
        self.selenium.sleep(0.5)
