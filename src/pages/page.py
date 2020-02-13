from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, NoSuchElementException, TimeoutException
import re
from locators import FirstScenarioLocators, SecondScenarioLocators


class BasePage(object):
    """
        Class, that implement's base page template
    """

    def __init__(self, browser):
        self._browser = browser

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, value):
        self._browser = value

    @property
    def wait(self):
        return WebDriverWait(self.browser, 10)

    @property
    def mouse(self):
        return ActionChains(self.browser)


class HomePage(BasePage):
    """
        Class, that implement's the home page template
    """
    def click_on_the_hidden_block(self):
        """
        Hovers the mouse over the guest-field and clicks on it 
        to make the hidden block visible
        """
        field = self.wait.until(EC.element_to_be_clickable(FirstScenarioLocators.CHILDREN_FIELD))
        hidden_block = self.browser.find_element_by_id(FirstScenarioLocators.HIDDEN_BLOCK)
        while not hidden_block.is_displayed():
            self.mouse.move_to_element(field).click().perform()

    def add_children(self, n):
        """
        Returns the number of created fields after clicking 
        the + button for children input-fields n-times
        """
        children = int(n)
        increment_button = self.browser.find_element_by_xpath(FirstScenarioLocators.INCREMENT_CHILDREN_BUTTON)
        for i in range(children):
            self.browser.implicitly_wait(20)
            increment_button.click()
        self.browser.implicitly_wait(20)
        count_age_inputs = len(self.browser.find_elements_by_xpath(FirstScenarioLocators.CHILDREN_AGE_INPUTS))
        return count_age_inputs


class BookingPage(BasePage):
    """
        Class, that implement's the template of page for booking
    """

    PRICE_PATTERN = re.compile('.+[UAH]+\s[0-9]*[\s,]?[0-9]+$')

    def check_in_calendar_opened(self):
        """
        Checks if check in calendar is opened
        """
        try:
            check_in_calendar = self.wait.until(EC.element_to_be_clickable(SecondScenarioLocators.CHECK_IN_CALENDAR_1))
        except TimeoutException:
            check_in_calendar = self.wait.until(EC.element_to_be_clickable(SecondScenarioLocators.CHECK_IN_CALENDAR_2))
        return check_in_calendar.is_displayed()

    def choose_first_city(self):
        """
        Choose the first city in the main menu and follows the link.
        Returns the tuple of three booleans, that shows if the hotel list is visible,
        check in calendar is opened and booking was not done.
        """
        self.browser.implicitly_wait(5)
        self.browser.execute_script("window.scrollTo(0,350)")
        first_city = self.wait.until(EC.element_to_be_clickable(SecondScenarioLocators.FIRST_CITY_ON_HOMEPAGE))
        fail_click = True
        while fail_click:
            try:
                self.mouse.move_to_element(first_city).click().perform()
            except StaleElementReferenceException:
                fail_click = False
            except WebDriverException:
                fail_click = False

        hotel_list = self.browser.find_element_by_id(SecondScenarioLocators.HOTEL_LIST_BLOCK)
        hotels_visible = hotel_list.is_displayed()
        try:
            self.browser.find_element_by_class_name(SecondScenarioLocators.WHEN_BOOKED_PRICE)
            self.browser.find_element_by_class_name(SecondScenarioLocators.WHEN_BOOKED_MESSAGE)
            not_booked = False
        except NoSuchElementException:
            not_booked = True
        return hotels_visible, self.check_in_calendar_opened(), not_booked

    def book_first_hotel(self):
        """
        Clicks on the Show prices button for the first hotel in list 
        and checks if the check in calendar is opened.
        Books on the 31th of March on one day.
        Clicks the Submit button and checks if each result entry has booking price 
        or banner saying no free places.
        Returns boolean value True if the sequence of operations is successful.
        """
        buttons = self.browser.find_elements_by_class_name(SecondScenarioLocators.HOTELS_BUTTONS)
        buttons[0].click()
        if self.check_in_calendar_opened():
            self.browser.execute_script("window.scrollTo(0,100)")
            self.browser.find_element_by_xpath(SecondScenarioLocators.MARCH_31).click()
            self.browser.find_element_by_xpath(SecondScenarioLocators.CHOOSE_IN_DATE_BUTTON).click()
            hotels = self.browser.find_elements_by_xpath(SecondScenarioLocators.HOTELS_ON_DATE)
            closed_registration1 = self.browser.find_elements_by_xpath(SecondScenarioLocators.REGISTRATION_CLOSED_1)
            closed_registration2 = self.browser.find_elements_by_xpath(SecondScenarioLocators.REGISTRATION_CLOSED_2)
            closed_registration3 = self.browser.find_elements_by_xpath(SecondScenarioLocators.REGISTRATION_CLOSED_3)
            counter = 0
            for hotel in hotels:
                tmp = hotel.text.split('\n')
                for i in tmp:
                    if self.PRICE_PATTERN.match(i):
                        counter += 1
                        break
            return len(hotels) == len(closed_registration1)+len(closed_registration2)+len(closed_registration3)+counter
        return False

