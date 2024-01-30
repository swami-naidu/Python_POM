import time

from Base.ObjectManager import Objects
from Base.conftest import *


def test_placeorder(greenkart_setup):
    # obj = Objects()
    # Objects.driver = obj.base.open_browser(browser_name="edge")
    # Objects.wait = obj.base.open_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    # obj.initialise_objects(Objects.driver, Objects.wait)

    Objects.home.search_item("Water Melon")
    # time.sleep(1)
    Objects.home.increment_item_for("Water Melon", 3)
    # time.sleep(1)
    Objects.home.click_on_add_to_cart("Water Melon")
    # time.sleep(1)

    Objects.home.search_item("Beetroot")
    # time.sleep(1)
    Objects.home.increment_item_for("Beetroot", 1)
    # time.sleep(1)
    Objects.home.click_on_add_to_cart("Beetroot")
    # time.sleep(1)

    Objects.home.click_on_cart()
    # time.sleep(1)
    Objects.home.goto_checkout()
    # time.sleep(1)

    Objects.checkout.enter_promo_code("rahulshettyacademy")
    # time.sleep(1)
    Objects.checkout.apply_promo_code()
    # time.sleep(1)
    Objects.checkout.verify_promo_code_applied()
    # time.sleep(1)
    Objects.checkout.place_order()
    # time.sleep(1)
    Objects.checkout.choose_country("India")
    # time.sleep(1)
    Objects.checkout.accept_t_and_c()
    # time.sleep(1)
    Objects.checkout.proceed_with_order()
    Objects.checkout.verify_success_message()
    # time.sleep(5)


def test_sorting_top_deals(greenkart_setup):
    # obj = Objects()
    # Objects.driver = obj.base.open_browser("chrome")
    # Objects.wait = obj.base.open_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    # obj.initialise_objects(Objects.driver, Objects.wait)

    Objects.home.click_on_top_deals()
    # time.sleep(1)
    Objects.topdeals.select_page_size(20)
    # time.sleep(1)
    Objects.topdeals.click_on_sort_button()
    # time.sleep(1)
    Objects.topdeals.verify_sorted_items()
    # time.sleep(1)

    Objects.home.click_on_cart_in_previous_window()
    # time.sleep(3)


