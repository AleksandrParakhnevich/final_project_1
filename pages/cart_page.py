import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    promo = "//input[@id='coupon']"
    coupon = "//input[@id='coupon']"
    apply = "//input[@class='preload_load semibold cart-promo-button']"
    cart_word = "//div[@id='promo_error']"
    order_button = "//button[@id='basketOrderButton2']"

    # Getters

    def get_promo(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.promo)))

    def get_coupon(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.coupon)))

    def get_apply(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.apply)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions

    def click_promo(self):
        self.get_promo().click()
        print("Click promo")

    def input_coupon(self, coupon):
        self.get_coupon().send_keys(coupon)
        print("Input coupon")

    def click_apply(self):
        self.get_apply().click()
        print("Click apply")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods

    def ordering(self):
        self.get_current_url()
        time.sleep(1)
        self.click_promo()
        time.sleep(1)
        self.input_coupon("hard228")
        time.sleep(1)
        self.click_apply()
        time.sleep(1)
        self.assert_cart_word(self.get_cart_word(), "введен некорректный промокод")
        time.sleep(1)
        self.click_order_button()
        time.sleep(1)
