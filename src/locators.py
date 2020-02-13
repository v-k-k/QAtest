from selenium.webdriver.common.by import By


class FirstScenarioLocators(object):
    """
    Class, that implement's locators for the first scenario
    """
    CHILDREN_FIELD = (By.XPATH, "//*[@id='xp__guests__toggle']")
    HIDDEN_BLOCK = "xp__guests__inputs-container"
    INCREMENT_CHILDREN_BUTTON = "//form/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]"
    CHILDREN_AGE_INPUTS = "//form/div[1]/div[3]/div[2]/div/div/div[4]/select"


class SecondScenarioLocators(object):
    """
    Class, that implement's locators for the second scenario
    """
    FIRST_CITY_ON_HOMEPAGE = (By.CSS_SELECTOR, "div.promotion-postcard__large:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    CHECK_IN_CALENDAR_1 = (By.CSS_SELECTOR, ".c2-calendar")
    CHECK_IN_CALENDAR_2 = (By.CSS_SELECTOR, ".bui-calendar")
    HOTEL_LIST_BLOCK = "hotellist_inner"
    WHEN_BOOKED_MESSAGE = "open_booking--message"
    WHEN_BOOKED_PRICE = "open_booking--message"
    HOTELS_BUTTONS = "bui-button__text"
    MARCH_31 = "//form//table/tbody/tr[6]/td[2]"
    CHOOSE_IN_DATE_BUTTON = "//form/div[5]/div[2]/button"
    HOTELS_ON_DATE = "//*[@data-hotelid]"
    REGISTRATION_CLOSED_1 = "//*[@class='bui-alert bui-u-bleed@small bui-alert--info']"
    REGISTRATION_CLOSED_2 = "//*[@class='fe_banner fe_banner__accessible fe_banner__scale_small fe_banner__w-icon fe_banner__red fe_banner__sr_soldout_property ']"
    REGISTRATION_CLOSED_3 = "//*[@class='bui-alert bui-u-bleed@small bui-alert--inline bui-alert--error bui-spacer--medium']"
