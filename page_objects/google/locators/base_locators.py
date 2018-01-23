class BaseLocators:

    @property
    def google_locators(self):
        from .google_locators import GoogleSiteLocators
        return GoogleSiteLocators
