from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def first_scenario(self, n):

        children = int(n)

        if self.gecko.match(self.path):
            browser = webdriver.Firefox(executable_path=self.path)
        else:
            browser = webdriver.Chrome(executable_path=self.path)

        browser.get(self.url)
        wait = WebDriverWait(browser, 40)
        mouse = ActionChains(browser)
        field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="xp__guests__toggle"]')))
        block = browser.find_element_by_id("xp__guests__inputs-container")

        while not block.is_displayed():
            mouse.move_to_element(field).click().perform()

        button = browser.find_element_by_xpath('//form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]')

        for i in range(children):
            browser.implicitly_wait(20)
            button.click()

        browser.implicitly_wait(20)
        count_age_inputs = len(browser.find_elements_by_xpath('//form/div[1]/div[3]/div[2]/div/div/div[4]/select'))
        browser.close()
        return count_age_inputs

    def second_scenario(self):
        pass
