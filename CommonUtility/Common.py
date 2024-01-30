from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class CommonMethods:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def clear_and_set_text(self, locator, text):
        # element = self.driver.find_element(locator)
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click_on_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def select_from_dropdown_by_visible_text(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        (Select(element)).select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, index):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        (Select(element)).select_by_index(index)

    def select_from_dropdown_by_value(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        (Select(element)).select_by_value(text)

    def element_is_enabled(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        result = element.get_attribute("class") != "disabled"
        return result

    def get_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        status = element.text
        print("Text taken from element:", status)
        return status

    def select_checkbox(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        if element.is_selected():
            pass
        else:
            element.click()

    def switch_to_child_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def switch_to_parent_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def get_list_of_webelements(self, common_locator):
        webelements_list = self.driver.find_elements(common_locator[0], common_locator[1])
        print(webelements_list)
        return webelements_list

    def get_text_of_webelements(self, webelement_list):
        text_list = []
        for we in webelement_list:
            text_list.append(we.text)
            print(we.text)
        return text_list
