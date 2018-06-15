from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.sign_in = driver.find_element(By.CLASS_NAME, "ow_signin_label")
        self.sign_up = driver.find_element(By.PARTIAL_LINK_TEXT, "Sing up")
        self.main_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Main")
        self.join_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Join")
        self.members_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Members")
        self.photo_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Photo")
        self.video_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Video")
        self.dashboard_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Dashboard")
        self.messages_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Messages")
        self.notifications_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Notifications")
        self.terms_of_use_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Terms of use")
        self.privacy_policy_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Privacy Policy")
        self.community_software_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Community software")
        self.mobile_version_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Mobile version")


class MembersPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.latest_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Latest")
        self.online_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Online")
        self.search_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Search")


class Photos(object):
    def __init__(self, driver):
        self.driver = driver
        self.explore_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Explore")
        self.my_photos_link = driver.find_element(By.PARTIAL_LINK_TEXT, "My photos")


class Videos(object):
    def __init__(self, driver):
        self.driver = driver
        self.latest_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Latest")
        self.top_rated_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Top Rated")
        self.browse_by_tag_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Browse by Tag")
