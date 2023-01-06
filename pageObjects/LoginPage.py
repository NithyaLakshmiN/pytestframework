from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_css = "button[type='submit']"
    link_logout_linktext = "Logout"

    # intializing driver
    def __init__(self, driver):
        self.driver = driver

    # Action method
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
