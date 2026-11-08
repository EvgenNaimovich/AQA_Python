import pytest
from selenium import webdriver


@pytest.fixture()
def browser_chrome():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()