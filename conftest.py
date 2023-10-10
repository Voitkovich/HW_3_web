import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

@pytest.fixture(scope="session")   #будет действовать всю сессию
def browser(): 
    browser == "chrome"
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# with open("config.yaml") as f:
#     testdata = yaml.safe_load(f)
#     service = Service(testdata['browser'])
#     options = webdriver.ChromeOptions

# class Site:
#     def __init__(self, address):
#         self.driver = webdriver.Chrome(service=service,
#                                        options=options)

#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.driver.get(address)
#         time.sleep(testdata["sleep_time"])