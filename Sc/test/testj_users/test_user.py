

from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import IpvRepo
from pages.user.users import user, users, Roles
import unittest
from utilities.ip_file import IP
import pytest
import time
# from utilities.custom_logger import setup_logging
from ddt import data, unpack, ddt
from random import random


@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Users(unittest.TestCase):
    # setup_logging(__name__)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.user = user(self.driver)
        self.users = users(self.driver)
        self.role = Roles(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing successful")

    @data({'org_username': 'username', 'firstname': 'test_sm', 'username': 'test_sm', 'password': 'admin',
           'confirmpassword': 'admin'})
    @pytest.mark.run(order=2)
    @unpack
    def testb_add_user(self, org_username, username, firstname,password, confirmpassword):
        self.user.click_user_icon()
        self.users.click_users_icon()
        self.users.click_add_user()
        time.sleep(5)
        self.users.click_role()
        # self.users.click_securitymanager()
        self.users.select_org()
        time.sleep(0.5)
        # self.users.enterorgname()
        self.users.enter_org_username(org_username)
        self.users.enter_firstname(firstname)
        self.users.enter_username(username)
        self.users.enter_password(password)
        self.users.enter_confirmpassword(confirmpassword)
        self.users.Submit()

    @data({'usernamne':'CustomSecurityManager'})
    @unpack
    def testc_add_role(self,usernamne):
        time.sleep(4)
        self.user.click_user_icon()
        self.role.clickrole()
        self.role.clickadd()

        self.role.entername(name=usernamne)

        self.role.checkboxcreatescan()

        self.role.MangerecastRule()

        self.users.Submit()




