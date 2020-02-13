from selenium import webdriver
import unittest
import re
from pages.page import HomePage, BookingPage


class TestTemplate(unittest.TestCase):

    URL = "http://www.booking.com"
    GECKO = re.compile('.+geckodriver\D*')
    PATH = ''

    def setUp(self):
        if self.GECKO.match(self.PATH):
            self.browser = webdriver.Firefox(executable_path=self.PATH)
        else:
            self.browser = webdriver.Chrome(executable_path=self.PATH)
        self.browser.get(self.URL)

    def test_scenario_one(self):
        """
        Implements Scenario 1 according to task 
        """
        home_page = HomePage(self.browser)
        home_page.click_on_the_hidden_block()
        assert home_page.add_children(5) == 5

    def test_scenario_two(self):
        """
        Implements Scenario 2 according to task 
        """
        booking_page = BookingPage(self.browser)
        result = booking_page.choose_first_city()
        for i in result:
            assert i
        assert booking_page.book_first_hotel()

    def tearDown(self):
        self.browser.quit()

