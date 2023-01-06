import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Addcustomerpage:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_addnew_css = "a[class='btn btn-primary']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_firstname_xpath = "//input[@id='FirstName']"
    textbox_lastname_xpath = "//input[@id='LastName']"
    textbox_gender_male_xpath = "//input[@id='Gender_Male']"
    textbox_gender_female_xpath = "//input[@id='Gender_Female']"
    textbox_dob_xpath = "//input[@id='DateOfBirth']"
    textbox_company_xpath = "//input[@id='Company']"
    checkbox_istaxexempt_xpath = "//input[@id='IsTaxExempt']"
    listbox_newsletter_xpath = "//div[@role='listbox']//ul[@id ='SelectedNewsletterSubscriptionStoreIds_taglist']"
    listbox_newsletter_yourstorename_xpath = "(//div[@class='k-list-scroller'])//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']//li[contains(text(),'Your store name')]"
    listbox_newsletter_teststore2_xpath = "(//div[@class='k-list-scroller'])//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']//li[contains(text(),'Test store 2')]"
    listbox_customerrole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listbox_customerrole_registered_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']//li[@class='k-button']//span[contains(text(),'Registered')]"
    listbox_customerrole_administrators_xpath = "//li[contains(text(),'Administrators')]"
    listbox_customerrole_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listbox_customerrole_vendors_xpath = "//li[contains(text(),'Vendors')]"
    listbox_customerrole_guests_xpath = "//li[contains(text(),'Guests')]"
    listbox_manageofvendor_xpath = "//*[@id='VendorId']"
    listbox_manageofvendor_vendor1_xpath = "//select[@id='VendorId']//option[contains(text(),'Vendor 1')]"
    listbox_manageofvendor_vendor2_xpath = "//select[@id='VendorId']//option[contains(text(),'Vendor 2')]"
    checkbox_active_xpath = "//input[@id='Active']"
    textbox_admincomment_xpath = "//textarea[@id='AdminComment']"
    button_Save_xpath = "//button[@name='save']"

    # intializing driver
    def __init__(self, driver):
        self.listitem = None
        self.driver = driver

    # Action method
    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickoncustomermenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickaddnewbutton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_addnew_css).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH ,self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH ,self.textbox_password_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH ,self.textbox_firstname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH ,self.textbox_lastname_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH ,self.textbox_dob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH ,self.textbox_company_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH ,self.textbox_admincomment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH ,self.button_Save_xpath).click()
        print("Customer create successfully")

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH ,self.textbox_gender_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH ,self.textbox_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH ,self.textbox_gender_male_xpath).click()

    def setManagerOfVendor(self,value):
        self.driver.find_element(By.XPATH,self.listbox_manageofvendor_xpath).click()
        print("Clicked on Manager of Vendor")
        drp=Select(self.driver.find_element(By.XPATH,self.listbox_manageofvendor_xpath))
        drp.select_by_visible_text(value)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH ,self.listbox_customerrole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH ,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_registered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH ,self.listbox_customerrole_guests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.listbox_newsletter_xpath).click()
        time.sleep(4)
        print("Clicked on New Letter")
        if newsletter == 'Your store name':
            self.listitem = self.driver.find_element(By.XPATH, self.listbox_newsletter_yourstorename_xpath)
        elif newsletter == 'Test store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.listbox_newsletter_teststore2_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def istaxexempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_istaxexempt_xpath).click()

    def active(self):
        self.driver.find_element(By.XPATH, self.checkbox_active_xpath).click()
