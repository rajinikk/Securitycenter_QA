import time

from base.SeleniumDriver import SeleniumDriver


class user(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _click_user = "Users"

    def click_user_icon(self):
        self.elementClick(self._click_user, locatorType="linktext")


class users(SeleniumDriver):
    _click_users = "//a[@href='#admin_users']"
    _users_add = "//a[@href='#admin_users/add']"
    _click_add_user = "//a[@href='#admin_users/add']"
    _click_role = "//*[@id='role']/span/span[1]"
    _click_securitymanager = "//li[@class='item-list-item label-securitymanager']"
    _select_org = "//div[@class ='dropdown item-list-dropdown dropdown-search-enabled dropdown-no-selection']"
    _search_org_username = "//*[@id='organization']/span[1]/input"
    _select_org_username = "//*[@id='organization']/li/a"
    _firstname = "//input[@id='firstname-input']"
    _username = "//input[@id='username-input']"
    _password = "//input[@id='password-input']"
    _confirmpassword = "//input[@id='confirmPassword-input']"
    _submit = "Submit"




    def click_users_icon(self):
        self.elementClick(self._click_users, locatorType="xpath")

    def click_add_user(self):
        self.elementClick(self._click_add_user, locatorType="xpath")

    def click_role(self):
        self.elementClick(self._click_role, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._click_securitymanager,locatorType="xpath")

    # def click_securitymanager(self):
    #     self.elementClick(self._click_securitymanager, locatorType="xpath")

    def select_org(self):
        self.elementClick(self._select_org, locatorType="xpath")

    def enter_org_username(self,org_username):
        time.sleep(2)
        print("Valuyes for printing",org_username)
        # self.sendKeys(org_username, self._search_org_username, locatorType="xpath")
        self.elementClick(self._select_org_username, locatorType="xpath")



    def enter_firstname(self,firstname):
        self.sendKeys(firstname,self._firstname,locatorType="xpath")

    def enter_username(self,username):
        self.sendKeys(username,self._username,locatorType="xpath")

    def enter_password(self,password):
        self.sendKeys(password,self._password,locatorType="xpath")

    def enter_confirmpassword(self,confirmpassword):
        self.sendKeys(confirmpassword,self._confirmpassword,locatorType="xpath")

    def Submit(self):
        self.elementClick(self._submit, locatorType="linktext")

class Roles(SeleniumDriver):

    _clickrole = '//*[@id="header"]/div/nav[1]/span[5]/ul/li[2]/a'
    def clickrole(self):
        self.elementClick(locator=self._clickrole, locatorType='xpath')
        time.sleep(0.5)

    _clickadd = 'body > div.application.module-tabbed-navigation > section > div > header > div.header-row > div > div > div > a'
    def clickadd(self):
        self.elementClick(locator=self._clickadd, locatorType='css')

    _entername = '//*[@id="name-input"]'
    def entername(self, name):
        self.sendKeys(data=name, locator=self._entername, locatorType='xpath')

    _clickusername = '//*[@id="createScans-input"]'
    def checkboxcreatescan(self):
        self.elementClick(locator=self._clickusername, locatorType='xpath')

    _managerecastrule = '//*[@id="permManageRecastRiskRules-input"]'
    def MangerecastRule(self):
        self.elementClick(locator=self._managerecastrule, locatorType='xpath')

    _submit = '//*[@id="form-overlay-submit"]'
    def submit(self):
        self.elementClick(self._submit, locatorType='xapth')




