import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.signup import SignUp


@pytest.mark.usefixtures("setup_and_teardown")
class TestSignUp:
    def test_four(self):

        sig = SignUp(self.driver)

        sig.click_login_tab()

        time.sleep(2)

        sig.click_login_button()

        time.sleep(2)

        sig.switch_tab()

        time.sleep(2)

        sig.click_signup_link()

        time.sleep(2)

        sig.select_radio_button()

        time.sleep(2)

        sig.enter_name()

        time.sleep(2)

        sig.enter_email()

        time.sleep(2)

        sig.enter_password()

        time.sleep(2)

        sig.enter_mobile_number()

        time.sleep(2)

        sig.click_checkbox()

        time.sleep(2)

        sig.click_signup()

        time.sleep(2)
