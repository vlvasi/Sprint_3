from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()
class TestStellarBurgers(unittest.TestCase):
    def test_registration_success(self, driver):
        driver.find_element(By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj"]').click()
        driver.find_element(By.NAME, 'name').send_keys('Влада')
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('123456789')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('123456789')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_registration_incorrect_password(self, driver):
        driver.find_element(By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('1234')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        driver.find_element(By.XPATH,'//p[@class="input__error text_type_main-default"]' )
        reg_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//p[@class="input__error text_type_main-default"]'))).text
        assert reg_text
        driver.quite()

    def test_login_button(selfself, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('123456789')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_login_with_account_button(selfself, driver):
        driver.find_element(By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('123456789')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_login_with_registertion_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.NAME, 'name').send_keys('Влада')
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.ID, 'Пароль').send_keys('123456789')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_login_with_forgot_password_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(By.ID, 'Email').send_keys(email)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'
        driver.find_element(By.ID, 'Пароль').send_keys('12345678')
        driver.find_element(By.ID, 'Введите код из письма').send_keys('12345')
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_account_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quite()

    def test_constructor_button_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_logo_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site'
        driver.quite()

    def test_exit_button_tap(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/account/profile')
        driver.find_element(By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quite()

    def test_change_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click
        section_name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"]').text()
        assert section_name == 'Соусы'
        driver.find_element(By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click()
        section_name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"]').text()
        assert section_name == 'Булки'
        driver.find_element(By.XPATH, '//div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]').click
        section_name = driver.find_element(By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10"]').text()
        assert section_name == 'Начинки'
        driver.quite()



