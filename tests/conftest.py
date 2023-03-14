import time

import pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome("C:\\Users\\APRINCE\\PycharmProjects\\pythonProject1\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.magicbricks.com/")
    time.sleep(3)
    request.cls.driver = driver
    yield
    driver.quit()
