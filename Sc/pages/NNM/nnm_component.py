from base.SeleniumDriver import SeleniumDriver
from utilities.ip_file import IP

class NNM(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickResource = "Resources"
    _clicknnm = "Nessus Network Monitors"
    _resourceAdd = "//a[@href='#passive_scanners/add']"
    _nnm_name =  "//*[@id='name-input']"
    _description = "//*[@id='description-textarea']"
    _host_text_filed = "//*[@id='ip-input']"
    _nnm_login_nnm = "//*[@id='username-input']"
    _nnm_password = "//*[@id='password-input']"
    _search_keyword = "//*[@id='repositories']/span/div/input"
    _nnm_repo_select = "//*[@id='repositories']/li[1]/a"
    _ipv4_nnm_org = "//*[@id='organization']/span/div/input"
    _submit = "Submit"



    def click_Resource(self):

        self.elementClick(self._clickResource,locatorType="linktext")

    def click_nnm(self):
        self.elementClick(self._clicknnm,locatorType="linktext")

    def resourceAdd(self):
        self.elementClick(self._resourceAdd,locatorType="xpath")

    def entername(self, name):
        self.sendKeys(name, self._nnm_name, locatorType='xpath')

    def enterdescription(self, description):
        self.sendKeys(description, locator=self._description, locatorType='xpath')

    def enteripname(self,ip):
        self.sendKeys(ip,locator=self._host_text_filed,locatorType='xpath')

    def enterusernamennmlogin(self, name):
        self.sendKeys(name, locator=self._nnm_login_nnm, locatorType='xpath')

    def enterpasswordnnmlogin(self, password):
        self.sendKeys(password, self._nnm_password, locatorType='xpath')

    def searchtextfield(self, search_keyword):
        self.sendKeys(search_keyword, self._search_keyword, locatorType='xpath')

    def click_nnm_repo(self):
        self.elementClick(locator=self._nnm_repo_select, locatorType='xpath')

    # def search_org(self, name):
    #     self.sendKeys(data=name, locator=self._ipv4_nnm_org, locatorType='xpath')

    def click_nnm_submit(self):
        self.elementClick(locator=self._submit, locatorType='linktext')





