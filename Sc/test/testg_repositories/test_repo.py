from pages.home.login_page import LoginPage
from pages.Repositories.repos_page import Repos, IpvRepo, Mobile, AgentRepo
import unittest
from utilities.ip_file import IP
import pytest
from ddt import data, unpack, ddt
import time
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Repo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.rp = Repos(self.driver)
        self.IpvRepo = IpvRepo(self.driver)
        self.Mobile = Mobile(self.driver)
        self.agent = AgentRepo(self.driver)
   
    @pytest.mark.run(order=1)
    def testa_add_logina(self):
        self.lp.login("admin","admin")
        success = self.lp.verifyLoginSuccessful()
        time.sleep(2)
        if success == "Dashboard":
            print("testing succefull")

    @pytest.mark.run(order=2)
    def testb_add_repo(self):
        self.rp.repotest()

    @pytest.mark.run(order=3)
    def testc_add_ipv4(self):

        self.IpvRepo.enter_Username(IP.RepoName.username_ipv4_repo)
        self.IpvRepo.enter_description(IP.RepoName.description)
        self.IpvRepo.enter_ip_ranges(ipranges=IP.IPV4)
        self.IpvRepo.trend_data()
        self.IpvRepo.trend_data()
        time.sleep(2)
        self.IpvRepo.submit()
        time.sleep(2)

    @pytest.mark.run(order=3)
    def testd_add_ipv6(self):  # Ipv6
        self.rp.repotestIpv6()
        self.IpvRepo.enter_Username(IP.RepoName.username_ipv6_repo)
        self.IpvRepo.enter_description(IP.RepoName.description_ipv6)
        self.IpvRepo.enter_ip_ranges(ipranges=IP.IPV6)
        self.IpvRepo.trend_data()
        self.IpvRepo.trend_data()
        time.sleep(2)
        self.IpvRepo.submit()
        time.sleep(2)

    #Mobile
    @data({'first': 'Centos_Nessus'})
    @pytest.mark.run(order=3)
    @unpack
    def teste_add_mobile_repo(self, first):
        self.rp.mobile()
        self.Mobile.enter_Username(IP.RepoName.username_mobile_repo)
        self.Mobile.enter_description(IP.RepoName.description_mobile)
        self.Mobile.enter_domain_controller(IP.RepoName.domain_controller)
        self.Mobile.enter_domain(IP.RepoName.domain)
        self.Mobile.enter_domain_username(IP.RepoName.domain_Username)
        self.Mobile.enter_domain_password(IP.RepoName.domain_Password)
        self
        self.Mobile.select_scanner(name=first)

    def testf_add_agent_repo(self):
        self.rp.agent()
        self.agent.enter_Username(IP.RepoName.Agent_username)
        self.agent.enter_description(IP.RepoName.Agent_description)
        self.agent.submit()
    #repo
    @data({'name':'Tenable_io'})
    @unpack
    def testg_add_tenable_io_repo(self,name):
        self.IpvRepo.tenable_io()
        self.IpvRepo.enter_Username(name=name)
        self.IpvRepo.enter_description(IP.RepoName.description)
        self.IpvRepo.enter_ip_ranges(ipranges=IP.TenableIo.ip_combination)
        self.IpvRepo.trend_data()
        self.IpvRepo.trend_data()
        time.sleep(2)
        self.IpvRepo.submit()





