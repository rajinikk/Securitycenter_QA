# from selenium import webdriver
# from base.SeleniumDriver import SeleniumDriver
# from selenium.webdriver.common.by import By
# from pages.home.login_page import LoginPage
# from pages.scanzone.zone import Zone, Scandata
# from pages.nessusscaner.nessusscaner import NessusScanner
# from pages.Repositories.repos_page import Repos, Ipv4Repo
# from pages.org.org_files import Org
# from utilities.ip_file import IP
# from pages.configuration.config import ConfigurationPage
# import unittest
# import pytest
# from ddt import data, unpack, ddt
# import time
#
#
# @ddt
# @pytest.mark.usefixtures("oneTimeSetUp")
# class Login(unittest.TestCase):
#
#     def classSetup(self, oneTimeSetUp):
#
#         self.lp = LoginPage(self.driver)
#         self.rp = Repos(self.driver)
#         self.zone = Zone(self.driver)
#         self.Ipv4Repo = Ipv4Repo(self.driver)
#         self.scandata = Scandata(self.driver)
#         self.Org = Org(self.driver)
#         self.nessscanner = NessusScanner(self.driver)
#         self.con = ConfigurationPage(self.driver)
#
#     @pytest.mark.run(order=1)
#     def test_methoda(self):
#         self.lp.login("admin","admin")
#         success = self.lp.verifyLoginSuccessful()
#         time.sleep(2)
#         if success == "Dashboard":
#             print("testing succefull")
#
#     @pytest.mark.run(order=2)
#     def test_methodb(self):
#         self.zone.click_resources()
#         time.sleep(2)
#         self.zone.click_scan_zones()
#         self.zone.add()
#         self.scandata.enterscanname(IP.Scandata.Name)
#         self.scandata.enterdescription()
#         self.scandata.rangetextarea()
#         self.scandata.searchnessus()
#         self.scandata.submit()
#
#     @data(("Centos_Nessus","Centos_based_nessus",))
#     @unpack
#     @pytest.mark.run(order=3)
#     def test_methodc(self, name, description_nessus,ip_nessus):
#         self.nessscanner.clickresources()
#         self.nessscanner.clickNessusScanner()
#         self.nessscanner.clickaddbutton()
#         time.sleep(1)
#         self.nessscanner.setnessusname(name=name)
#         self.nessscanner.setdescription(description=description_nessus)
#         self.nessscanner.sethostip(ip=ip_nessus)
#         # self.nessscanner.setport(port=IP.Nessusscannerdata.setport)
#         self.nessscanner.admin_username(admin=IP.Nessusscannerdata.admin_username)
#         self.nessscanner.admin_password(password=IP.Nessusscannerdata.admin_password)
#         self.nessscanner.submit()
#         2
#
#     @pytest.mark.run(order=4)
#     def test_methodd(self):
#         self.rp.repotest()
#
#     @pytest.mark.run(order=5)
#     def test_methode(self):
#         self.Ipv4Repo.run(IP.RepoNmae.username_ipv4_repo, IP.RepoNmae.description, IP.IPV4)
#
#     @pytest.mark.run(order=6)
#     def test_methodf(self):
#
#         self.Org.org()
#         self.Org.add_Org()
#         time.sleep(2)
#         self.Org.enter_username(IP.OrganName.Org1_username)
#         self.Org.enter_description(IP.OrganName.Org1)
#         time.sleep(1)
#         self.Org.dropDown()
#         self.Org.click_drop_down()
#         time.sleep(4)
#         self.Org.Submit()
#
#         self.Org.popup()
#
#     @pytest.mark.run(order=7)
#     def test_methode(self):
#         self.con.click_on_system()
#         self.con.click_on_configuration()
#         self.con.click_on_pluginsorfeed()
#         time.sleep(2)
#         self.con.click_inside_pluginsorfeed()
#
#
#
#
#
#
#
#
