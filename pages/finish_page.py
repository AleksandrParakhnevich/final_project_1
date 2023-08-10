import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish_word = "/html/body/div[1]/div/div/form/div[1]/h1"

    # Getters

    def get_finish_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.finish_word)))

    # Actions

    # Methods
    def finish(self):
        self.get_current_url()
        time.sleep(10)
        self.assert_finish_word(self.get_finish_word(), "Введите номер телефона")
        time.sleep(1)
        self.get_screenshot()
