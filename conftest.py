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
def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys('vlada_vasileva1_10@gmail.com')
    driver.find_element(*Locators.PASSWORD).send_keys('123456789')
    driver.find_element(*Locators.ENT_BUTTON).click()
    return driver