from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.scanzone.zone import Zone, Scandata
from pages.nessusscaner.nessusscaner import NessusScanner
from pages.Repositories.repos_page import Repos, IpvRepo
from pages.org.org_files import Org
from utilities.ip_file import IP
from pages.configuration.config import ConfigurationPage
import unittest
import pytest
from ddt import data, unpack, ddt
import time
import logging
# from utilities.custom_logger import setup_logging
from random import random


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class ScanZone(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        logging.info("testing this file")
        logging.info("started loggin ")
        self.lp = LoginPage(self.driver)
        self.zone = Zone(self.driver)
        self.scandata = Scandata(self.driver)

    @pytest.mark.run(order=1)
    def testa_method(self):
        self.lp.login("admin", "admin")
        logging.info("Entering data for username and password for login")
        success = self.lp.verifyLoginSuccessful()
        logging.info("Logging is successfull")
        time.sleep(2)
        if success == "Dashboard":
            logging.debug("Login Succesfull if {} is {}".format(success, 'Dashboard'))

    # @data({'first': 'Centos_Nessus', 'second': 'Both window And Centos', 'third': '172.26.18.95'})
    # @pytest.mark.run(order=2)
    # @unpack
    # def testb_add_scanzone_both_WindowsAndNessus(self, first, second, third):
    #     self.zone.click_resources()
    #     time.sleep(2)
    #     self.zone.click_scan_zones()
    #     self.zone.add()
    #     self.scandata.enterscanname(username=first + str(random()))
    #     self.scandata.enterdescription(descriptionname=second)
    #     self.scandata.rangetextarea(ranges=third)
    #     values = ['Centos', 'Windows']
    #     for value in values:
    #
    #         if ('value' == 'Centos'):
    #             self.scandata.searchnessus(value)
    #             self.scandata.click_centos_element()
    #             time.sleep(5)
    #         else:
    #             self.scandata.clear()
    #             self.scandata.searchnessus(value)
    #             self.scandata.click_windowsforboth_element()

    @data({'value': 'Centos', 'first': 'Centos_Nessus', 'second': 'Centos_based_nessus', 'third': '172.26.0.0/24,172.26.48.0/24'},
          {'value': 'Windows', 'first': 'Windows_Nessus', 'second': 'Windows_based_nessus', 'third': '172.26.0.0/24,172.26.48.0/24'},
          {'value': 'agent', 'first': 'agent_centos_nessus', 'second': 'agent capable centos nessus','third': '172.26.0.0/24,172.26.48.0/24'})
    @pytest.mark.run(order=2)
    @unpack
    def testc_add_scanzone(self, value, first, second, third):
        self.zone.click_resources()
        time.sleep(2)
        self.zone.click_scan_zones()
        self.zone.add()
        self.scandata.enterscanname(username=first + str(random()))
        self.scandata.enterdescription(descriptionname=second)
        self.scandata.rangetextarea(ranges=third)
        # value = IP.Scandata.search_Centos
        self.scandata.searchnessus(value)
        time.sleep(5)
        if value == 'Centos':
            print("Entering data in field{}".format(first))
            # self.scandata.searchnessus(search=first)
            self.scandata.click_centos_element()
            self.scandata.submit()
            time.sleep(2)
        elif (value == 'Windows'):
            print("Entering data in field{}".format(first))
            # self.scandata.searchnessus(search=first)
            self.scandata.click_windows_element()
            self.scandata.submit()
            time.sleep(2)

        else:
            print("Entering data in field{}".format(first))
            # self.scandata.searchnessus(search=first)
            self.scandata.agent_centos_element()
            self.scandata.submit()
            time.sleep(2)


    @data({'first': 'Centos_Windows', 'second': 'Both window And Centos', 'third': '172.26.0.0/24,172.26.48.0/24'})
    @pytest.mark.run(order=3)
    @unpack
    def testd_add_scanzone_both_WindowsAndCentos(self, first, second, third):
        self.zone.click_resources()
        time.sleep(2)
        self.zone.click_scan_zones()
        self.zone.add()
        self.scandata.enterscanname(username=first + str(random()))
        self.scandata.enterdescription(descriptionname=second)
        self.scandata.rangetextarea(ranges=third)
        values = ['Centos', 'Windows']
        for value in values:

            if (value == 'Centos'):
                self.scandata.searchnessus(value)
                self.scandata.click_centos_element()
                time.sleep(5)
            else:
                self.scandata.clear()
                self.scandata.searchnessus(value)
                self.scandata.click_windows_element()

        self.scandata.submit()

    @data({'first': 'Test_Tenable_io', 'secound': 'Windows_based_nessus', 'third': '18.236.123.145,34.213.181.16,35.162.215.149'})
    @pytest.mark.run(order=3)
    @unpack
    def testc_methoe(self,first,secound,third):
        self.zone.click_resources()
        time.sleep(2)
        self.zone.click_scan_zones()
        self.zone.add()
        self.scandata.enterscanname(username=first + str(random()))
        self.scandata.enterdescription(descriptionname=secound)
        self.scandata.rangetextarea(ranges=third)
        self.scandata.searchnessus(first)
        self.scandata.tenable_io()
        self.scandata.submit()




        # self.scandata.get_Nessus_text()
#
