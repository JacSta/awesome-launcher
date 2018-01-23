from selenium.webdriver.common.by import By


class RegisterLocators:
    BTN_signIn = By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    BTN_createAnAccount = By.ID, 'SubmitCreate'
    BTN_register = By.XPATH, '//*[@id="submitAccount"]/span'
    BTN_orderHistoryAndDetails = By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[1]/a/span'

    RADIOBTN_titleGender = By.ID, 'id_gender1'

    INPUT_email = By.ID, 'email_create'
    INPUT_firstName = By.ID, 'customer_firstname'
    INPUT_lastName = By.ID, 'customer_lastname'
    INPUT_emailRegForm = By.ID, 'email'
    INPUT_password = By.ID, 'passwd'
    INPUT_addressFirstName = By.ID, 'firstname'
    INPUT_addressLastName = By.ID, 'lastname'
    INPUT_addressStreet = By.ID, 'address1'
    INPUT_addressCity = By.ID, 'city'
    INPUT_postCode = By.ID, 'postcode'
    INPUT_mobilePhone = By.ID, 'phone_mobile'

    DROPDOWN_day = By.ID, 'days'
    DROPDOWN_month = By.ID, 'months'
    DROPDOWN_year = By.ID, 'years'
    DROPDOWN_selectDay = By.XPATH, '//*[@id="days"]/option[12]'
    DROPDOWN_selectMonth = By.XPATH, '//*[@id="months"]/option[11]'
    DROPDOWN_selectYear = By.XPATH, '//*[@id="years"]/option[33]'
    DROPDOWN_state = By.ID, 'id_state'
    DROPDOWN_stateSelectGeorgia = By.XPATH, '//*[@id="id_state"]/option[12]'
