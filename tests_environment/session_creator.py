from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities
from tests_environment.set_env_config import SetEnvConfig


class WebDriverSessionCreator:
    def create_session(self):
        if SetEnvConfig().set_browser() == 'chrome':
            return self.__chrome_session()
        elif SetEnvConfig().set_browser() == 'firefox':
            return self.__firefox_session()
        elif SetEnvConfig().set_browser() == 'android':
            return self.__android_session()

    @staticmethod
    def __chrome_session():
        return Remote(command_executor=SetEnvConfig().set_grid_url(),
                      desired_capabilities={"browserName": "chrome",
                                            "version": "",
                                            "platform": "WINDOWS",
                                            "platformName": "Windows",
                                            "javascriptEnabled": True})

    @staticmethod
    def __firefox_session():
        return Remote(command_executor=SetEnvConfig().set_grid_url(),
                      desired_capabilities=DesiredCapabilities.FIREFOX)

    @staticmethod
    def __android_session():
        return Remote(command_executor=SetEnvConfig().set_grid_url(),
                      desired_capabilities={"browserName": "chrome",
                                            "javascriptEnabled": True,
                                            "platformVersion": "6.0",
                                            "platform": "ANDROID",
                                            "platformName": "Android",
                                            "deviceName": "TB3-850F",
                                            "acceptSslCerts": True,
                                            "acceptInsecureCerts": True})
