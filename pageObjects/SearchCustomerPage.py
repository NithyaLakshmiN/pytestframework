import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Searchcustomerpage :
    txtbox_email_xpath = "//*[@id='SearchEmail']"
    textbox_fname_xpath = "//*[@id='SearchFirstName']"
    textbox_lname_xpath = "//*[@id='SearchLastName']"
    button_search_xpath ="//button[@id='search-customers']"
    table_searchresults_xpath ="//div[@class='dataTables_scrollHeadInner']//table[@class='table table-bordered table-hover table-striped dataTable no-footer']"
    table_searchresultrecord_id="//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.textbox_fname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.textbox_lname_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_elements(By.XPATH,self.table_searchresultrecord_id)
            self.emailid = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            print(self.emailid )
            if self.emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_elements(By.XPATH,self.table_searchresultrecord_id)
            self.name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if self.name == Name:
                flag = True
                break
        return flag