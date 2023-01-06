import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_Login_DDT_002:
    baseURL = ReadConfig.getapplicationurl()
    path = ".//Testdata/LoginData.xlsx"
    # username = ReadConfig.getusername()
    # password = ReadConfig.getpassword()
    logger = LogGen.loggen()


    def test_login_ddt(self, setup):
        print("****test login ddt****")
        print("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt1.png")
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt2.png")
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt3.png")
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_ddt4.png")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");