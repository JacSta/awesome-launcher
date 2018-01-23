from selenium.webdriver.common.by import By


class GoogleSiteLocators:
    ELEMENT_logo = By.ID, "hplogo"
    INPUT_search = By.CLASS_NAME, "gsfi"
    BTN_search = By.XPATH, '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
