from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import Repos, IpvRepo, Mobile
import unittest
from pages.org.org_files import Org
from utilities.ip_file import IP
import pytest
import time
from ddt import ddt, data, unpack

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class AddOrg(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.Org = Org(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing succefull")

    @data({'first': 'Selectable Zones','agent':'agent_centos_nessus'})
    @unpack
    def testb_add_org(self, first, agent):
        self.Org.org()
        self.Org.add_Org()
        time.sleep(2)
        self.Org.enter_username(IP.OrganName.Org1_username)
        self.Org.enter_description(IP.OrganName.Org1)
        time.sleep(1)
        self.Org.dropDown()
        self.Org.click_drop_down(name=first)
        self.Org.click_automatic_ditribution()
        self.Org.select_zones()
        self.Org.select_repos()
        self.Org.select_lce()
        self.Org.select_agent_capable(agent_name=agent)
        self.Org.select_ldaprepo()


        self.Org.Submit()
        self.Org.popup()

