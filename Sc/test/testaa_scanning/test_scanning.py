from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import IpvRepo
from pages.Scanning.scanning import scanning,credentials,AuditFiles,Policies
import unittest
from utilities.ip_file import IP
import pytest
import time
# from utilities.custom_logger import setup_logging
from ddt import data, unpack, ddt
import os
from random import random

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configfiles', 'U_RedHat_6_V1R10_STIG_SCAP_1-1_Benchmark')
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Test(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.scanning = scanning(self.driver)
        self.credentials = credentials(self.driver)
        self.af = AuditFiles(self.driver)
        self.policy = Policies(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing successful")

    @data({'name': 'linux_machine', 'description': 'Added a linux system', 'username': 'root', 'password': 'LabPass1'})
    @pytest.mark.run(order=2)
    @unpack
    def testb_add_ssh_password(self, name, description, username, password):
        self.scanning.click_scanning_icon()
        self.credentials.click_drop_down_scanning()
        self.credentials.scanning_add_method()
        time.sleep(3)
        self.credentials.ssh_password()
        self.credentials.enter_ssh_password_name(name + str(random()))
        time.sleep(3)
        self.credentials.enter_ssh_password_description(description)
        self.credentials.enter_ssh_password_username(username)
        self.credentials.enter_ssh_password_password(password)
        time.sleep(3)
        self.credentials.Submit()
        time.sleep(3)

    @data({'name': 'windows_machine', 'description': 'Added a windows system', 'username': 'admin', 'password': 'LabPass1'})
    @pytest.mark.run(order=3)
    @unpack
    def testc_add_windows_password(self, name, description, username, password):
        print("Enter and click value")
        time.sleep(1)
        self.scanning.click_scanning_icon()
        self.credentials.click_drop_down_scanning()
        self.credentials.scanning_add_method()
        time.sleep(12)
        self.credentials.windows_password()
        self.credentials.enter_windows_password_name(name=name+str(random))
        self.credentials.enter_windows_password_description(description=description)
        self.credentials.enter_windows_password_username(username=username)
        self.credentials.enter_windows_password_password(password=password)
        self.credentials.Submit()

    @data({'name': 'test_audit', 'description': 'audittt fileeeeeeee'})
    @pytest.mark.run(order=2)
    @unpack
    def testd_scanning_method(self, name, description, ):

        self.scanning.click_scanning_icon()
        time.sleep(2)
        self.af.click_audit()
        time.sleep(2)
        self.af.click_add_audit()
        self.af.Unix()
        print("Added Unix file in tenable sc@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.af.click_add_audit()
        self.af.Windows()
    #
    #     # self.af.click_add_advanced()
    #     #  e.sleep(5)
    @data({'name': 'Host_Name', 'description': 'Host_namme'})
    @pytest.mark.run(order=2)
    @unpack
    def testf_policyadd(self,name, description):
        self.scanning.click_scanning_icon()
        self.policy.addHostDiscovery(name=name, description=description)

    @data({'name': 'Basic_network', 'description': 'Basic_network_scan'})
    @unpack
    def testg_basicnetworkpolicy(self,name, description):
        self.scanning.click_scanning_icon()
        self.policy.basic_networkscan(name=name, description=description)

    @data({'name': 'Basic_network', 'description': 'Basic_network_scan'})
    @unpack
    def testh_policycompliance_auditing(self,name, description):
        self.scanning.click_scanning_icon()
        self.policy.PolicyCompliance(name=name, description=description)

    # @data({'name': 'Saclp_auditing', 'description': 'Basic_network_scan'})
    # @unpack
    # def testi_scalpauiditing(self,name, description):
    #     self.scanning.click_scanning_icon()
    #     self.policy.scalpandauditing(name,description)





