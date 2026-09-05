import pytest
from selenium import webdriver

from Pages.Login_Admin_page import Login_Admin_page
from utilities.read_properties import Read_Config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help= "specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("browser must be either chrome or firefox or edge")
    driver.maximize_window()
    yield driver  # 👈 test ko driver deta hai

    driver.quit()  # 👈 test ke baad close

@pytest.fixture
def login_setup(setup):
    driver = setup
    driver.maximize_window()
    driver.get(Read_Config.get_admin_page_url())
    login = Login_Admin_page(driver)

    login.login(Read_Config.get_username(), Read_Config.get_password())
    return driver



## pytest html custome report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata['Project Name'] = 'LearnProject'
    metadata['module name ']= 'login page'
    metadata['tester name ']= 'manisha'

@pytest.mark.optionalhook
def pytest_Metadat(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('plugin', None)


