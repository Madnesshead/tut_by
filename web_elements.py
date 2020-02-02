from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

__all__ = ["InputField",
           "FramedInputField",
           "SwitchButton",
           "DropDownMenu",
           "Link",
           "ToggleButton",
           "ImageLink",
           "SharedToggleButton",
           "MenuLink"]


class FrameContextWrapper(object):
    def __init__(self, web_element, driver):
        self.driver = driver  # type: WebDriver
        self.web_element = web_element

    def __enter__(self):
        return self.web_element

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.switch_to.default_content()


class WebElementBase(object):
    def __init__(self, locator, locator_type=By.CSS_SELECTOR, wait_timeout=10,
                 search_condition=ec.visibility_of_element_located):
        self._search_condition = search_condition
        self._wait_timeout = wait_timeout
        self._locator_type = locator_type
        self._locator = locator

    def __get__(self, instance, owner):
        return WebDriverWait(instance.driver, 6).until(
            self._search_condition((self._locator_type, self._locator)))  # type: WebElement


class InputField(WebElementBase):
    pass


class SwitchButton(WebElementBase):
    pass


class DropDownMenu(WebElementBase):
    pass


class Link(WebElementBase):
    pass


class ToggleButton(WebElementBase):
    pass


class ImageLink(WebElementBase):
    pass


class FramedInputField(InputField):
    def __init__(self, locator, frame_to_switch=None, locator_type=By.ID, wait_timeout=10,
                 search_condition=ec.visibility_of_element_located):
        super(FramedInputField, self).__init__(locator, locator_type, wait_timeout, search_condition)
        self.frame_to_switch = frame_to_switch

    def __get__(self, instance, owner):
        # switch to frame here
        return FrameContextWrapper(super(FramedInputField, self).__get__(instance, owner), instance.driver)


class SharedToggleButton(ToggleButton):
    def __get__(self, instance, owner):
        instance.share_link.click()
        return super(ToggleButton, self).__get__(instance, owner)


class MenuLink(Link):
    def __init__(self, menu_name, locator, locator_type=By.CSS_SELECTOR, wait_timeout=10,
                 search_condition=ec.visibility_of_element_located):
        self.menu_name = menu_name
        super(Link, self).__init__(locator, locator_type, wait_timeout, search_condition)

    def __get__(self, instance, owner):
        ActionChains(instance.driver).move_to_element(getattr(instance, self.menu_name)).perform()
        return super(Link, self).__get__(instance, owner)
