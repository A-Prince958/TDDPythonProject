import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    def click_login_tab(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[2]/a").click()

    def click_login_button(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[2]/div/div[2]/a").click()

    def switch_tab(self):
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)

    def click_signup_link(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"normalSignupLink\"]").click()

    def select_radio_button(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ubiusertype1\"]").click()

    def enter_name(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ubifname\"]").send_keys("Prince")

    def enter_email(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ubiemail\"]").send_keys("sathishsathish36627@gmail.com")

    def enter_password(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ubipass\"]").send_keys("Prince@63820")

    def enter_mobile_number(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ubimobile1\"]").send_keys("6382605974")

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"signUp\"]/div/div[10]/div/label").click()

    def click_signup(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"signUp\"]/div/div[11]/button").click()







