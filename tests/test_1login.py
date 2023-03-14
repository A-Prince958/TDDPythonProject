import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.login import Login


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_one(self):

        log = Login(self.driver)

        log.click_login_tab()

        log.click_login_button()

        time.sleep(3)

        log.switch_tab()

        log.enter_email()

        log.next_button()

        log.enter_password()

        log.click_2login_button()

        time.sleep(5)

    def test_two(self):

        log = Login(self.driver)

        log.click_login_tab()

        time.sleep(2)

        log.click_login_button()

        time.sleep(2)

        log.switch_tab()

        time.sleep(2)

        log.enter_mobile_number()

        time.sleep(2)

        log.next_button()

        time.sleep(5)

        log.enter_otp()

        time.sleep(4)

        assert (5-2 == 7)

    def test_three(self):

        log = Login(self.driver)

        log.click_login_tab()

        time.sleep(2)

        log.click_login_button()

        time.sleep(2)

        log.switch_tab()

        time.sleep(2)

        log.click_google_logo()

        time.sleep(5)
