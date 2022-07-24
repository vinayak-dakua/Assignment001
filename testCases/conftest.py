import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption( "--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        # driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "ff":
        service_obj = Service("C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        # driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "ie":
        service_obj = Service("C:\\IEDriverServer.exe")
        driver = webdriver.Ie(service=service_obj)
        # driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")

    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
