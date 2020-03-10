from base.SeleniumDriver import SeleniumDriver


class IndustrialSecurityInstances(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickResource = "Resources"
    _clickIsi = "Industrial Security Instances"
    _isiAdd = "//a[@href='#industrial_scanners/add']"
    _isi_name = "//input[@id='name-input']"
    _isi_description = "//textarea[@id='description-textarea']"
    _host = "//input[@id='ip-input']"
    _isi_username = "//input[@id='username-input']"
    _isi_password = "//input[@id='password-input']"
    _isi_reponame = "//input[@class='select-view-search-input']"
    _clickbox = "//i[@class='toggle-selected  icon-square-o ']"
    _submit = "Submit"



    def click_Resource(self):
        self.elementClick(self._clickResource, locatorType="linktext")

    def clickIsi(self):
        self.elementClick(self._clickIsi, locatorType="linktext")

    def IsiAdd(self):
        self.elementClick(self._isiAdd, locatorType="xpath")

    def isi_name(self,name):
        self.sendKeys(name,self._isi_name,locatorType="xpath")

    def isi_description(self,name):
        self.sendKeys(name,self._isi_description,locatorType="xpath")

    def host(self,name):
        self.sendKeys(name,self._host,locatorType="xpath")

    def isi_username(self,name):
        self.sendKeys(name,self._isi_username,locatorType="xpath")

    def isi_password(self,name):
        self.sendKeys(name,self._isi_password,locatorType="xpath")

    def isi_Repositories(self,repo_name):
        self.sendKeys(repo_name,self._isi_reponame,locatorType="xpath")

    def isi_reposelect(self):
        self.elementClick(self._clickbox,locatorType="xpath")

    def submit(self):
        self.elementClick(self._submit, locatorType="linktext")


