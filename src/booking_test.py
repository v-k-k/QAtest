from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
import re


class BookingTest:

    """
    Class, that implement's two test scenarios:
        
        1. first_scenario(N) - going to home page http://www.booking.com, 
           opening menu for selecting strangers number and specifying N number of children
           return's the number of created age inputs
        
        2. second_scenario
    """

    gecko = re.compile('.+geckodriver\D*')
    url = "http://www.booking.com"

    def __init__(self, path):
        self._path = path

        if self.gecko.match(self.path):
            self._browser = webdriver.Firefox(executable_path=self.path)
        else:
            self._browser = webdriver.Chrome(executable_path=self.path)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def browser(self):
        return self._browser

    @property
    def wait(self):
        return WebDriverWait(self.browser, 40)

    @property
    def mouse(self):
        return ActionChains(self.browser)

    def first_scenario(self, n):
        children = int(n)
        self.browser.get(self.url)
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="xp__guests__toggle"]')))
        block = self.browser.find_element_by_id("xp__guests__inputs-container")
        while not block.is_displayed():
            self.mouse.move_to_element(field).click().perform()

        button = self.browser.find_element_by_xpath('//form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]')

        for i in range(children):
            self.browser.implicitly_wait(20)
            button.click()

        self.browser.implicitly_wait(20)
        count_age_inputs = len(self.browser.find_elements_by_xpath('//form/div[1]/div[3]/div[2]/div/div/div[4]/select'))
        self.browser.close()
        return count_age_inputs

    def second_scenario(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(60)
        self.browser.execute_script("window.scrollTo(0,350)")
        first_city = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.promotion-postcard__large:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")))
        fail_click = True
        while fail_click:
            try:
                self.mouse.move_to_element(first_city).click().perform()
            except StaleElementReferenceException:
                fail_click = False
            except WebDriverException:
                fail_click = False

        self.browser.implicitly_wait(60)
        check_in_calendar = self.browser.find_element_by_xpath("//form/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]")
        calendar = check_in_calendar.is_displayed()
        hotel_list = self.browser.find_element_by_id("hotellist_inner")
        hotels = hotel_list.is_displayed()
        print(calendar, hotels)
        self.browser.close()