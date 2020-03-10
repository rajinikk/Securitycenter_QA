from pages.home.login_page import LoginPage
from pages.Log_file.log_correlation import LogCorelation
import pytest
import unittest
from ddt import data, unpack, ddt
import time
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Lce(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.lce = LogCorelation(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing succefull")

    @data({'name': 'Lce_server_to_test','description':'Automation for adding lce server','host':'172.26.18.62'})
    @pytest.mark.run(order=3)
    @unpack
    def testb_addlce_server(self, name, description, host):
        self.lce.clickresources()
        self.lce.click_lce()
        self.lce.add_lce_server()
        time.sleep(1)
        self.lce.enter_lceusername(name=name)
        self.lce.enter_lcedescription(description=description)
        self.lce.enter_lcehost(host=host)
        self.lce.clickcheckauthintication()
        self.lce.submit()
        self.lce.click_lce_clients()

