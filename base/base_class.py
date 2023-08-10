import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method  cart assert word"""

    @staticmethod
    def assert_cart_word(word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method  screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y .%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + ' .png'
        self.driver.save_screenshot('C:\\Users\\jin65\\PycharmProjects\\final_project\\screen\\' + name_screenshot)

    """Method  finish assert word"""

    @staticmethod
    def assert_finish_word(word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")
