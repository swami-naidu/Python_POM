import time

from selenium.webdriver.common.by import By

from CommonUtility.Common import CommonMethods


class Home(CommonMethods):
    search_box = (By.CLASS_NAME, "search-keyword")
    increment_item_xpath = "//h4[contains(text(),'______')]/following-sibling::div//a[@class='increment']"
    add_to_cart_button_xpath = "//h4[contains(text(),'______')]/following-sibling::div/button[text()='ADD TO CART']"
    cart = (By.XPATH, "//img[@alt='Cart']")
    checkout_button = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    top_deals_link = (By.LINK_TEXT, "Top Deals")

    def search_item(self, item_name):
        self.clear_and_set_text(self.search_box, item_name)

    def increment_item_for(self, item, count):
        time.sleep(1)
        xpath = Home.increment_item_xpath.replace("______", item)
        locator = (By.XPATH, xpath)
        for i in range(1, count):
            time.sleep(1)
            self.click_on_element(locator)

    def click_on_add_to_cart(self, item):
        xpath = Home.add_to_cart_button_xpath.replace("______", item)
        locator = (By.XPATH, xpath)
        self.click_on_element(locator)

    def click_on_cart(self):
        self.click_on_element(self.cart)

    def goto_checkout(self):
        if self.element_is_enabled(self.checkout_button):
            self.click_on_element(self.checkout_button)
        else:
            print("no items were selected")

    def click_on_top_deals(self):
        self.click_on_element(self.top_deals_link)
        self.switch_to_child_window()

    def click_on_cart_in_previous_window(self):
        self.switch_to_parent_window()
        self.click_on_element(self.cart)
