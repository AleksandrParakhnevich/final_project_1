import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    box_last_name = "/html/body/main/div/div/div/form/div/div/div[1]/div[1]/div[1]/div[2]/input"
    last_name = "//input[@name='LAST_NAME']"
    sms_checkbox = "/html/body/main/div/div/div/form/div/div/div[2]/div/div/div[2]/label[2]/span[1]/span"
    finish_button = "/html/body/main/div/div/div/form/div/div/div[2]/div/div/div[1]/div[5]/button"

    # Getters

    def get_box_last_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.box_last_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_sms_checkbox(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sms_checkbox)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def click_box_last_name(self):
        self.get_box_last_name().click()
        print("Click box last name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def click_sms_checkbox(self):
        self.get_sms_checkbox().click()
        print("Click sms_checkbox")

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    # Methods
    def input_info(self):
        self.get_current_url()
        time.sleep(1)
        self.click_box_last_name()
        time.sleep(1)
        self.input_last_name("Иванов")
        time.sleep(1)
        self.click_sms_checkbox()
        time.sleep(1)
        self.click_finish_button()
        time.sleep(1)
