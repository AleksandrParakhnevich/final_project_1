import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.ordering()

    cip = ClientInfoPage(driver)
    cip.input_info()

    pp = PaymentPage(driver)
    pp.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish test")
    time.sleep(10)
    driver.quit()
