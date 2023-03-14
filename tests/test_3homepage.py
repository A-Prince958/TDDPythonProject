import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestHomePage:
    def test_five(self):

        hom = HomePage(self.driver)

        hom.click_searchbar()

        hom.click_cross_symbol()

        hom.enter_city()

        time.sleep(2)

        hom.click_suggestion()

        time.sleep(2)

        hom.click_search()

        time.sleep(2)

    def test_six(self):

        hom = HomePage(self.driver)

        hom.click_mb_prime()

        time.sleep(2)

        hom.click_join()

        time.sleep(2)

    def test_seven(self):

        hom = HomePage(self.driver)

        hom.click_help()

        time.sleep(2)

        hom.click_help_center()

        time.sleep(2)

        hom.switch_tab()

        time.sleep(2)

        hom.close_popup()

        time.sleep(2)

        hom.enter_question()

        time.sleep(2)

        hom.pick_suggestion()

        time.sleep(2)

        hom.enter_search()

        time.sleep(2)

    def test_eight(self):

        hom = HomePage(self.driver)

        hom.click_buy()

        time.sleep(2)

        hom.click_rent()

        time.sleep(2)

        hom.click_sell()

        time.sleep(2)

        hom.click_loans()

        time.sleep(2)

        hom.click_properties()

        time.sleep(2)

        hom.click_mb_advice()

        time.sleep(2)

    def test_nine(self):

        hom = HomePage(self.driver)

        hom.scroll_window()

        time.sleep(2)

        hom.click_play_store()

        time.sleep(2)

        hom.switch_window()

        hom.click_apple_store()

        time.sleep(3)

    def test_ten(self):

        hom = HomePage(self.driver)

        hom.scroll_window()

        time.sleep(2)

        hom.click_facebook()

        time.sleep(3)

        hom.switch_window()

        hom.click_twitter()

        time.sleep(3)

        hom.switch_window()

        hom.click_linkedin()

        time.sleep(3)

        hom.switch_window()

        hom.click_youtube()

        time.sleep(3)

        hom.switch_window()

        hom.click_instagram()

        time.sleep(3)