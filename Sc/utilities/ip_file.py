from random import random


class IP(object):
    IPV4 = "172.26.48.0/24" + ",172.26.0.0/24"
    IPV6 = "2001:db8:26:18:250:56ff:fea6:7960,2001:db8:26:18:250:56ff:fea6:757f/64"

    class RepoName(object):
        # ipv4
        username_ipv4_repo = "Test_Ipv4_repo"
        description = "Repo for ipv4 ip ranges "
        # ipv6
        username_ipv6_repo = "Test_Ipv6_repo"
        description_ipv6 = "Repo for ipv6 ip ranges "
        # mobile
        username_mobile_repo = "Test_mobile_repo"
        description_mobile = "Lakshmi Priya"
        domain_controller = "tenablerelab3.com"
        domain = "tenablerelab3.com"
        domain_Username = "administrator"
        domain_Password = "sapphire"
        # Agent
        Agent_username = "test_agent"
        Agent_description = "Agent Description value"

    class OrganName(object):
        Org1_username = "username"
        Org1 = "Org1_admin"

    class Scandata(object):
        Obj1 = "test data for scan zone"
        Name = "Nessus1" + str(random())
        search_Centos = "Centos"
        search_Windows = "Windows"

    class Nessusscannerdata(object):
        setnessusname = "Nessus scannner" + str(random())
        setdescription = "nessus scanner to add in tenbalesc"
        sethost = "172.26.16.133"
        setport = "8834"
        admin_username = "admin"
        admin_password = "admin"

    class Nnm(object):
        setnessusname = "Nessus scannner" + str(random())
        setdescription = "nessus scanner to add in tenbalesc"
        sethost = "172.26.16.94"
        setport = "8834"
        admin_username = "admin"
        admin_password = "LabPass1@"

    class Isi(object):
        name_isi = "isi_test2" + str(random())
        isi_host = "172.26.18.93"
        description_isi = "fjiowejiofssjjiosdfu9werwoiprsedfkljsdfop"
        username_isi = "admin"
        password_isi = "LabPass1@"

    class User(object):
        first_Name = "test_sm"
        username = "test_sm"
        password = "admin"
        confirmPassword = "admin"

    class TenableIo(object):
        first_name = "test_tenableio"+str(random)
        ip_combination = "18.236.123.145"+",34.213.181.16"+",35.162.215.149"
        admin_username = "testing_team1@tenabletesting.dev"
        admin_password = "LabPass1!"

