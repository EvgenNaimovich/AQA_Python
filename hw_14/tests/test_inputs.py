from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.parametrize("input_data, expected", [
    ("asdf", ""),
    ("-1123E35","-1123E35"),
    (Keys.ARROW_UP, "1"),
    (Keys.ARROW_DOWN, "-1"),
    (-123, "-123")
])
def test_inputs(browser_chrome, input_data, expected):
    browser_chrome.get("https://the-internet.herokuapp.com/inputs")
    input_numbers = browser_chrome.find_element(By.TAG_NAME, "input")
    input_numbers.click()
    input_numbers.send_keys(input_data)
    assert input_numbers.get_attribute("value") == expected
