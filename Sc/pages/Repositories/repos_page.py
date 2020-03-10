import time

from base.SeleniumDriver import SeleniumDriver
from utilities.ip_file import IP


class Repos(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _clickRepos = "Repositories"
    _clickDropDownRepo = "//a[@href='#repositories']"
    _repoAdd = "//a[contains(@href,'#repositories/add')]/child::span"
    _ipv4Repo = "//i[@class='icon icon-desktop']/child::span[contains(text(),'v4')]"
    _ipv6Repo = "//i[@class='icon icon-desktop']/child::span[contains(text(),'v6')]"
    _mobile = "//i[@class='icon icon-mobile']"
    _agent = "/html/body/div[1]/section/div/div/div/div/div/div[2]/div/div[1]/ul/li[4]"

    def click_repos_icon(self):
        self.elementClick(self._clickRepos, locatorType="linktext")


    def click_drop_down_repo(self):
        self.elementClick(self._clickDropDownRepo, locatorType="xpath")

    def repo_add_method(self):
        self.elementClick(self._repoAdd, locatorType="xpath")

    def add_ipv4_repo(self):
        self.elementClick(self._ipv4Repo, locatorType="xpath")

    def add_ipv6_repo(self):
        self.elementClick(self._ipv6Repo, locatorType="xpath")

    def add_mobile_repo(self):
        self.elementClick(self._mobile, locatorType="xpath")

    def add_agent_repo(self):
        userName = self.driver.find_element_by_xpath(self._agent)
        self.driver.execute_script("arguments[0].click();", userName)

    def repotest(self):
        self.click_repos_icon()
        import time
        time.sleep(1)
        print("clicking on drowpdown")
        self.click_drop_down_repo()
        print("clicked")
        self.repo_add_method()
        self.add_ipv4_repo()


    def repotestIpv6(self):
        # self.click_repos_icon()
        # import timecli
        # time.sleep(1)
        # print("clicking on drowpdown")
        # self.click_drop_down_repo()
        # print("clicked")
        self.repo_add_method()
        self.add_ipv6_repo()

    def mobile(self):
        # self.click_repos_icon()
        # import time
        # time.sleep(1)
        # print("clicking on drowpdown")
        # self.click_drop_down_repo()
        # print("clicked")
        self.repo_add_method()
        self.add_mobile_repo()

    def agent(self):
        self.click_repos_icon()
        self.click_drop_down_repo()
        self.repo_add_method()
        time.sleep(1)
        self.add_agent_repo()
        print("agent repo added {}".format("first"))

    def tenable_io(self):
        self.repo_add_method()
        self.add_ipv4_repo()







class IpvRepo(Repos):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _name = "//input[@id='name-input']"
    _description = "//textarea[@id='description-textarea']"
    _ip_ranges = "//textarea[@id='ranges-textarea']"
    _Generate_Trend_data = "//input[@id='trendingEnabled-input']"

    _Submit_button = "//a[@id = 'form-overlay-submit']"

    def enter_Username(self, name):
        self.sendKeys(name, locator=self._name, locatorType="xpath")

    def enter_description(self, description):
        self.sendKeys(description, locator=self._description, locatorType="xpath")

    def enter_ip_ranges(self, ipranges):
        self.sendKeys(ipranges, locator=self._ip_ranges, locatorType="xpath")

    def trend_data(self):
        self.scroll()
        self.elementClick(self._Generate_Trend_data, locatorType="xpath")

    def submit(self):
        self.elementClick(self._Submit_button, locatorType="xpath")

    def run(self, name, description, ipv4):
        print("enter value", name)
        print("enter value", description)
        print("enter value", ipv4)
        self.click_repos_icon()
        self.click_drop_down_repo()
        self.repo_add_method()
        self.add_ipv4_repo()
        self.enter_Username(name)

        self.enter_description(description)
        self.enter_ip_ranges(ipv4)
        self.trend_data()
        self.trend_data()
        self.submit()

    def test_nnm_repo(self, name, description, host_ip, ):
        self.run(name,description=description, ipv4=host_ip)



class Mobile(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _name = "//input[@id='name-input']"
    _description = "//textarea[@id='description-textarea']"
    _domain_Controller = "//input[@id='ActiveSyncdomain_controller-input']"
    _domain = "//input[@id='ActiveSyncdomain-input']"
    _domain_username = "//input[@id='ActiveSyncdomain_admin-input']"
    _domain_password = "//input[@id='ActiveSyncpassword-input']"
    _click_scanner = "//*[@id='scanner']/span/span[1]"
    _select_scanner = "Centos_Nessus"
    _click_submit = "Submit"


    def enter_Username(self, name):
        self.sendKeys(name, locator=self._name, locatorType="xpath")

    def enter_description(self, description):
        self.sendKeys(description, locator=self._description, locatorType="xpath")

    def enter_domain_controller(self,domain_controller):
        self.sendKeys(domain_controller,locator=self._domain_Controller,locatorType="xpath")

    def enter_domain(self,domain):
        self.sendKeys(domain,locator=self._domain,locatorType="xpath")

    def enter_domain_username(self,domain_username):
        self.sendKeys(domain_username,locator=self._domain_username,locatorType="xpath")

    def enter_domain_password(self,domain_password):
        self.sendKeys(domain_password,locator=self._domain_password,locatorType="xpath")

    def select_scanner(self,name):


        self.elementClick(self._click_scanner,locatorType="xpath")
        self.elementHover(locator=self._select_scanner, locatorType='linkText', element=name)
        # self.elementClick(self._select_scanner, locatorType="linktext")
        self.elementClick(self._click_submit, locatorType="linktext")

class AgentRepo(Mobile):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _name = "//input[@id='name-input']"
    _description = "//*[@id='description-textarea']"
    # _ip_ranges = "//textarea[@id='ranges-textarea']"
    # _Generate_Trend_data = "//input[@id='trendingEnabled-input']"

    _Submit_button = "//a[@id = 'form-overlay-submit']"

    def enter_Username(self, name):
        self.sendKeys(name, locator=self._name, locatorType="xpath")

    def enter_description(self, description):
        self.sendKeys(description, locator=self._description, locatorType="xpath")

    # def enter_ip_ranges(self, ipranges):
    #     self.sendKeys(ipranges, locator=self._ip_ranges, locatorType="xpath")

    def trend_data(self):
        self.scroll()
        self.elementClick(self._Generate_Trend_data, locatorType="xpath")

    def submit(self):
        self.elementClick(self._Submit_button, locatorType="xpath")













