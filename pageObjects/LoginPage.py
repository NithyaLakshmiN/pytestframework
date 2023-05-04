import time
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class Loginpage:
    button_signinwithemail_css = ".firebaseui-idp-password > .firebaseui-idp-text-long"
    textbox_username_css="#ui-sign-in-email-input"
    button_next_css =".firebaseui-id-submit"
    textbox_password_css = "#ui-sign-in-password-input"
    button_signin_css = ".firebaseui-id-submit"
    link_logout_css = "span[class='b-avatar avatar-icon badge-primary rounded-circle'] span[class='b-avatar-text'] span"
    invalid_login_msg_css =".firebaseui-textfield.mdl-textfield.mdl-js-textfield.mdl-textfield--floating-label.is-upgraded.is-dirty.firebaseui-textfield-invalid"

    # intializing driver
    def __init__(self, driver):
        self.driver = driver

    # Action method
    def clickSigninwithemailid(self):
        time.sleep(10)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.button_signinwithemail_css)))
        self.driver.find_element(By.CSS_SELECTOR, self.button_signinwithemail_css).click()
        print("Clicked on signinwithemailid button")

    def setUserName(self, username):
        time.sleep(10)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.textbox_username_css)))
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).send_keys(username)

    def clickonNextButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_next_css).click()

    def setPassword(self, password):
        time.sleep(10)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.textbox_password_css)))
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).send_keys(password)

    def setinvalidPassword(self, invalidassword):
        time.sleep(10)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.textbox_password_css)))
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css).send_keys(invalidassword)

    def clickSignin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_signin_css).click()

    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_logout_css).click()

    def validate_invalid_login_msg(self):
         time.sleep(20)
         actual_msg = self.driver.find_element(By.CSS_SELECTOR, self.invalid_login_msg_css).text
         print(actual_msg)
         return actual_msg
