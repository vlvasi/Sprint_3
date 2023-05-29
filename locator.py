from selenium.webdriver.common.by import By

class Locators:
    ACC_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]') #Личный кабинет
    REG_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Кнопка регистрации
    ENT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Кнопка Войти
    INCORECT_PASSWORD_TEXT = (By.XPATH,'//p[@class="input__error text_type_main-default"]') #Текст - "Некорректный пароль"
    RESERT_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Кнопка Восстановить
    SAVE_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]') #Кнопка Сохранить
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]') #Кнопка Конструктор
    LOGO_BUTTON =  (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]') #логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') #Кнопка Выход
    BEANS_SECTION = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') #Секция Булки
