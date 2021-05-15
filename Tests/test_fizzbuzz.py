from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects import home_page
from Selenium_helper import selenium_helper

"""This class gets and executes tests from the different pages in the page-object-model"""
class selenium_test():
    driver = webdriver.Chrome(executable_path="seleniumDriver/chromedriver")
    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                           ElementNotVisibleException,
                                                                           ElementNotSelectableException])
    """instances of po classes and helper class"""
    sh = selenium_helper.Selenium_Helper(driver)
    HomePage = home_page.Home_Page(driver, wait)

    """Tests"""
    def test_FizzBuzz(self):
        """initiate driver"""
        self.sh.initiate_driver()

        """Navigate to the base page"""
        try:
            self.HomePage.go_to_home_page()
        except TimeoutException:
            print("Page load exception occurred")


        """FIZZ, BUZZ AND FIZZBUZZ TEST"""
        # to test more numbers increase range
        for i in range(30):
            fizz_buzz_validator = self.HomePage.fizzBuzz(i+1)
            fizz_buzz_result = self.HomePage.get_FizzBuzz_result(i+1)

            # individual validation
            if fizz_buzz_result == str(fizz_buzz_validator):
                print(str(fizz_buzz_result) + "  " + str(fizz_buzz_validator) + " PASS")
            else:
                print(str(fizz_buzz_result) + "  " + str(fizz_buzz_validator) + " FAIL")

        """finish tests"""
        self.sh.finish_tests()