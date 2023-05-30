from selenium.webdriver.common.by import By

class Locators:
    ACC_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]') #Личный кабинет
    REG_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj"]') #Кнопка Зарегистрироваться
    ENT_BUTTON = (By.ID, 'Войти') #Кнопка Войти
    REGISTRATION_BUTTON = (By.ID, 'Зарегистрироваться') #Кнопка-огурец Зарегистрироваться
    RECOVER_BUTTON = (By.ID, 'Восстановить') #Кнопка Восстановить
    SAVE_BUTTON = (By.ID, 'Сохранить') #Кнопка Сохранить
    INCORECT_PASSWORD_TEXT = (By.XPATH,'//p[@class="input__error text_type_main-default"]') #Текст - "Некорректный пароль"
    CONSTRUCTOR_BUTTON = (By.ID, 'Конструктор') #Кнопка Конструктор
    LOGO_BUTTON =  (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]') #логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') #Кнопка Выход
    SAUSE_SECTIONS = (By.ID, 'Соусы') #Секция Соусы
    BUNS_SECTIONS = (By.ID, 'Булки')  #Секция Булки
    TOPPING_SECTIONS = (By.ID, 'Начинки')  # Секция Начинки
    EMAIL = (By.ID, 'Email') # email
    PASSWORD = (By.ID, 'Пароль') # password
    NAME = (By.NAME, 'name') #name
    CODE_RECOVER = (By.ID, 'Введите код из письма') #Поле Восстановить пароль
