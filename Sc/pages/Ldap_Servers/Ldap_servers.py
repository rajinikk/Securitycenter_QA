import time

from base.SeleniumDriver import SeleniumDriver
from utilities.ip_file import IP


class LdapServers(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _Resources = "//a[@class=' dropdown-toggle']"
    _ldap_servers = "//a[@href='#ldap_servers']"
    _add = "//a[@href='#ldap_servers/add']"
    _dropdown =  "//*[@id='encryption']/span"
    _nope_xpath = "//*[@id='encryption']/li[3]"
    _entername = "//input[@id='name-input']"
    _description = "//textarea[@id='description-textarea']"
    _host_name = "//input[@id='host-input']"
    _user_name = "//input[@id='username-input']"
    _password = "//input[@id='password-input']"
    _base_dn = "//input[@id='base-input']"
    _filter = "//input[@id='string-input']"
    _attribute = "//input[@id='usernameAttribute-input']"
    _email_attribute = "//input[@id='emailAttribute-input']"
    _phone_attribute = "//input[@id='phoneAttribute-input']"
    _name_attribute = "//input[@id='nameAttribute-input']"
    _test_setting = "//a[@id='form-overlay-test']"
    _submit = "Submit"



    def ldap_name(self, username):
        time.sleep(2)
        self.sendKeys(username, locator=self._entername, locatorType="xpath")

    def ldap_description(self, description):
        self.sendKeys(description, locator=self._description, locatorType="xpath")

    def click_resources(self):
        self.elementClick(self._Resources, locatorType="xpath")

    def clickdropdown(self):
        self.elementClick(self._dropdown, locatorType="xpath")

    def elementhovering(self,Non):
        self.elementHover(locator=self._nope_xpath,locatorType="xpath",element=Non)

    def click_ldap_servers(self):
        self.elementClick(self._ldap_servers, locatorType="xpath")

    def add(self):
        self.elementClick(self._add, locatorType="xpath")

    def ldap_host_name(self,host_name):
        self.sendKeys(host_name,locator=self._host_name,locatorType="xpath")

    def ldap_user_name(self,username):
        self.sendKeys(username,locator=self._user_name,locatorType="xpath")

    def ldap_password(self,password):
        self.sendKeys(password,locator=self._password, locatorType="xpath")

    def ldap_Base_DN(self,base_dn):
        self.sendKeys(base_dn,locator=self._base_dn, locatorType="xpath")

    def user_object_filter(self,filter):
        self.sendKeys(filter, locator=self._filter, locatorType="xpath")

    def username_attribute(self,attribute):
        self.sendKeys(attribute, locator=self._attribute, locatorType="xpath")

    def email_attribute(self,email_attribute):
        self.sendKeys(email_attribute,locator=self._email_attribute, locatorType="xpath")

    def phone_attribute(self,phone_attribute):
        self.sendKeys(phone_attribute,locator=self._phone_attribute, locatorType="xpath")

    def name_attribute(self,name_attribute):
        self.sendKeys(name_attribute, locator=self._name_attribute, locatorType="xpath")

    def test_setting(self):
        self.elementClick(locator=self._test_setting, locatorType="xpath")

    def submit(self):
        self.elementClick(self._submit, locatorType="linktext")





