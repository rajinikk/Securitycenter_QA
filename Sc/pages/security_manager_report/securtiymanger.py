from base.SeleniumDriver import SeleniumDriver
import os
import time


class Report(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _reportingbanner = '//*[@id="header"]/div/nav[1]/span[5]/a'
    def reportingBanner(self):
        self.elementClick(locator=self._reportingbanner, locatorType='xpath')

    _reprts ='//*[@id="header"]/div/nav[1]/span[5]/ul/li[1]/a'
    def reports(self):
        self.elementClick(locator=self._reprts, locatorType='xpath')
        time.sleep(1)

    _reportadd = '/html/body/div[1]/section/div/header/div[1]/div/div/div[2]/a'
    def addreport(self):
        self.elementClick(locator=self._reportadd,locatorType='xpath')
        time.sleep(2)

    _complianceandconfiguration='//*[@id="reports-content"]/div/div[3]/div/ul/li[1]'
    def complianceandconfiguration(self):
        self.elementClick(locator=self._complianceandconfiguration,locatorType='xpath')
        time.sleep(3)

    _firstcompliancereport = '//*[@id="reports-content"]/div/div[4]/div/ul/li[1]/div[1]'
    def fistcompliancereport(self):
        self.elementClick(locator=self._firstcompliancereport, locatorType='xpath')

    _allsystem = '//*[@id="targets"]/span/span[1]'
    def clickallsytems(self):
        self.elementClick(locator=self._allsystem, locatorType='xpath')

    _ipaddr  ='//*[@id="targets"]/li[3]/a'
    def clickIp(self):
        self.elementClick(locator=self._ipaddr, locatorType='xpath')

    _iprange = '//*[@id="ips-textarea"]'
    def iptextarea(self, iparea):
        self.sendKeys(data=iparea, locator=self._iprange, locatorType='xpath')

    _selectall = '//*[@id="repositories"]/li[1]/i'
    def selectallrepo(self):
        self.elementClick(locator=self._selectall, locatorType='xpath')

    _submit = '//*[@id="form-overlay-submit"]'
    def submitform(self):
        self.elementClick(locator=self._submit, locatorType='xpath')
        time.sleep(3)

    _runnreprt = '//*[@id="reports-content"]/div/div[4]/div/div/div[2]/div/div[8]/div/span[1]/ul/li/a'
    def runreport(self):
        self.elementClick(locator=self._runnreprt, locatorType='xpath')

    _reportresult = '/html/body/div[1]/section/div/header/div[2]/ul/li[2]/a'
    def reportresult(self):
        self.elementClick(locator=self._reportresult, locatorType='xpath')

    _monitoring = '//*[@id="reports-content"]/div/div[3]/div/ul/li[4]'
    def monitoring(self):
        self.elementClick(locator=self._monitoring,locatorType='xpath')
        time.sleep(2)

    _cloud_servciereport = '//*[@id="reports-content"]/div/div[4]/div/ul/li[3]/div[1]/p'
    def cloudreport(self):
        self.elementClick(locator=self._cloud_servciereport, locatorType='xpath')

class Cyberscope(Report):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _Cyberscope = '//*[@id="reports-content"]/div/div[5]/div/div/ul/li[4]'
    def clickcyberscope(self):
        self.elementClick(locator=self._Cyberscope, locatorType='xpath')

    _cyberscopename = '//*[@id="name-input"]'
    def cyberscopename(self, name):
        self.sendKeys(data=name, locator=self._cyberscopename, locatorType='xpath')


class DiscoveryDetection(Report):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver  = driver

    _discovery = '#reports-content > div > div.pane-view.pane-content.add > div > ul > li:nth-child(2)'
    def discovery(self):
        self.elementClick(locator=self._discovery, locatorType='css')

    _patchmanagement = '//*[@id="reports-content"]/div/div[5]/div/ul/li[1]/div[2]/i'
    def patchmanagement(self):
        self.elementClick(locator=self._patchmanagement, locatorType='xpath')

class ReportAttribute(Report):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _repoattri = 'Report Attributes'
    def reportattribute(self):
        self.elementClick(locator=self._repoattri, locatorType='linktext')

    _attributeadd = '/html/body/div[1]/section/div/header/div[1]/div/div/div/a'
    def add_attribute(self):
        self.elementClick(locator=self._attributeadd, locatorType='xpath')

    _reportattrname  = '//*[@id="name-input"]'
    def addname(self,name):
        self.sendKeys(data=name, locator=self._reportattrname,locatorType='xpath')

class CSV(Report):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _addcsvreport = '//*[@id="reports-content"]/div/div[3]/div/div/ul/li[2]'
    def addcsvreport(self):
        self.elementClick(locator=self._addcsvreport,locatorType='xpath')

    







