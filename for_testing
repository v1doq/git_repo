from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from pod import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from pod import login_in
#from pod import Login
driver = webdriver.Firefox()
def open_site(driver):
    basic_url = "http://127.0.0.1/oxwall"
    #driver = webdriver.Firefox()
    driver.get(basic_url + "/")

open_site(driver)
login_in(user_name="admin", password="passDima_", driver=driver)
'''
driver.find_element(By.CLASS_NAME, "ow_signin_label").click()
driver.find_element(By.NAME, "identity").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("passDima_")
driver.find_element(By.NAME, "submit").click()

time.sleep(5)
'''

members = driver.find_element(By.PARTIAL_LINK_TEXT, "Members")

driver.execute_script("arguments[0].click();", members)
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "Online").click()
'''
action = ActionChains(driver)

admin_menu = driver.find_element(By.PARTIAL_LINK_TEXT, "Admin")
#driver.execute_script("argument[0].scrollIntoView();", admin_menu)
#admin_menu.click()
action.move_to_element(admin_menu).pause(5)

subbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign Out")
action.move_to_element(subbutton).click().perform()

'''
