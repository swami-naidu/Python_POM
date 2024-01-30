from Base.BaseClass import BaseClass
from Pages.CheckoutPage import Checkout
from Pages.HomePage import Home
from Pages.TopDealsPage import TopDeals


class Objects:
    driver = None
    wait = None
    home = None
    checkout = None
    topdeals = None
    base = BaseClass()

    def initialise_objects(self, driver, wait):
        Objects.home = Home(driver, wait)
        Objects.checkout = Checkout(driver, wait)
        Objects.topdeals = TopDeals(driver, wait)

