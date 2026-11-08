import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_add_remove_elements(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser_chrome.find_element(By.XPATH, "//button[text()='Add Element']")
    add_element.click()
    add_element.click()
    count_add_element = len(browser_chrome.find_elements(By.XPATH, "//button[text()='Delete']"))
    assert count_add_element == 2, f"Количество 'Delete' должно быть 2, но получено -> {count_add_element}"

    del_element = browser_chrome.find_element(By.XPATH, "//button[text()='Delete']")
    del_element.click()
    count_del_element = len(browser_chrome.find_elements(By.XPATH, "//button[text()='Delete']"))
    assert count_del_element == 1, f"Количество 'Delete' должно быть 1, но получено -> {count_del_element}"