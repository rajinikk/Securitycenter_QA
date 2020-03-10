import unittest
from utilities.ip_file import IP
import pytest
from pages.configuration.config import ConfigurationPage
from pages.home.login_page import LoginPage
import time
from ddt import unpack, data, ddt


@pytest.mark.usefixtures("oneTimeSetUp")
class Config(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.con = ConfigurationPage(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing succefull")

    @pytest.mark.run(order=2)
    def testb_method(self):
        self.con.click_on_system()
        self.con.click_on_configuration()
        self.con.click_on_pluginsorfeed()
        time.sleep(2)
        self.con.click_inside_pluginsorfeed()


