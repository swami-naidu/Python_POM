from selenium.webdriver.common.by import By

from CommonUtility.Common import CommonMethods


class Checkout(CommonMethods):
    promo_code_text_box = (By.XPATH, "//input[@class='promoCode']")
    promo_code_apply_button = (By.XPATH, "//button[@class='promoBtn']")
    promo_code_status = (By.XPATH, "//span[@class='promoInfo']")
    place_order_button = (By.XPATH, "//button[text()='Place Order']")
    choose_country_dropdown = (By.XPATH, "//label[text()='Choose Country']/..//select")
    accept_t_and_c_checkbox = (By.XPATH, "//input[@class='chkAgree']")
    proceed_button = (By.XPATH, "//button[text()='Proceed']")
    success_message = (By.XPATH, "//div[@class='wrapperTwo']/span")

    def enter_promo_code(self, code):
        self.clear_and_set_text(self.promo_code_text_box, code)

    def apply_promo_code(self):
        self.click_on_element(self.promo_code_apply_button)

    def verify_promo_code_applied(self):
        assert "applied" in self.get_text(self.promo_code_status), "Failed to apply Promocode"

    def place_order(self):
        self.click_on_element(self.place_order_button)

    def choose_country(self, country_name):
        self.select_from_dropdown_by_visible_text(self.choose_country_dropdown, country_name)

    def accept_t_and_c(self):
        self.select_checkbox(self.accept_t_and_c_checkbox)

    def proceed_with_order(self):
        self.click_on_element(self.proceed_button)

    def verify_success_message(self):
        message = self.get_text(self.success_message)
        assert "successfully" in message, "order not placed successfully"
