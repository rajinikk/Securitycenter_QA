from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.scanzone.zone import Zone, Scandata
from pages.nessusscaner.nessusscaner import NessusScanner
from pages.Repositories.repos_page import Repos, IpvRepo
from pages.org.org_files import Org
from utilities.ip_file import IP
from pages.Ldap_Servers.Ldap_servers import LdapServers
import unittest
import pytest
from ddt import data, unpack, ddt
import time
import logging
# from utilities.custom_logger import setup_logging
from random import random


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class LadapServer(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        logging.info("testing this file")
        logging.info("started loggin ")
        self.lp = LoginPage(self.driver)
        # self.zone = Zone(self.driver)
        # self.scandata = Scandata(self.driver)
        self.ldp = LdapServers(self.driver)

    @pytest.mark.run(order=1)
    def testa_method(self):
        self.lp.login("admin", "admin")
        logging.info("Entering data for username and password for login")
        success = self.lp.verifyLoginSuccessful()
        logging.info("Logging is successfull")
        time.sleep(2)
        if success == "Dashboard":
            logging.debug("Login Succesfull if {} is {}".format(success, 'Dashboard'))


    @data({'name':'LDAP 3 Test','description':'(devldap2.devldap2.lab.tenablesecurity.com)','hostIP':'172.26.97.2','non':'None','username':'devldap20'+'\\a'+'dministrator','password':'LabPass1',
            'BaseDN':'CN=Users,DC=devldap2,DC=lab,DC=tenablesecurity,DC=com','UserObjectFilte':'sAMAccountName=*','nameattr':'sAMAccountName','emailattr':'mail',
           'phoneattr':'telephoneNumber','nameattrsecound':'CN'})
    @pytest.mark.run(order=2)
    @unpack
    def testb_add_ldps(self,name,description,hostIP,non,username,password,BaseDN, UserObjectFilte,nameattr,emailattr,phoneattr, nameattrsecound):
        self.ldp.click_resources()
        self.ldp.click_ldap_servers()
        self.ldp.add()
        self.ldp.ldap_name(name)
        self.ldp.ldap_description(description)
        self.ldp.ldap_host_name(hostIP)
        time.sleep(5)
        self.ldp.clickdropdown()
        self.ldp.elementhovering(Non=non)
        self.ldp.ldap_user_name(username)
        self.ldp.ldap_password(password=password)
        self.ldp.ldap_Base_DN(base_dn=BaseDN)
        self.ldp.user_object_filter(filter=UserObjectFilte)
        self.ldp.username_attribute(nameattr)
        self.ldp.email_attribute(email_attribute=emailattr)
        self.ldp.phone_attribute(phone_attribute=phoneattr)
        self.ldp.name_attribute(name_attribute=nameattrsecound)
        self.ldp.test_setting()
        time.sleep(3)
        self.ldp.submit()



