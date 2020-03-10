import time
import unittest

import pytest
from _pytest import logging

from ddt import ddt
from pages.home.login_page import LoginPage
from pages.assurancereport.assurance_report_cards_page import AssuranceReportCards


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class AssurancceReportCard(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.arp = AssuranceReportCards(self.driver)

    def testA_login_sm_user(self):
        self.lp.login("sm", "admin")
        self.lp.verifyLoginSuccessful()
        time.sleep(2)

    def testB_create_new_assurance_report_card(self):
        self.arp.click_dashboard()
        self.arp.click_AssuranceReportCards()
        self.arp.click_addAssuranceReportCardsButton()
        self.arp.click_compliance()
        time.sleep(5)
        self.arp.click_SelectAssuranceReportCardTemplate()
        self.arp.click_Targets()
        self.arp.click_IpsInTargets()
        self.arp.sendIps(ipRange="172.26.48.0")
        self.arp.click_selectAllInRepositories()
        self.arp.click_addCompliance()