from time import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.basic
def test_dropdown(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_element = browser_chrome.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    select.select_by_value("1")
    assert select.first_selected_option.text == "Option 1", (f"Должен был выбран select c текстом 'Option 1' "
                                                             f"но выбрано -> {select.first_selected_option.text} ")
    select.select_by_value("2")
    assert select.first_selected_option.text == "Option 2", (f"Должен был выбран select c текстом 'Option 2' "
                                                             f"но выбрано -> {select.first_selected_option.text} ")

