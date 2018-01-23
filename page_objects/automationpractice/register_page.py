from tests_support.decorator import *
from .base_page import BasePage


@decorate_all_functions(print_on_call)
class RegisterPage(BasePage):
    def __init__(self, selenium, data_helper):
        super(RegisterPage, self).__init__(selenium, data_helper)

    def click_signin(self):
        """Click Sign In button"""
        self.selenium.wait_for_element_visible(self.locator.register_locators.BTN_signIn)
        self.selenium.click(self.locator.register_locators.BTN_signIn)

    def fill_in_email_address(self, purchaser_details):
        """Fill in email adress field"""
        self.selenium.wait_for_element_visible(self.locator.register_locators.INPUT_email)
        self.selenium.send_keys(self.locator.register_locators.INPUT_email, purchaser_details['pEmail'])

    def click_create_an_account(self):
        """Click create an account button"""
        self.selenium.click(self.locator.register_locators.BTN_createAnAccount)

    def fill_in_personal_information_form(self, purchaser_details):
        """Fills in registry form"""
        self.selenium.wait_for_element_visible(self.locator.register_locators.RADIOBTN_titleGender)
        self.selenium.click(self.locator.register_locators.RADIOBTN_titleGender)
        self.selenium.send_keys(self.locator.register_locators.INPUT_firstName, purchaser_details['pName'])
        self.selenium.send_keys(self.locator.register_locators.INPUT_lastName, purchaser_details['pSurname'])
        self.selenium.send_keys(self.locator.register_locators.INPUT_password, 'test567!')
        self.selenium.click(self.locator.register_locators.DROPDOWN_day)
        self.selenium.click(self.locator.register_locators.DROPDOWN_selectDay)
        self.selenium.click(self.locator.register_locators.DROPDOWN_month)
        self.selenium.click(self.locator.register_locators.DROPDOWN_selectMonth)
        self.selenium.click(self.locator.register_locators.DROPDOWN_year)
        self.selenium.click(self.locator.register_locators.DROPDOWN_selectYear)
        self.selenium.send_keys(self.locator.register_locators.INPUT_addressStreet, purchaser_details['pStreetName'])
        self.selenium.send_keys(self.locator.register_locators.INPUT_addressCity, purchaser_details['pCity'])
        self.selenium.click(self.locator.register_locators.DROPDOWN_state)
        self.selenium.click(self.locator.register_locators.DROPDOWN_stateSelectGeorgia)
        self.selenium.send_keys(self.locator.register_locators.INPUT_postCode, purchaser_details['pPostalCode'])
        self.selenium.send_keys(self.locator.register_locators.INPUT_mobilePhone, purchaser_details['pPhone'])
        self.selenium.click(self.locator.register_locators.BTN_register)

    def assert_order_history_is_visible(self):
        """Checks 'Order History and Details'"""
        button_visible = self.selenium.get_element_visibility(
            self.locator.register_locators.BTN_orderHistoryAndDetails)
        self.selenium.unittest.assertTrue(button_visible,
                                          msg="Order History And Details is not visible, probably registration failed")
