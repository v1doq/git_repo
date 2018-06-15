from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Firefox


class Login(object):

    def __init__(self):
        self.driver = driver

    def signin(self):
        driver.find_element(By.CLASS_NAME, "ow_signin_label").click()

    def username(self, user_name):
        driver.find_element(By.NAME, "identity").send_keys(user_name)

    def password(self, password):
        driver.find_element(By.NAME, "password").send_keys(password)

    def submit(self):
        driver.find_element(By.NAME, "submit").click()
        time.sleep(1)


class NewsFeed(object):

    def enter_new_feed(self, news_text):
        driver.find_element(By.NAME, "status").send_keys(news_text)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(By.CLASS_NAME, "ow_button")).click()
        # driver.find_element(By.CLASS_NAME, "ow_button").click()

    def enter_like(self):
        driver.find_element(By.CLASS_NAME, "ow_miniic_control ow_cursor_pointer newsfeed_like_btn_cont").click()


class SingOut(object):
    def sing_out_user(self):
        action = ActionChains(driver)
        admin_menu = action.move_to_element(driver.find_element(By.NAME, "admin"))
        admin_menu.move_to_element(driver.find_element(By.NAME, "Sign Out")).click()


def login_in(user_name, password, driver):

    driver.find_element(By.CLASS_NAME, "ow_signin_label").click()
    driver.find_element(By.NAME, "identity").send_keys(user_name)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(1)

