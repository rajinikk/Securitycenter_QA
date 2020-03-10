from base.SeleniumDriver import SeleniumDriver
import time
from pages.Locator_file import Locator


class LogCorelation(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickresources(self):
        self.elementClick(Locator._Resources, locatorType="linktext")

    def click_lce(self):
        self.elementClick(Locator._lceresource, locatorType="linktext")

    def add_lce_server(self):
        self.elementClick(Locator._lceAddButton,locatorType="xpath")

    def enter_lceusername(self,name):
        self.sendKeys(data=name,locator= Locator._lceusername,locatorType='xpath')

    def enter_lcedescription(self,description):
        self.sendKeys(data=description, locator=Locator._lcedescription, locatorType='xpath')

    def enter_lcehost(self,host):
        self.sendKeys(data=host,locator=Locator._lcehost, locatorType='xpath')

    def clickcheckauthintication(self):
        self.elementClick(locator=Locator._lceauthintication,locatorType='xpath')

    def submit(self):
        self.elementClick(locator=Locator._lcesubmit,locatorType='xpath')

    def click_lce_clients(self):
        self.elementClick(locator=Locator._lceclient_click, locatorType='xpath')
