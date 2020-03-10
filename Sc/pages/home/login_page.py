from base.SeleniumDriver import SeleniumDriver
#import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    #log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//input[@id='username']"
    _email_field = "//input[@id='username']"
    _password_field = "//input[@id='password']"
    _login_button = "//input[contains(@value,'Sign In')]"
    _advanced ="//button[@id='details-button']"
    _proceed_buton="//a[contains(@id,'proceed-link')]"

    def click_proceed_button(self):
        self.elementClick(self._proceed_buton,locatorType="xpath")

    def click_advanced_button(self):
        self.elementClick(self._advanced, locatorType="xpath")


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterUsername(self, email):
        self.sendKeys(email, self._email_field)


    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email, password):
        self.click_advanced_button()
        self.click_proceed_button()
        self.clickLoginLink()
        self.enterUsername(email)
        self.enterPassword(password)
        import time
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.getElement("//a[contains(text(),'Dashboard')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        print("Test")
