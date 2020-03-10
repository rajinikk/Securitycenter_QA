from pages.home.login_page import LoginPage
import unittest
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.securitymanagerreport.securtiymanger import Report,DiscoveryDetection, ReportAttribute
from selenium.webdriver.support import expected_conditions as cond
import time
from ddt import data, unpack, ddt

@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class OrgUsers(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.rp = Report(self.driver)
        self.dis = DiscoveryDetection(self.driver)
        self.attr =  ReportAttribute(self.driver)

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

    @data({'ipaddrshow': '172.26.18.0/24 , 172.26.48.0/24'})
    @pytest.mark.run(order=1)
    @unpack
    def testb_add_report(self, ipaddrshow):
        print("Compliance report")
        self.rp.reportingBanner()
        self.rp.reports()
        self.rp.addreport()
        self.rp.complianceandconfiguration()
        self.rp.fistcompliancereport()
        self.rp.clickallsytems()
        self.rp.clickIp()
        self.rp.iptextarea(iparea=ipaddrshow)
        self.rp.selectallrepo()
        self.rp.submitform()

    @data({'ipaddrshow': '172.26.18.0/24 , 172.26.48.0/24'})
    @pytest.mark.run(order=1)
    @unpack
    def testc_runreprt(self,ipaddrshow):
        self.rp.runreport()
        time.sleep(3)
        self.rp.reportresult()
        time.sleep(5)
        self.rp.reportingBanner()
        self.rp.reports()
        self.rp.addreport()
        self.rp.monitoring()
        self.rp.cloudreport()
        self.rp.clickallsytems()
        self.rp.clickIp()
        self.rp.iptextarea(iparea=ipaddrshow)
        self.rp.selectallrepo()
        self.rp.submitform()

    @data({'ipaddrshow': '172.26.18.0/24 , 172.26.48.0/24'})
    @pytest.mark.run(order=2)
    @unpack
    def testd_discoverydetection(self,ipaddrshow):
        time.sleep(5)
        self.rp.reportingBanner()
        self.rp.addreport()
        self.dis.discovery()
        time.sleep(2)
        self.dis.patchmanagement()
        self.rp.clickallsytems()
        self.rp.clickIp()
        self.rp.iptextarea(iparea=ipaddrshow)
        self.rp.selectallrepo()
        self.rp.submitform()

    @data({'Name': 'Cyberscope attribute'})
    @pytest.mark.run(order=2)
    @unpack
    def teste_reportattribute(self,Name):
        self.attr.reportattribute()
        self.attr.add_attribute()
        self.attr.addname(name=Name)
        self.rp.submitform()







