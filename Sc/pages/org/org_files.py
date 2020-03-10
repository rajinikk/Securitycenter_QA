from base.SeleniumDriver import SeleniumDriver
import time


class Org(SeleniumDriver):

    #log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        print("driver file",driver)
        super().__init__(driver)
        self.driver = driver

    _Organizations = "//a[@href='#organizations']"
    _add_Organizations = "//a[@href='#organizations/add']"
    _NameInput = "//input[@id='name-input']"
    _description_text_area ="//textarea[@id='description-textarea']"
    _drop_down_toggle = "//ul[@id='distributionMethod']/li/a"
    _drop_down ="//*[@id='distributionMethod']/span/div/span[@data-toggle='dropdown']"
    _Selectable_zone = '//*[@id="distributionMethod"]/li[3]/a[contains(text(),"Selectable Zones")]'
    _selectzones = "//*[@id='unforcedZones']/li[1]/a"
    _clickrepos = "//*[@id='repositories']/li[1]"
    _selectrepos = "Select All"
    _agent_repos = "//*[@id='agentScanners']/li/a"
    _lce_server = "//*[@id='assets' and @class='item-list select-view item-list-info select-view-search-enabled']"
    _ldap_repo = "//*[@id='ldapServers']/li/a"
    _automatic_ditribution = '//*[@id="automaticDistribution-input"]'
    _submit = "Submit"
    _yes = "//*[@id='add-org-user-cancel']"

    def org(self):
        self.elementClick(self._Organizations, locatorType="xpath")

    def add_Org(self):
        self.elementClick(self._add_Organizations, locatorType="xpath")

    def enter_username(self, username):
        self.sendKeys(username, locator=self._NameInput, locatorType="xpath")

    def enter_description(self, description):
        self.sendKeys(description, locator=self._description_text_area)

    def dropDown(self):
        print("Click on element on dropdown element")
        time.sleep(2)
        self.elementClick(self._drop_down, locatorType="xpath")

    def click_drop_down(self,name):
        self.elementHover(self._Selectable_zone,locatorType="xpath",element=name)

    def click_automatic_ditribution(self):
        self.elementClick(self._automatic_ditribution, locatorType="xpath")

    def select_zones(self):
        self.elementHover(locator=self._selectzones, locatorType="xpath")

    def select_repos(self):
        self.elementHover(locator=self._clickrepos, locatorType="xpath")
        # self.elementClick(locator=self._selectrepos, locatorType="linkText")

    def select_lce(self):
        self.elementHover(locator=self._lce_server, locatorType='xpath')


    def select_agent_capable(self, agent_name):
        self.elementHover(self._agent_repos, locatorType="xpath",element=agent_name)

    def select_ldaprepo(self):
        self.elementHover(self._ldap_repo, locatorType="xpath")



    def Submit(self):
        self.elementClick(self._submit, locatorType="linktext")
        
    def popup(self):
         self.elementHover(self._yes, locatorType='xpath')

         

