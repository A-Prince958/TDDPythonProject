import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_searchbar(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"keyword_autoSuggestSelectedDiv\"]/div/div[1]").click()

    def click_cross_symbol(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"keyword_autoSuggestSelectedDiv\"]/div/div[2]").click()

    def enter_city(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/section/section/div/div[1]/div[3]/div[1]/div[1]/input").send_keys(
            "Chennai")

    def click_suggestion(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"serachSuggest\"]/div[2]/span").click()

    def click_search(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"searchFormHolderSection\"]/section/div/div[1]/div[3]/div[4]").click()

    def click_mb_prime(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[1]/a").click()

    def click_join(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[1]/div/div[2]/div[1]/div/div[2]/a").click()

    def click_help(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[7]/a").click()

    def click_help_center(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[7]/div/div/div/ul/li[1]/a").click()

    def switch_tab(self):
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)

    def close_popup(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"userPersonaPopupCloseAnchor\"]").click()

    def enter_question(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"searchContentInput\"]").send_keys("How to change my mobile number?")

    def pick_suggestion(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"ui-id-2\"]").click()

    def enter_search(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"doSearchButton\"]").click()

    def click_buy(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"buyheading\"]").click()

    def click_rent(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]").click()

    def click_sell(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[3]/a").click()

    def click_loans(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[4]/a").click()

    def click_properties(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[5]/a").click()

    def click_mb_advice(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[6]/a").click()

    def scroll_window(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_play_store(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[1]/a").click()

    def switch_window(self):
        p = self.driver.window_handles[-1]
        self.driver.switch_to.window(p)
        self.driver.close()
        time.sleep(2)
        q = self.driver.window_handles[0]
        self.driver.switch_to.window(q)

    def click_apple_store(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[2]/a").click()

    def click_facebook(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[3]/a").click()

    def click_twitter(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[4]/a").click()

    def click_linkedin(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[5]/a").click()

    def click_youtube(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[6]/a").click()

    def click_instagram(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/footer/section[1]/div/div[1]/ul[2]/li[7]/a").click()








