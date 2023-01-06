import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Loginpage
from pageObjects.AddcustomerPage import Addcustomerpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()  # Logger


    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = Addcustomerpage(self.driver)
        self.addcust.clickoncustomermenu()
        time.sleep(5)
        self.addcust.clickoncustomermenuitem()

        self.addcust.clickaddnewbutton()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        print(self.email)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        #self.addcust.setNewsletter("Test store 2")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("67657")
        self.addcust.setLastName("76576587878768786")
        self.addcust.setDob("7/05/1990")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.istaxexempt()
        self.addcust.active()
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr_success.png")
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr_failure.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
