from pages.NNM.nnm_component import NNM
from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import IpvRepo
import unittest
from utilities.ip_file import IP
import pytest
import time
from ddt import unpack, data, ddt

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Nnm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.nnm = NNM(self.driver)
        self.ipv4nmm = IpvRepo(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing succefull")

    @data({'name': 'test_nnm_repo', 'description': 'Adding nnm description', 'ipv4': '172.26.48.0/24 ,172.26.18.0/24'}
          )
    @unpack
    @pytest.mark.run(order=2)
    def testb_add_nnm_repo(self, name, description, ipv4):
        print("values netering in")
        self.ipv4nmm.test_nnm_repo(name=name, description=description, host_ip=ipv4)


    def testc_add_nnm(self):
        self.nnm.click_Resource()
        self.nnm.click_nnm()
        time.sleep(2)
        self.nnm.resourceAdd()
        self.nnm.entername(name=IP.Nnm.setnessusname)
        self.nnm.enterdescription(description=IP.Nnm.setdescription)
        self.nnm.enteripname(ip=IP.Nnm.sethost)
        self.nnm.enterusernamennmlogin(name=IP.Nnm.admin_username)
        self.nnm.enterpasswordnnmlogin(password=IP.Nnm.admin_password)
        self.nnm.searchtextfield(search_keyword="test_nnm_repo")
        self.nnm.click_nnm_repo()
        time.sleep(3)
        # self.nnm.search_org(name=name)
        self.nnm.click_nnm_submit()
#


