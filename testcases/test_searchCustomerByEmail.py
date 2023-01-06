import time

import pytest

from pageObjects.LoginPage import Loginpage
from pageObjects.AddcustomerPage import Addcustomerpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import Searchcustomerpage
import string
import random


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()  # Logger


    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = Addcustomerpage(self.driver)
        self.addcust.clickoncustomermenu()
        time.sleep(5)
        self.addcust.clickoncustomermenuitem()

        self.logger.info("************* searching customer by emailID **********")
        self.searchcust = Searchcustomerpage(self.driver)
        self.searchcust.setEmail("kiyjcycyhjc676008@gmail.com")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
