from base.SeleniumDriver import SeleniumDriver
import os
import time


class scanning(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickscanning = "//*[@id='header']/div/nav[1]/span[6]/a"

    def click_scanning_icon(self):
        self.elementClick(self._clickscanning, locatorType="xpath")



class credentials(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickDropDownScanning = "//a[@href='#credentials']"
    _scanningAdd = "//a[@href='#credentials/add']"
    _sshpassword = "//*[@id='credentials-content']/div[1]/div[3]/div/div[3]/ul/li[6]/h5"
    _windowspassword ="//*[@id='credentials-content']/div[1]/div[3]/div/div[4]/ul/li[7]/h5"
    _name = "//input[@id='name-input']"
    _description = "//textarea[@id='description-textarea']"
    _ssh_username = "//input[@id='username-input']"
    _ssh_password = "//input[@id='password-input']"
    _windows_username = "//input[@id='username-input']"
    _windows_password = "//input[@id='password-input']"
    _submit = "//a[@id='form-overlay-submit']"

    def click_drop_down_scanning(self):
        self.elementClick(self._clickDropDownScanning, locatorType="xpath")

    def scanning_add_method(self):
        self.elementClick(self._scanningAdd, locatorType="xpath")

    def ssh_password(self):
        self.elementClick(self._sshpassword, locatorType="xpath")

    def enter_ssh_password_name(self, name):
        self.sendKeys(name, locator=self._name, locatorType="xpath")

    def enter_ssh_password_description(self, description):
        self.sendKeys(description, locator=self._description, locatorType="xpath")

    def enter_ssh_password_username(self, username):
        self.sendKeys(username, self._ssh_username, locatorType="xpath")

    def enter_ssh_password_password(self, password):
        self.sendKeys(password, self._ssh_password, locatorType="xpath")

    def Submit(self):
        self.elementClick(self._submit, locatorType="xpath")

    def windows_password(self):
            userName = self.driver.find_element_by_xpath(self._windowspassword)
            self.driver.execute_script("arguments[0].click();", userName)
            # self.elementClick(self._windowspassword,locatorType="xpath")

    def enter_windows_password_name(self, name):
                self.sendKeys(name, locator=self._name, locatorType="xpath")

    def enter_windows_password_description(self, description):
                self.sendKeys(description, locator=self._description, locatorType="xpath")

    def enter_windows_password_username(self,username):
                self.sendKeys(username,self._windows_username, locatorType="xpath")

    def enter_windows_password_password(self,password):
                self.sendKeys(password,self._windows_password, locatorType="xpath")

class AuditFiles(credentials):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _audit_files = '//a[contains(text(),"Audit Files")]'
    _add_audit = '//a[@class="btn btn-primary add"]'
    _add_advanced_audit = "//li[@class='btn btn-large' and @data-context='custom' ]//parent::ul[@class='tile-list']"
    _name_field = "//input[@id='name-input']"
    _description_field = "//*[@id='description-textarea']"
    _auditfile_upload_field = "//div[@id='fileUpload']/parent::span[@class='form-item-element']"
    _audit_upload = "//span[@class='form-item-element']/descendant::div[@id='fileUpload']/descendant::span[@class='btn dummy-button']"
    #Unix_Audit_file
    _unixauditfile = '#audit_files-content > div > div.pane-view.pane-content.add > div > ul > li:nth-child(25)'
    _search_command =  'body > div.application.module-tabbed-navigation > section > div > header > div > div > div > div:nth-child(2) > input'
    _centos6server = '#audit_files-content > div > div.pane-view.pane-content.selectTemplate > div > ul:nth-child(2) > li:nth-child(1) > div.template-item-content-wrapper'
    _centosname = '#name-input'
    _centosdescription = '#description-textarea'
    #Windows_Audit_file
    _clickwindows = '#audit_files-content > div > div > div > ul > li:nth-child(29)'

    def click_audit(self):
        self.elementClick(self._audit_files, locatorType="xpath")

    def click_add_audit(self):
        self.elementClick(self._add_audit, locatorType="xpath")

    def addunixtemplate(self):
        self.elementClick(self._unixauditfile, locatorType='css')

    def addWindowstemaplate(self):
        self.elementClick(self._clickwindows, locatorType='css')

    def search(self,data):
        self.sendKeysEnter(data=data,locator=self._search_command, locatorType='css')



    def clickcentos6(self):
        self.elementClick(locator=self._centos6server, locatorType='css')

    def clickwindows(self):
        self.elementClick(locator=self._clickwindows, locatorType='css')

    def entername(self,data):
        self.sendKeys(data=data, locator=self._centosname, locatorType='css')

    def description(self,description):
        self.sendKeys(data=description, locator=self._centosdescription, locatorType='css')

    def click_add_advanced(self):
        self.elementClick(locator=self._add_advanced_audit, locatorType="xpath")

    def click_audit_name(self,set_name):
        self.sendKeys(set_name, locator=self._name_field, locatorType="xpath")

    def click_audit_description(self,setdescription):
        self.sendKeys(setdescription, locator=self._description_field, locatorType= "xpath")

    def click_upload_file(self):
        self.upload_file()

    def Unix(self):
        self.addunixtemplate()
        self.search(data='Centos')
        time.sleep(2)
        self.clickcentos6()
        self.entername(data='UNIX')
        self.description(description='Unix_Description')
        credentials.Submit(self)

    def Windows(self):
        # self.click_audit()
        # self.click_add_audit()
        self.addWindowstemaplate()
        time.sleep(1)
        self.search(data='Windows')
        self.clickwindows()
        self.entername(data='Windows')
        self.description(description='Windows_Description')
        credentials.Submit(self)




class Policies(credentials):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _policies_fields = "//a[@href='#policies']"
    _add_button = "//a[contains(text(),'Add')]"
    _host_dicvovery="//*[@id='policies-content']/div[1]/div[3]/div/ul[1]/li[1]/h5"
    _basic_network_scan="//*[@id='policies-content']/div[1]/div[3]/div/ul[1]/li[2]/i"
    _defualt = "//*[@id='MODE|advanced']/span/span[1]"
    _reporticon = "//*[@id='policies-content']/div[1]/div[2]/div/div/div[1]/div/ul/li[9]"
    _dnsname = "#reverse_lookup-input"
    _hostping = "#log_live_hosts-input"
    _policyreport = "#policies-content > div.pane-manager-view > div.pane-view.pane-content.form > div > div > div.vertical-tabs-container > div > ul > li:nth-child(3)"
    _policyCompliance= "#policies-content > div.pane-manager-view > div.pane-view.pane-content.addSelection > div > ul:nth-child(2) > li:nth-child(6) > i"
    _configuration_advance = "//*[@id='MODE|advanced']/li[3]/a"
    #Scalp_and_Auditing_policy
    _ScalpAudiitng =  "#policies-content > div.pane-manager-view > div.pane-view.pane-content.addSelection > div > ul:nth-child(2) > li:nth-child(8) > i"
    _scalpReport  = '#policies-content > div.pane-manager-view > div.pane-view.pane-content.form > div > div > div.vertical-tabs-container > div > ul > li:nth-child(3)'
    _Scalpcompliance = '#policies-content > div.pane-manager-view > div.pane-view.pane-content.form > div > div > div.vertical-tabs-container > div > ul > li:nth-child(6)'
    _clickAuditing = '#dataListControl > span > div > a'
    _clickSelectType = "#view6116-type > span > span.icon-caret-down.dropdown-arrow"
    _SelectWindows = '#view1444-type > li > a'
    _Select_Windows_audit_file = '#view1447-value > li > a'
    _selectaudit = '#view1447-value > span > span.dropdown-label'
    _selectWindows_audit = '#view1447-value > li > a'
    _clickBox = '#dataListControl > span > div > div.data-list-elements > div > div > form > div.form-sections > div > div.form-item.inline-form-actions > a.action-ok.dlc-action.icon-check.icon-lg'
    _clickUnixFile = '#view3942-type > li.item-list-item.label-unix > a'





    def click_policies(self):
        self.elementClick(self._policies_fields, locatorType="xpath")

    def click_add(self):
        self.elementClick(self._add_button, locatorType="xpath")

    def enterhostpolicy(self):
        self.elementClick(self._host_dicvovery, locatorType="xpath")

    def enetrbasicnetork(self):
        self.elementClick(self._basic_network_scan, locatorType="xpath")

    def enterHostPolicyName(self, name):
        self.sendKeys(name, locator=credentials._name, locatorType="xpath")

    def enter_hostPolicy_description(self, description):
        self.sendKeys(description, locator=credentials._description, locatorType="xpath")

    def clickadvanceconfiguration(self):
        self.elementClick(locator=self._defualt, locatorType="xpath")
        self.elementHover(locator=self._configuration_advance, locatorType="xpath",)

    def Basicnetworkreport(self):
        self.elementClick(locator=self._reporticon, locatorType="xpath")

    def PolicyNetworkCompliance(self):
        self.elementClick(locator=self._policyreport, locatorType="css")

    def dnsName(self):

        self.elementClick(locator=self._dnsname, locatorType="css")
    def hostping(self):
        self.elementClick(locator=self._hostping, locatorType='css')

    def policyComplianceAuditing(self):
        self.elementClick(locator=self._policyCompliance, locatorType="css")
    ######ScalpReoport
    def scalpAuditPolicy(self):
        self.elementClick(locator=self._ScalpAudiitng, locatorType='css')

    def scalpreport(self):
        self.elementClick(locator=self._scalpReport, locatorType='css')

    def scalpcompliance(self):
        self.elementClick(locator=self._Scalpcompliance, locatorType='css')

    def clickauditfile(self):
        self.elementClick(locator=self._clickAuditing, locatorType='css')

    def clickselectAuditFile(self):
        time.sleep(2)
        # self.elementClick(locator=self._clickSelectType, locatorType='xpath')
        Select = self.driver.find_element_by_css_selector(self._clickSelectType)
        self.driver.execute_script("arguments[0].click();", Select)

    _UnixAuditSelect = "#view6119-value > span > span.dropdown-label"
    def selectUnixAudit(self):
        time.sleep(2)
        Select = self.driver.find_element_by_css_selector(self._UnixAuditSelect)
        self.driver.execute_script("arguments[0].click();", Select)


    _WindowsCss=  "(//h2[@data-id='Compliance']/following::li[@class='item-list-item label-windows'])[2]"
    def selectWindowsAudit(self):
        time.sleep(2)
        Select = self.driver.find_element_by_css_selector(self._WindowsCss)
        self.driver.execute_script("arguments[0].click();", Select)

    def windowsAudit(self):
        self.elementClick(locator=self._selectaudit, locatorType='css')

    def windows_auditfile(self):
        self.elementClick(locator=self._Select_Windows_audit_file, locatorType='css')

    def rightclick(self):
        self.elementClick(locator=self._clickBox, locatorType='css')

    def unix_audit_file(self):
        self.elementHover(locator=self._clickUnixFile, locatorType='css')

    _UnixAuditFile = "#view6116-type > li.item-list-item.label-unix > a.item-list-item-text"
    def Click_UnixAudit(self):
        # self.elementHover(locator=self._UnixAuditFile, locatorType='css')
        Select = self.driver.find_element_by_css_selector(self._UnixAuditFile)
        self.driver.execute_script("arguments[0].click();", Select)


    _SelectUnixValue="//a[contains(text(),'UNIX')]"
    def selectUnixAuditValue(self):
        self.elementClick(locator=self._SelectUnixValue, locatorType='xpath')


    _okay = '#dataListControl > span > div > div.data-list-elements > div > div > form > div.form-sections > div > div.form-item.inline-form-actions > a.action-ok.dlc-action.icon-check.icon-lg'
    def ClickRightBox(self):
        self.elementClick(locator=self._okay, locatorType='css')

    _okayWindows = '//*[@id="dataListControl"]/span/div/div[1]/div[2]/div/form/div[4]/div/div[1]/a[1]'
    def clickRightWindows(self):
        self.elementClick(locatorType=self._okayWindows,locator='css')

    #Windows
    _selectType= "#view6192-type > span > span.dropdown-label"
    def selectWindwos(self):
        time.sleep(1)
        Select = self.driver.find_element_by_css_selector(self._selectType)
        self.driver.execute_script("arguments[0].click();", Select)

    _clickselect = '#view1524-type > span > span.dropdown-label'
    def clickselect(self):
        time.sleep(0.3)
        Select = self.driver.find_element_by_css_selector(self._clickselect)
        self.driver.execute_script("arguments[0].click();", Select)

    _clickWindows = '#view1524-type > li > a'
    def clickwindowsAudit(self):
        time.sleep(0.5)
        Select = self.driver.find_element_by_css_selector(self._clickWindows)
        self.driver.execute_script("arguments[0].click();", Select)

    _clickwindowsvalues = '#view1527-value > span > span.dropdown-label'
    def selectwindowsauditvalues(self):
        time.sleep(0.4)
        Select = self.driver.find_element_by_css_selector(self._clickwindowsvalues)
        self.driver.execute_script("arguments[0].click();", Select)

    _selectwindowsaudit = '#view1527-value > li > a'
    def windowsvalue(self):
        time.sleep(0.3)
        Select = self.driver.find_element_by_css_selector(self._selectwindowsaudit)
        self.driver.execute_script("arguments[0].click();", Select)

    def addHostDiscovery(self,name,description):
        self.click_policies()
        self.click_add()
        self.enterhostpolicy()
        self.enterHostPolicyName(name=name)
        self.enter_hostPolicy_description(description=description)
        credentials.Submit(self)

    def basic_networkscan(self,name, description):
        self.click_policies()
        self.click_add()
        time.sleep(2)

        self.enetrbasicnetork()
        self.enterHostPolicyName(name=name)
        self.enter_hostPolicy_description(description=description)

        self.clickadvanceconfiguration()
        self.Basicnetworkreport()
        time.sleep(4)
        self.dnsName()
        credentials.Submit(self)

    def PolicyCompliance(self,name, description):
        self.click_policies()
        self.click_add()
        self.policyComplianceAuditing()
        self.enterHostPolicyName(name=name)
        self.enter_hostPolicy_description(description=description)
        self.clickadvanceconfiguration()
        self.PolicyNetworkCompliance()
        self.dnsName()
        self.hostping()
        credentials.Submit(self)

    def scalpandauditing(self,name, description):
        self.click_policies()
        self.click_add()
        self.scalpAuditPolicy()
        self.enterHostPolicyName(name=name)
        self.enter_hostPolicy_description(description=description)
        time.sleep(0.3)
        self.clickadvanceconfiguration()
        self.scalpreport()
        time.sleep(0.3)
        self.dnsName()
        self.scalpcompliance()
        self.clickauditfile()
        self.clickselectAuditFile()
        time.sleep(0.1)
        #Selecting Unix file
        self.Click_UnixAudit()
        # #
        self.selectUnixAudit()
        #Selecting Unix Auditing value
        self.selectUnixAuditValue()
        self.ClickRightBox()
        time.sleep(1.2)
        self.clickauditfile()


    #Windows_file
        self.selectWindwos()
        self.selectWindowsAudit()
        self.clickselect()
        self.clickwindowsAudit()
        self.selectwindowsauditvalues()
        self.windowsvalue()
        self.ClickRightBox()

        #



        










