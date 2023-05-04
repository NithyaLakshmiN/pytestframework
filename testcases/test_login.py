
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen



class Test_Login_001:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    invalidpassword= ReadConfig.getinvalidpassword()
    logger = LogGen.loggen()



    def test_valid_login(self, setup):
        print("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.clickSigninwithemailid()
        self.lp.setUserName(self.username)
        self.lp.clickonNextButton()
        self.lp.setPassword(self.password)
        self.lp.clickSignin()
        actual_title = self.driver.title
        if actual_title == "NovaGuide View":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            print("****Login test passed ****")
            self.lp.clickLogout()
            self.driver.close()
            assert True
        else:
            print("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.lp.clickLogout()
            self.driver.close()
            assert False

    def test_invalid_login(self, setup):
        print("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.clickSigninwithemailid()
        self.lp.setUserName(self.username)
        self.lp.clickonNextButton()
        self.lp.setinvalidPassword(self.invalidpassword)
        self.lp.clickSignin()
        self.lp.validate_invalid_login_msg()
        actual_msg = "The email and password you entered don't match"
        if actual_msg == "The email and password you entered don't match":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalid_login.png")
            print("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            print("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
