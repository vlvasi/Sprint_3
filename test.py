import email
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locators

class TestStellarBurgersRegistration():
    def test_registration_success(self, driver):
        driver.find_element(*Locators.ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys('Влада')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.ENT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*Locators.ACC_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('1234')
        driver.find_element(*Locators.ENT_BUTTON).click()
        driver.find_element(*Locators.INCORECT_PASSWORD_TEXT)
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.INCORECT_PASSWORD_TEXT)).text
        assert reg_text
        driver.quite()

class TestStellarBurgersLogin():
    def test_login_button(selfself, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.ENT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'

    def test_login_with_account_button(selfself, driver):
        driver.find_element(*Locators.ACC_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.ENT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'

    def test_login_with_registertion_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME).send_keys('Влада')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'

    def test_login_with_forgot_password_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*Locators.NAME).send_keys(email)
        driver.find_element(*Locators.RECOVER_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'
        driver.find_element(*Locators.PASSWORD).send_keys('123456789')
        driver.find_element(*Locators.CODE_RECOVER).send_keys('12345')
        driver.find_element(*Locators.SAVE_BUTTON).click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

class TestStellarBurgersAccount():
    def test_account_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.ACC_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quite()

class TestStellarBurgersConstructor():
    def test_constructor_button_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'

    def test_logo_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(*Locators.LOGO_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

class TestStellarBurgersExit():
    def test_exit_button_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(*Locators.EXIT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quite()

class TestStellarBurgersSections():
    def test_change_section_sause(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SAUSE_SECTIONS).click
        section_name = driver.find_element(*Locators.SAUSE_SECTIONS).text()
        assert section_name == 'Соусы'

    def test_change_section_buns(self, driver):
        driver.find_element(*Locators.BUNS_SECTIONS).click()
        section_name = driver.find_element(*Locators.BUNS_SECTIONS).text()
        assert section_name == 'Булки'

    def test_change_section_topping(self, driver):
        driver.find_element(*Locators.TOPPING_SECTIONS).click
        section_name = driver.find_element(*Locators.TOPPING_SECTIONS).text()
        assert section_name == 'Начинки'
        driver.quite()




