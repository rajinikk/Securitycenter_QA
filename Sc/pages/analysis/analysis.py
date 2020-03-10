from selenium.webdriver.common.by import By

from base.SeleniumDriver import SeleniumDriver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Analysis(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickanalysis = '#header > div > nav.main-nav > span:nth-child(3) > a'
    def clickanalysis(self):
        self.elementClick(self._clickanalysis,locatorType='css')

    _queries = '//*[@id="header"]/div/nav[1]/span[3]/ul/li[4]/a'
    def clickQuesries(self):
        self.elementClick(locator=self._queries,locatorType='xpath')

    _addquries = '/html/body/div[1]/section/div/header/div[1]/div/div/div/a'
    def addqueries(self):
        self.elementClick(locator=self._addquries, locatorType='xpath')

    _quriesname = '//*[@id="name-input"]'
    def addmobilename(self, name):
        self.sendKeys(data=name, locator=self._quriesname, locatorType='xpath')

    _queryBuilderType = '//*[@id="analysisType"]/span/span[1]'
    _mobile = '//*[@id="analysisType"]/li[3]/a'
    def type(self):
        self.elementClick(locator=self._queryBuilderType, locatorType='xpath')
        self.elementHover(locator=self._mobile, locatorType='xpath')

    _queryFilter = '//*[@id="dataListControl"]/span/div/a'
    _selectFilter = "//span/span[1][contains(text(),'Select a Filter')]"
    _repo = 'Repositories'
    _testmobilerepo = '//span/div/section/ul/li/a'
    _checkbox = '//*[@id="dataListControl"]/span/div/div[1]/div/div/form/div[4]/div/div[1]/a[1]'
    _submit = '//*[@id="form-overlay-submit"]'
    def Mobilefilter(self):
        self.elementClick(locator=self._queryFilter, locatorType='xpath')
        self.elementClick(locator=self._selectFilter,locatorType='xpath')
        self.scroll()
        self.elementClick(locator=self._repo, locatorType='linktext')
        self.elementClick(locator=self._testmobilerepo, locatorType='xpath')
        self.elementClick(locator=self._checkbox, locatorType='xpath')
        self.elementClick(locator=self._submit, locatorType='xpath')

    _queryBuilderType = '//*[@id="analysisType"]/span/span[1]'
    _event = '//*[@id="analysisType"]/li[2]/a'
    def clickEvent(self):
        self.elementClick(locator=self._queryBuilderType, locatorType='xpath')
        self.elementHover(locator=self._event, locatorType='xpath')


    _lceevents = 'LCEs'

    def EventQuery(self,name):
        Analysis.clickanalysis(self)
        Analysis.clickQuesries(self)
        Analysis.addqueries(self)
        Analysis.addmobilename(self,name=name)
        Analysis.clickEvent(self)
        self.elementClick(locator=self._queryFilter, locatorType='xpath')
        self.elementClick(locator=self._selectFilter, locatorType='xpath')
        self.scroll()
        self.elementHover(locator=self._lceevents,locatorType='linktext')
        self.elementClick(locator=self._testmobilerepo, locatorType='xpath')
        self.elementClick(locator=self._checkbox, locatorType='xpath')
        self.elementClick(locator=self._submit, locatorType='xpath')

    _name = '//*[@id="name-input"]'
    def addti(self):
        self.driver.executeScript("document.querySelector('#name-input').setAttribute('value', 'new value for element')");

    _status= 'Creator'
    _selectticket = 'Ticket'
    _ticket = 'Ticket'
    def ticket(self):
        Analysis.clickanalysis(self)
        Analysis.clickQuesries(self)
        Analysis.addqueries(self)
        self.addti()
        self.elementClick(locator=self._queryBuilderType, locatorType='xpath')
        self.elementClick(locator=self._selectticket, locatorType='linktext')
        self.scroll()
        self.elementClick(locator=self._queryFilter, locatorType='xpath')
        self.elementClick(locator=self._selectFilter, locatorType='xpath')
        time.sleep(2)
        self.elementClick(locator=self._status, locatorType='linktext')
        self.elementClick(locator=self._testmobilerepo, locatorType='xpath')
        self.elementClick(locator=self._checkbox, locatorType='xpath')
        self.elementClick(locator=self._submit, locatorType='xpath')


    #vulnerability
    _vulneriabilty = 'Vulnerabilities'
    def clickvulnerability(self):
        self.elementClick(locator=self._vulneriabilty, locatorType='linktext')
        time.sleep(9)

    _option = '#analysis > header > div > div > div > div > div.dropdown.header-action > a'
    def option(self):
        self.elementClick(locator=self._option, locatorType='css')

    _opentkt = '//*[@id="analysis"]/header/div/div/div/div/div[1]/ul/li[5]/a'
    def opentkt(self):
        self.elementHover(locator=self._opentkt,locatorType='xpath')

    def nametkt(self):
        self.sendKeys(data="AutomationTicket", locator=self._name, locatorType='xpath')

    _assignee = '//*[@id="assignee"]/span/span[1]'
    def selectassignee(self):
        self.elementClick(locator=self._assignee, locatorType='xpath')

    _selectuser = '//*[@id="assignee"]/li/a'
    def selectuser(self):
        self.elementHover(locator=self._selectuser, locatorType='xpath')

    _classfication = '//*[@id="classification"]/span/span[1]'
    def clickselect(self):
        self.elementClick(locator=self._classfication, locatorType='xpath')

    _patch='//*[@id="classification"]/li[3]/a'
    def clickpatch(self):
        self.elementHover(locator=self._patch, locatorType='xpath')


    def vulnerability(self):
        Analysis.clickanalysis(self)
        Analysis.clickvulnerability(self)
        Analysis.option(self)
        Analysis.opentkt(self)
        Analysis.nametkt(self)
        Analysis.selectassignee(self)
        Analysis.selectuser(self)
        Analysis.clickselect(self)
        Analysis.clickpatch(self)
        self.elementClick(locator=self._submit, locatorType='xpath')

    _clickvulnerabilty  = '//*[@id="analysis-content-container"]/div/div[3]/div/div[2]/div[1]/div[2]'
    _accept_risk_rule = '#analysis-content-container > div > div.pane-view.pane-content.pane-main.anchor-right.analysis-report-view > div > div > div > div > div.row.vuln-item-actions > ul > li:nth-child(2) > a'
    _selectRepo = '//*[@id="repository"]/li[1]/i'
    _clearTextField = '//*[@id="ips-textarea"]'
    def acceptriskrule(self):
        time.sleep(12)
        Analysis.clickanalysis(self)
        Analysis.clickvulnerability(self)
        self.elementClick(locator=self._clickvulnerabilty, locatorType='xpath')
        self.elementClick(locator=self._clickvulnerabilty, locatorType='xpath')
        self.elementClick(locator=self._accept_risk_rule, locatorType='css')
        self.elementClick(locator=self._selectRepo, locatorType='xpath')
        self.elementClear(locator=self._clearTextField, locatorType='xpath')
        self.sendKeys(data="172.26.48.0,172.26.0.0",locator=self._clearTextField,locatorType='xpath')






