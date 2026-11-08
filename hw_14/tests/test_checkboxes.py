import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_checkboxes(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = browser_chrome.find_elements(By.CSS_SELECTOR, "[type='checkbox']")
    assert False == checkboxes[0].is_selected(), f"checkbox_1 ожидает False, получено -> {checkboxes[0].is_selected()}"

    checkboxes[0].click()
    assert True == checkboxes[0].is_selected(), f"checkbox_1 ожидает True, получено -> {checkboxes[0].is_selected()}"

    assert True == checkboxes[1].is_selected(), f"checkbox_2 ожидает True, получено -> {checkboxes[0].is_selected()}"
    checkboxes[1].click()
    assert False == checkboxes[1].is_selected(), f"checkbox_2 ожидает False, получено -> {checkboxes[0].is_selected()}"



