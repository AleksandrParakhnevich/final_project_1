import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    mans_button = "/html/body/header/div/div[1]/div/div/div/div/div[2]/div[1]/div/a"
    sweatshirt_button = "/html/body/main/div/div[1]/div[1]/aside/div[2]/div[2]/div[3]/ul/li[5]/a"
    size_button = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[1]"
    checkbox_1 = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]" \
                 "/div[1]/div[2]/div[2]/div/label[3]/div/span"
    color_button = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[2]/div[1]"
    checkbox_2 = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]" \
                 "/div[1]/div[2]/div[2]/div[2]/div/label[5]/div/span[1]"
    season_button = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[4]/div[1]"
    checkbox_3 = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]" \
                 "/div[1]/div[4]/div[2]/div[2]/div/label[4]/div/span"
    show_button = "//button[@id='filter-submit']"
    sort_button = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[6]/div[1]"
    radio_button_1 = "/html/body/main/div/div[1]/div[2]/div[4]/form/div[1]/div[1]/div[6]/div[2]/div[2]/div/label[3]"
    select_product_1 = "/html/body/main/div/div[1]/div[2]/div[7]/div[1]/a/div[1]/div[1]/div[4]"
    select_color_1 = "/html/body/main/div[3]/form/div/div/div/div[2]/div[7]/div/label[3]"
    select_size_1 = "/html/body/main/div[3]/form/div/div/div/div[2]/div[5]"
    select_size_2_xl = "/html/body/main/div[3]/form/div/div/div/div[2]/div[5]/div[4]/div/label[5]"
    add_to_cart_button = "//button[@id='product_tobasket']"
    store_button = "/html/body/main/div[3]/form/div/div/div/div[2]/div[9]/div[4]"
    cart = "//a[@class='header-user-icon header-user-cart sprite header-user-wide']"

    # Getters

    def get_mans_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.mans_button)))

    def get_sweatshirt_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sweatshirt_button)))

    def get_size_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.size_button)))

    def get_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_1)))

    def get_color_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.color_button)))

    def get_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_2)))

    def get_season_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.season_button)))

    def get_checkbox_3(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_3)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sort_button)))

    def get_radio_button_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.radio_button_1)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_color_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_color_1)))

    def get_select_size_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_size_1)))

    def get_select_size_2_xl(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_size_2_xl)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_mans_button(self):
        self.get_mans_button().click()
        print("Click mans button")

    def click_sweatshirt_button(self):
        self.get_sweatshirt_button().click()
        print("Click sweatshirt button")

    def click_size_button(self):
        self.get_size_button().click()
        print("Click size button")

    def click_checkbox_1(self):
        self.get_checkbox_1().click()
        print("Click checkbox 1")

    def click_color_button(self):
        self.get_color_button().click()
        print("Click color button")

    def click_checkbox_2(self):
        self.get_checkbox_2().click()
        print("Click checkbox 2")

    def click_season_button(self):
        self.get_season_button().click()
        print("Click season button")

    def click_checkbox_3(self):
        self.get_checkbox_3().click()
        print("Click checkbox 3")

    def click_show_button(self):
        self.get_show_button().click()
        print("Click show button")

    def click_sort_button(self):
        self.get_sort_button().click()
        print("Click sort button")

    def click_radio_button_1(self):
        self.get_radio_button_1().click()
        print("Click radio button 1")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Select product 1")

    def click_select_color_1(self):
        self.get_select_color_1().click()
        print("Select color 1")

    def click_select_size_1(self):
        self.get_select_size_1().click()
        print("Select size 1")

    def click_select_size_2_xl(self):
        self.get_select_size_2_xl().click()
        print("Select size 2 xl")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click Add to cart button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_product(self):
        self.get_current_url()
        time.sleep(1)
        self.click_mans_button()
        time.sleep(1)
        self.click_sweatshirt_button()
        time.sleep(1)
        self.click_size_button()
        time.sleep(1)
        self.click_checkbox_1()
        time.sleep(1)
        self.click_color_button()
        time.sleep(1)
        self.click_checkbox_2()
        time.sleep(1)
        self.click_season_button()
        time.sleep(1)
        self.click_checkbox_3()
        time.sleep(1)
        self.click_show_button()
        time.sleep(1)
        self.click_sort_button()
        time.sleep(1)
        self.click_radio_button_1()
        time.sleep(1)
        self.click_select_product_1()
        time.sleep(1)
        self.click_select_color_1()
        time.sleep(1)
        self.click_select_size_1()
        time.sleep(1)
        self.click_select_size_2_xl()
        time.sleep(1)
        self.click_add_to_cart_button()
        time.sleep(1)
        self.click_cart()
