import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObjects.LoginPage import Loginpage


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        option1 = Options()
        option1.add_argument("--disable-notifications")
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Edge()
        print("Launching edgebrowser.........")
        return driver
    yield driver
    print("Test Case run complete")
    print("Browser closed")


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NGV Automation'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Nithya Lakshmi N'
    config._metadata['Test environment'] = 'https://dev-reader.tcdcloud.com/jupiter/index.html'


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
