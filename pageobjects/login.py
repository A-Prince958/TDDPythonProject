import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:

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

    def enter_email(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"emailOrMobile\"]").send_keys("prince63820@gmail.com")

    def next_button(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"btnStep1\"]").click()

    def enter_password(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys("Prince@63820")

    def click_2login_button(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"btnLogin\"]").click()

    def enter_mobile_number(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"emailOrMobile\"]").send_keys("6382088426")

    def enter_otp(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"verifyOtpDiv\"]/div[2]/div[3]/button").click()

    def click_google_logo(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"my-signin2\"]/div/div").click()



