import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from base.base_class import Base


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    pay_button = "//button[@id='pay-btn']"

    # Getters

    def get_pay_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.pay_button)))

    # Actions

    def click_pay_button(self):
        self.get_pay_button().click()
        print("Click pay button")

    # Methods
    def payment(self):
        self.get_current_url()
        time.sleep(3)
        self.click_pay_button()
