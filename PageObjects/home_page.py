import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Home_Page:
    """HOME PAGE LOCATORS"""
    _base_page = "http://3.17.211.54:8000/"
    _input_box_xpath = "//input[@id='input']"
    _enter_button_xpath = "//button[@id='enter']"
    _clear_button_xpath = "//button[@id='clear']"
    _display_result_xpath = "//h3/span[@id='result']"

    """Constructor"""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    """navigates to the app page"""
    def go_to_home_page(self):
        self.driver.get(self._base_page)
        print("=====> Navigating to base-page")

    """FizzBuzz calculator function"""
    def fizzBuzz(self,n):
        result = 0
        """
        If number is divisible by both :: Result = FizzBuzz
        Or if divisible by either 3 or 5 :: if by 3 Result = Fizz or Buzz
        Or if not divisible by 3 and 5 :: Result = number      
        """
        if (n % 3 == 0) & (n % 5 ==0):
            result = "FizzBuzz"
        elif (n % 3 == 0) or (n % 5 ==0):
            if (n % 3 == 0):
                result = "Fizz"
            else:
                result = "Buzz"
        else:
            result = n
        return result

    """Provides input to the app and retrieves result from the result area"""
    def get_FizzBuzz_result(self, input):
        # Home page elements
        input_box = self.wait.until(EC.presence_of_element_located((By.XPATH, self._input_box_xpath)))
        enter_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self._enter_button_xpath)))
        clear_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self._clear_button_xpath)))
        display_result = self.wait.until(EC.presence_of_element_located((By.XPATH, self._display_result_xpath)))

        """
        STEPS
        1. Send input in the input box
        2. Click Enter button
        3. Check and record result
        4. Clear the text and result
        """

        #send input into the input box
        input_box.click()
        input_box.send_keys(input)

        # click enter button
        enter_button.click()

        time.sleep(.2)
        # get the result text
        result = display_result.text

        # click clear button to clear
        clear_button.click()

        # return result text to be validated
        return result