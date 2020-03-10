import time
import unittest


import pytest
from ddt import ddt

from pages.blackout.blackoutPage import BlackOutWindow
from pages.home.login_page import LoginPage


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class AddBlackOutWindow(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.bw = BlackOutWindow(self.driver)

    def testA_login_sm_user(self):
        self.lp.login("sm", "admin")
        self.lp.verifyLoginSuccessful()
        self.driver.implicitly_wait(10)

    def testB_add_new_blackout_window(self):
        self.bw.click_scan()
        self.bw.click_blackout_windows()
        time.sleep(2)
        self.bw.click_add_blackout_window()
        self.driver.implicitly_wait(15)
        self.bw.send_name(bw_name = "Test Blackout Window")
        self.bw.click_submit()