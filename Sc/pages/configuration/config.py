from base.SeleniumDriver import SeleniumDriver
import time


class ConfigurationPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _click_system = "//*[@id='header']/div/nav[1]/span[7]"
    _click_configuration = "//*[@id='header']/div/nav[1]/span[7]/ul/li[1]/a"
    _click_pluginsorfeed = "//*[@id='configuration-content']/div[1]/div/div/ul/li[7]/i"

    _click_plugins = ["//*[@id='feedUpdate']/div[3]/div[1]/div[1]/div/i[2]",
                      "//*[@id='pluginUpdate']/div[3]/div[1]/div[1]/div/i[2]",
                      "//*[@id='passivePluginUpdate']/div[3]/div[1]/div[1]/div/i[2]",
                      "//*[@id='lcePluginUpdate']/div[3]/div[1]/div[1]/div/i[2]"]
    _click_update = ["//*[@id='feedUpdate']/div[3]/div[1]/div[3]/a",
                     "//*[@id='pluginUpdate']/div[3]/div[1]/div[3]/a",
                     "//*[@id='passivePluginUpdate']/div[3]/div[1]/div[3]/a",
                     "//*[@id='lcePluginUpdate']/div[3]/div[1]/div[3]/a"]
    _click_submit = "Submit"
    _back = "//*[@id='configuration']/header/div/div/div/div/a"

    def click_on_system(self):
        self.elementClick(self._click_system, locatorType="xpath")

    def click_on_configuration(self):
        self.elementClick(self._click_configuration, locatorType="xpath")

    def click_on_pluginsorfeed(self):
        self.elementClick(self._click_pluginsorfeed, locatorType="xpath")

    def click_inside_pluginsorfeed(self):
        for i in range(4):
            self.elementClick(self._click_plugins[i], locatorType="xpath")
            time.sleep(5)
            self.elementClick(self._click_update[i], locatorType="xpath")
            time.sleep(3)
            self.elementClick(self._click_submit, locatorType="linktext")
            time.sleep(3)


