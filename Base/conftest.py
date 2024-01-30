import pytest

from Base.ObjectManager import Objects


@pytest.fixture()
def greenkart_setup():
    obj = Objects()
    Objects.driver = obj.base.open_browser(browser_name="edge")
    Objects.wait = obj.base.open_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    obj.initialise_objects(Objects.driver, Objects.wait)


@pytest.fixture(scope="class")
def greenkart_class_setup():
    obj = Objects()
    Objects.driver = obj.base.open_browser(browser_name="edge")
    Objects.wait = obj.base.open_url("https://rahulshettyacademy.com/seleniumPractise/#/")
    obj.initialise_objects(Objects.driver, Objects.wait)
