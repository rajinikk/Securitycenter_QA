import time

from base.SeleniumDriver import SeleniumDriver
from utilities.ip_file import IP


class ActiveScan(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _scan = "//*[@id='header']/div/nav[1]/span[4]/a"
    _activescan='Active Scans'
    _addactivescan = "//a[@href='#scans/add']/span"
    _username = "//*[@id='name-input']"
    _SelectPolicy = "//*[@id='policy']/span/span[1]"


    def click_scan(self):
        self.elementClick(locator=self._scan, locatorType='xpath')

    def click_active_scan(self):
        self.elementClick(locator=self._activescan, locatorType='linktext')

    def clickaddactivescan(self):
        self.elementClick(locator=self._addactivescan, locatorType='xpath')

    def EnterScanName(self,data):
        self.sendKeys(data=data,locator=self._username, locatorType='xpath')

    def ClickSelectpolicy(self):
        self.elementClick(locator=self._SelectPolicy, locatorType='xpath')
        self.sendKeys()

