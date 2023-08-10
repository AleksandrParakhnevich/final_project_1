import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.finn-flare.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    auth = "//div[@class='header-user-icon header-user-profile sprite']"
    user_name = "//input[@id='login-input']"
    password = "//input[@id='user-password']"
    login_button = "//button[@class='button color_inverse login-button']"
    main_word = "//span[@class='header_work_schedule_2022__link']"

    # Getters

    def get_auth(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.auth)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_auth(self):
        self.get_auth().click()
        print("Click auth")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_auth()
        self.input_user_name("jin654@yandex.ru")
        self.input_password("52555155")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Скидка 10% при оплате Подели и 5% при оплате онлайн")
        time.sleep(5)
