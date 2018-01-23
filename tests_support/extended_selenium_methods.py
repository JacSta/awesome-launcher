import traceback
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.select import Select
from tests_environment.set_env_config import SetEnvConfig
from tests_environment.session_creator import WebDriverSessionCreator


class ExtendedSeleniumMethods:
    def __init__(self, unittest):
        self.unittest = unittest
        self.driver = WebDriverSessionCreator().create_session()
        self.config = SetEnvConfig().set_env_config()
        self.actions = ActionChains(self.driver)

    def get_url(self, app_url, sub_page=''):
        # Opens given url address
        self.driver.get(app_url + sub_page)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)

    def set_custom_window_size(self):
        if SetEnvConfig().set_resolution() == 'max':
            self.max_window_size()
            if SetEnvConfig().set_browser() == 'firefox':
                self.max_window_size()
        elif SetEnvConfig().set_resolution() in SetEnvConfig().set_resolutions_list():
            self.max_window_size()
            size = self.driver.get_window_size()
            self.driver.set_window_size(SetEnvConfig().set_resolution(), size['height'] - 15)
            self.driver.set_window_position(0, 0)

    def max_window_size(self):
        self.driver.maximize_window()

    def __find_element(self, element):
        return self.driver.find_element(*element)

    def __find_elements(self, element):
        return self.driver.find_elements(*element)

    def click(self, element):
        # Clicks into given element
        return self.__find_element(element).click()

    def send_keys(self, element, value):
        # Send keys to element input/text area
        self.clean_input(element)
        self.__find_element(element).send_keys(value)

    def clean_input(self, element):
        # Cleans input/text area element from value
        self.__find_element(element).clear()

    def move_mouse_over(self, element, click=False):
        # Moves mouse cursor over given element
        if click is False:
            self.actions.move_to_element(self.__find_element(element)).perform()
        else:
            self.actions.move_to_element(self.__find_element(element)).click().perform()
        self.actions.reset_actions()

    def select_from_dropdown_by_value(self, selector, value):
        # Select from drop down menu by value
        return Select(self.__find_element(selector)).select_by_value(value)

    def wait_for_element_visible(self, element, time_out=30):
        # Waits for element visible for 30 seconds (default)
        try:
            WebDriverWait(self.driver, time_out, 0.25).until(
                expected_conditions.visibility_of_element_located(
                    element
                )
            )
        except (NoSuchElementException, Exception):
            print("\nElement ".join(map(str, element)), " is not visible\n")
            traceback.print_exc()
            raise

    def wait_for_element_non_visible(self, element, time_out=10):
        # Wait for element non visible for 10 seconds (default)
        try:
            WebDriverWait(self.driver, time_out, 0.25).until(
                expected_conditions.invisibility_of_element_located(
                    element
                )
            )
        except (NoSuchElementException, Exception):
            print("\nElement ".join(map(str, element)), " is still visible\n")
            traceback.print_exc()
            raise

    def get_element_visibility(self, element):
        # Returns information about element visibility without raising an exception
        try:
            self.__find_element(element).is_displayed()
            return True
        except (NoSuchElementException, Exception):
            return False

    def get_attribute_from_element(self, element, attribute):
        # Returns attribute value from given element
        return self.__find_element(element).get_attribute(attribute)

    def get_text(self, element):
        # Returns text from given element
        return self.__find_element(element).text

    def get_current_url(self):
        # Returns current url address
        return self.driver.current_url

    def assert_text_from_element(self, element, expected):
        # Gets text from given element and assert it with :param expected:
        actual = self.get_text(element)
        self.unittest.assertEqual(expected, actual)

    def accept_browser_alert(self):
        # Accepts browser alert
        alert = self.driver.switch_to_alert()
        alert.accept()

    @staticmethod
    def sleep(sleep_time):
        sleep(sleep_time)

    def refresh_current_page(self):
        self.driver.refresh()

    def find_visible_element(self, element):
        # Search for all elements on page by given locator and returns only visible element
        elements = self.__find_elements(element)
        elem_visible = next(elem for elem in elements if elem.is_displayed())
        return elem_visible

    def check_if_element_is_click_able(self, element):
        # Returns information whether given element is clickable
        try:
            elements = self.__find_elements(element)
            next(elem for elem in elements if elem.is_displayed())
            return True
        except (NoSuchElementException, Exception):
            return False

    def scroll_to_element(self, element):
        # Scrolls to given element
        elem = self.__find_element(element)
        self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
        sleep(0.5)

    def scroll_to_top(self):
        # Scrolls to top of the page
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        # Scrolls to bottom of the page
        self.driver.execute_script("window.scrollTo(0, 2000);")

    def scroll_custom_value(self, y):
        # Scrolls page by custom value
        self.driver.execute_script("window.scrollTo(0, %s);" % y)

    def execute_script(self, script):
        return self.driver.execute_script(script)
