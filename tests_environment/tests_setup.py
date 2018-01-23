import unittest
from tests_environment.set_env_config import SetEnvConfig
from tests_snippets.snippets_initializer import SnippetInitializer
from tests_support.extended_selenium_methods import ExtendedSeleniumMethods
from tests_support.data_helper import Details


class TestsSetup(unittest.TestCase):
    def setUp(self):
        # Start session for given browser and url address
        self.logged = 1
        self.unittest = unittest.TestCase()
        self.selenium = ExtendedSeleniumMethods(self.unittest)
        self.data_helper = Details(self.selenium)
        self.snippet = SnippetInitializer(self.selenium, self.data_helper)

        if SetEnvConfig().set_browser() != 'android':
            self.window_size()
        self.selenium.get_url(app_url=SetEnvConfig().set_app_url())

    def tearDown(self):
        # Close browser session
        self.selenium.driver.close()
        self.selenium.driver.quit()

    def window_size(self):
        # Sets window frame size for given argument --resolution/-res
        if SetEnvConfig().set_resolution() == 'max' \
                or SetEnvConfig().set_resolution() in SetEnvConfig().set_resolutions_list():
            self.selenium.set_custom_window_size()
        else:
            print('\n--- Given resolution (%s) is not valid ---' % SetEnvConfig().set_resolution())
            print('--- Options: max, 992, 768, 480 ---')
            self.tearDown()
