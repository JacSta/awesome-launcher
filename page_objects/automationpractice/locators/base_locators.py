class BaseLocators:
    @property
    def register_locators(self):
        from .register_locators import RegisterLocators
        return RegisterLocators
