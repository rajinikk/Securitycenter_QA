from base.SeleniumDriver import SeleniumDriver


class BlackOutWindow(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _Scans = "Scans"
    _BlackoutWindows = "Blackout Windows"
    _AddBlackOutwindow = "div.header-action a.btn.btn-primary.add"
    _name = "input#name-input"
    _submit = "div.form-actions a#form-overlay-submit"


    def click_scan(self):
        self.elementClick(locator=self._Scans, locatorType='linktext')


    def click_blackout_windows(self):
        self.elementClick(locator=self._BlackoutWindows, locatorType='linktext')


    def click_add_blackout_window(self):
        self.elementClick(locator=self._AddBlackOutwindow, locatorType='css')


    def send_name(self, bw_name):
        self.sendKeys(data = bw_name, locator=self._name, locatorType="css")


    def click_submit(self):
        self.elementClick(locator=self._submit, locatorType="css")
