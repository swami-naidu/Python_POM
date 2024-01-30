from selenium.webdriver.common.by import By

from CommonUtility.Common import CommonMethods


class TopDeals(CommonMethods):
    page_size_dropdown = (By.ID, "page-menu")
    sort_button = (By.XPATH, "//span[text()='Veg/fruit name']/following-sibling::span")
    items_in_top_deals = (By.XPATH, "//tbody/tr/td[1]")

    def select_page_size(self, size):
        self.select_from_dropdown_by_visible_text(self.page_size_dropdown, str(size))

    def click_on_sort_button(self):
        self.click_on_element(self.sort_button)

    def verify_sorted_items(self):
        web_elements_list = self.get_list_of_webelements(self.items_in_top_deals)
        print(web_elements_list)
        sorted_items_list = self.get_text_of_webelements(web_elements_list)
        items_list = sorted_items_list.copy()
        items_list.sort()
        print("Original List:", items_list)
        print("  Sorted List:", sorted_items_list)
        assert items_list == sorted_items_list
