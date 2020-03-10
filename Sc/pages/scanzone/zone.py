from selenium.webdriver.common.by import By

from base.SeleniumDriver import SeleniumDriver
import time


class Zone(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _Resources = "Resources"
    _Scan_zones = "Scan Zones"
    _add = "//a[@href='#scan_zones/add']"

    def click_resources(self):
        self.elementClick(self._Resources, locatorType="linktext")

    def click_scan_zones(self):
        self.elementClick(self._Scan_zones, locatorType="linktext")

    def add(self):
        self.elementClick(self._add, locatorType="xpath")


class Scandata(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _enter_name = "//input[@id='name-input']"
    _description = "//*[@id='description-textarea']"
    _ranges_text_area = "//textarea[@id='ranges-textarea']"
    _Search = "//input[@class='select-view-search-input']"
    _setUser_name = "//input[@id='name-input']"
    _Click_centos = "//li[@class='item-list-item label-centos_nessus']"
    _Click_windows = "//li[@class='item-list-item label-windows_nessus']"
    # "//*[@id='scanners']/li[3]/a"
    # _Click_windows = "//*[@id='scanners']/li[3]/a"
    _Click_agent_centos = "//*[@id='scanners']/li[3]/a"
    _click_tenable_io  ="//li[@class='item-list-item label-test_tenable_io']"
    # _windowsforboth_element = "_Click_windows"
    _submit = "Submit"

    def enterscanname(self, username):
        time.sleep(2)
        self.sendKeys(username, locator=self._setUser_name, locatorType="xpath")

    def enterdescription(self, descriptionname):
        self.sendKeys(descriptionname, locator=self._description, locatorType='xpath')

    def rangetextarea(self, ranges):
        self.sendKeys(ranges, locator=self._ranges_text_area, locatorType='xpath')

    def searchnessus(self, search):
        time.sleep(2)
        self.sendKeys(search, locator=self._Search, locatorType='xpath')

    def clear(self):
        self.elementClear(locator=self._Search, locatorType='xpath')

    def click_centos_element(self):
        print("values or click centos element")
        time.sleep(0.1)
        self.elementClick(locator=self._Click_centos, locatorType='xpath')
        time.sleep(2)

    def click_windowsforboth_element(self):
        self.elementClick(locator=self._windowsforboth_element, locatorType='xpath')

    def click_windows_element(self):
        time.sleep(0.1)
        self.elementClick(locator=self._Click_windows, locatorType='xpath')
        time.sleep(2)

    def agent_centos_element(self):
        time.sleep(0.1)
        self.elementClick(locator=self._Click_agent_centos, locatorType='xpath')
        time.sleep(2)

    def tenable_io(self):
        self.elementClick(locator=self._click_tenable_io, locatorType='xpath')

    def submit(self):
        self.elementClick(self._submit, locatorType="linktext")
