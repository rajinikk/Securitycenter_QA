from pages.home.login_page import LoginPage
from pages.active_scan.active_scan import ActiveScan
import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
import time
from ddt import data, unpack, ddt

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class ActiveScan(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.active = ActiveScan(self.driver)

    @data({'name': 'test_sm', 'password': 'admin'})
    @pytest.mark.run(order=1)
    @unpack
    def testa_add_logina(self,name,password):
        self.lp.login(email=name, password=password)
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)

        self.wait_page_load()

        if success == "Dashboard":
            print("testing successful")

    def wait_page_load(self):
        WebDriverWait(self.driver, 3)

    @data({'first': 'Centos_Nessus'})
    @unpack
    def testb_active_scan(self,first):
        self.active.click_scan()
        self.active.click_active_scan()
        self.active.clickaddactivescan()
        self.active.EnterScanName(data=first)
        self.active.ClickSelectpolicy()

