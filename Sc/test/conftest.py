import pytest
from pages.home.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        baseURL = "https://172.26.18.173"
        driver = webdriver.Firefox(executable_path=r'C:\Users\delixus\Documents\New folder\Sc\geckodriver.exe')
        driver.maximize_window()
        
        driver.implicitly_wait(9)
        driver.get(baseURL
                   )
        print("Running tests on FF")
    else:
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        baseURL = "https://172.26.18.173"
        print("running test on chrome file")
        # driver = webdriver.Chrome(executable_path=r'C:\Users\delixus\Documents\New folder\Sc\chromedriver.exe')
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(9)
        driver.get(baseURL)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")





