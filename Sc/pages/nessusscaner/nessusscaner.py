from selenium.webdriver.common.by import By
from base.SeleniumDriver import SeleniumDriver
from pages.Locator_file import Locator


class NessusScanner(SeleniumDriver):
        
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickresources(self):
        self.elementClick(Locator._Resources, locatorType="linktext")

    def clickNessusScanner(self):
        self.elementClick(Locator._Nessus_scanner, locatorType="linktext")

    def clickaddbutton(self):
        self.elementClick(Locator._add, locatorType='xpath')

    def setnessusname(self, name):
        self.sendKeys(name, Locator._setname, locatorType='xpath')

    def setdescription(self, description):
        self.sendKeys(description, Locator._setDescription, locatorType='xpath')

    def sethostip(self, ip):
        
        self.sendKeys(ip, Locator._setHost, locatorType='xpath')
    
    def setport(self, port):
            self.elementClear(locator=Locator._setport, locatorType='xpath')
            self.sendKeys(port,locator=Locator._setport, locatorType='xpath')

    def admin_username(self, admin):
        self.sendKeys(admin, Locator._setadminusername, locatorType='xpath')

    def admin_password(self, password):
        self.sendKeys(password, Locator._setadminpassword, locatorType='xpath')

    def submit(self):
        self.elementClick(Locator._clickSubmit, locatorType='xpath')   

    def current(self):
        self.get_current_url()

    def click_agent_toggle(self):
        self.elementClick( Locator._agent_toggle_locator , locatorType='xpath')

    def clicking_nessus_components(self):
        self.clickresources()
        self.clickNessusScanner()
        self.clickaddbutton()

        