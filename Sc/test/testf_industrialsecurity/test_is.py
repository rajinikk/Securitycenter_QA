from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import IpvRepo
from pages.industrial_security.indutrial_security_instances import IndustrialSecurityInstances
import unittest
from utilities.ip_file import IP
import pytest
import time






@pytest.mark.usefixtures("oneTimeSetUp")
class Repo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.isi = IndustrialSecurityInstances(self.driver)

    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin", "admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing successful")

    def testb_add_is_instance(self):
        self.isi.click_Resource()
        self.isi.clickIsi()
        self.isi.IsiAdd()
        time.sleep(2)
        self.isi.isi_name(IP.Isi.name_isi)
        time.sleep(2)
        self.isi.isi_description(IP.Isi.description_isi)
        time.sleep(2)
        self.isi.host(IP.Isi.isi_host)
        time.sleep(5)
        self.isi.isi_username(IP.Isi.username_isi)
        self.isi.isi_password(IP.Isi.password_isi)
        self.isi.isi_Repositories(IP.RepoName.username_ipv4_repo)
        time.sleep(3)
        self.isi.isi_reposelect()
        self.isi.submit()
