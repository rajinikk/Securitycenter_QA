from pages.home.login_page import LoginPage
import unittest
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from pages.analysis.analysis import Analysis
from selenium.webdriver.support import expected_conditions as cond
import time
from ddt import data, unpack, ddt

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class OrgUsers(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.analy = Analysis(self.driver)

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

    # @data({'name': 'MobileQuries'})
    # @unpack
    # def testb_query(self, name):
    #     self.analy.clickanalysis()
    #     self.analy.clickQuesries()
    #     self.analy.addqueries()
    #     time.sleep(3)
    #     self.analy.addmobilename(name=name)
    #     self.analy.type()
    #     self.analy.Mobilefilter()
    #
    # @data({'name': 'EvenetQuries'})
    # @unpack
    # def testc_event(self,name):
    #    time.sleep(3)
    #    self.analy.EventQuery(name=name)


    # def testd_tiket(self):
    #     self.analy.ticket()
#     Values need to implement

    def testd_vulnerabilites(self):
        self.analy.vulnerability()
        WebDriverWait(driver=self.driver, timeout=5)
        self.analy.acceptriskrule()
