import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_typos(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/typos")

    for i in range(10):
        element = browser_chrome.find_element(By.XPATH, "//div[@class='example']/p[2]")
        assert element.text == "Sometimes you'll see a typo, other times you won't.",(
            f"Ожидалось -> Sometimes you'll see a typo, other times you won't."
            f"Получено -> {element.text}. Некорректный текст получен на {i + 1} попытке")
        browser_chrome.refresh()