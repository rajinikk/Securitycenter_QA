from base.SeleniumDriver import SeleniumDriver


class AssuranceReportCards(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _dashboard = "Dashboard"
    _AssuranceReportCards = "Assurance Report Cards"
    _addAssuranceReportCardsButton = "a.btn.btn-primary.add"
    _compliance = "li.btn.btn-large i.icon.glyphicons.group"
    _SelectAssuranceReportCardTemplate = "//*[@id='reportCards-content']/div/div[3]/div/ul/li[1]/div[2]"
    _Targets = "div#targets .dropdown.item-list-dropdown"
    _IpsInTargets = "ul#targets li.item-list-item.label-ips"
    _sendIps = "textarea#definedIPs-textarea"
    _selectAllInRepositories = "li.item-list-item.label-selectall i.toggle-selected.icon-square-o"
    _addCompliance = "div.form-actions a#form-overlay-submit"

    def click_dashboard(self):
        self.elementClick(locator=self._dashboard, locatorType='linktext')


    def click_AssuranceReportCards(self):
        self.elementClick(locator=self._AssuranceReportCards, locatorType='linktext')


    def click_addAssuranceReportCardsButton(self):
        self.elementClick(locator=self._addAssuranceReportCardsButton, locatorType='css')


    def click_compliance(self):
        self.elementClick(locator=self._compliance, locatorType='css')


    def click_SelectAssuranceReportCardTemplate(self):
        # self.driver.execute_script("arguments[0].click()", self._SelectAssuranceReportCardTemplate)
        self.elementClick(locator=self._SelectAssuranceReportCardTemplate, locatorType="xpath")


    def click_Targets(self):
        self.elementClick(locator=self._Targets,locatorType="css")


    def click_IpsInTargets(self):
        self.elementClick(locator=self._IpsInTargets, locatorType="css")


    def sendIps(self, ipRange):
        self.sendKeys(data=ipRange, locator=self._sendIps, locatorType="css")


    def click_selectAllInRepositories(self):
        self.elementClick(locator=self._selectAllInRepositories, locatorType="css")


    def click_addCompliance(self):
        self.elementClick(locator=self._addCompliance, locatorType="css")