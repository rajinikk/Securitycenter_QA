from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.nessusscaner.nessusscaner import NessusScanner
from pages.Repositories.repos_page import Repos, IpvRepo, Mobile
import unittest
from utilities.ip_file import IP
import pytest
from ddt import ddt, data, unpack
import random
import time
# from utilities.custom_logger import setup_logging
import logging


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class NessusScannerTest(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.rp = Repos(self.driver)
        self.IpvRepo = IpvRepo(self.driver)
        self.nessscanner = NessusScanner(self.driver)
        self.Mobile = Mobile(self.driver)
   
    @pytest.mark.run(order=1)
    def testa_add_logina(self):        
        self.lp.login("admin","admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            logging.info("testing succefull")
        
    

    @data({'first':'Centos_Nessus', 'secound': 'Centos_based_nessus', 'third': '172.26.18.95'},
          {'first': 'Windows_Nessus', 'secound':'Windows_based_nessus', 'third': '172.26.18.198'},
          {'first':'agent_centos_nessus','secound':'agent capable centos nessus', 'third': '172.26.18.96'})
    @unpack
    @pytest.mark.run(order=2)
    def testb_method(self, first, secound, third):
        logging.info("first name{} secound name {} third name {}".format(first,secound,third))
        if (first == 'agent_centos_nessus'):
            self.nessscanner.clicking_nessus_components()
            time.sleep(4)
            logging.info("Entering values for agent".format(first))
            self.nessscanner.setnessusname(name= first)
            self.nessscanner.setdescription(description=secound)
            self.nessscanner.sethostip(ip=third)
            self.nessscanner.admin_username(admin=IP.Nessusscannerdata.admin_username)
            self.nessscanner.admin_password(password=IP.Nessusscannerdata.admin_password)
            self.nessscanner.click_agent_toggle()
            self.nessscanner.scroll()
            self.nessscanner.submit()

            self.nessscanner.get_current_url()

        elif (first=='Centos_Nessus' or (first=='Windows_Nessus')):
                test = self.nessscanner.current()
                # self.nessscanner.clickresources()
                # self.nessscanner.clickNessusScanner()
                # self.nessscanner.clickaddbutton()
                self.nessscanner.clicking_nessus_components()
                time.sleep(4)
                self.nessscanner.setnessusname(name=first)
                self.nessscanner.setdescription(description=secound)
                self.nessscanner.sethostip(ip=third)
                self.nessscanner.admin_username(admin=IP.Nessusscannerdata.admin_username)

                self.nessscanner.admin_password(password=IP.Nessusscannerdata.admin_password)
                self.nessscanner.submit()
                time.sleep(5)
        else:
            logging.info("Entered Nessus Name is not of type {0} {1} {2}".format('centos','windows','agentcapable'))

    @data({'first': 'Test_Tenable_io', 'secound': 'cloud.tenable.com', 'third': '443'})
    @unpack
    def testc_method(self,first, secound, third):
        logging.info("first name{} secound name {} third name {}".format(first, secound, third))
        if (first == 'Test_Tenable_io'):
            self.nessscanner.clicking_nessus_components()
            time.sleep(4)
            logging.info("Entering values for agent".format(first))
            self.nessscanner.setnessusname(name=first)
            self.nessscanner.sethostip(ip=secound)
            self.nessscanner.setport(port=third)
            self.nessscanner.admin_username(admin=IP.TenableIo.admin_username)
            self.nessscanner.admin_password(password=IP.TenableIo.admin_password)
            self.nessscanner.scroll()
            self.nessscanner.submit()


