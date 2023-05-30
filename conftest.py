import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site'

@pytest.fixture
    def driver():
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture
def login(drover):
    driver.find_element(By.ID, 'email').send_keys('vlada_vasileva1_10@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('123456789')
    driver.find_element(By.XPATH, '//button[@class="auth-from__button"]').click()
    return driver