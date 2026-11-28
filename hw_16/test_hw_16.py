import os.path
from pathlib import Path
from time import sleep
from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.advanced
def test_context_menu(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/context_menu")
    time_wait = WebDriverWait(browser_chrome, 10)
    elem = browser_chrome.find_element(By.CSS_SELECTOR, "#hot-spot")
    actions = ActionChains(browser_chrome)
    actions.move_to_element(elem).context_click().perform()
    time_wait.until(EC.alert_is_present())
    alert = browser_chrome.switch_to.alert
    assert alert.text == "You selected a context menu"
    alert.accept()


@pytest.mark.advanced
def test_dynamic_control(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/dynamic_controls")
    browser_chrome.find_element(By.XPATH, "//*[@type='button' and text()='Remove']").click()
    time_wait = WebDriverWait(browser_chrome, 10)
    elem_massage = time_wait.until(EC.visibility_of_element_located((By.ID, 'message')))
    assert elem_massage.text == "It's gone!", f"Ожидается 'It's gone!', получено {elem_massage.text}"

    assert not browser_chrome.find_element(By.XPATH, "//*[@id='input-example']/input").is_enabled()
    checkbox = browser_chrome.find_elements(By.XPATH, "//*[@type='checkbox']")
    assert len(checkbox) == 0, f"Ожидалось, что чекбокс отсутствует на странице. Кол-во checkbox: {len(checkbox)}."

    browser_chrome.find_element(By.XPATH, "//*[@type='button' and text()='Enable']").click()
    msg = time_wait.until(EC.visibility_of_element_located((By.ID, 'message')))
    assert msg.text == "It's enabled!", f"Ожидается 'It's enabled!', получено {msg.text}"

    elem_input = time_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    elem_input.send_keys("Хорошего дня!")
    assert elem_input.is_enabled(), "Поле ввода не стало активным"


@pytest.mark.advanced
def test_file_upload(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/upload")
    file_path = Path("Slutskiya_tkachykhi.txt").resolve()
    browser_chrome.find_element(By.CSS_SELECTOR, "#file-upload").send_keys(str(file_path))
    browser_chrome.find_element(By.CSS_SELECTOR, "#file-submit").click()
    time_wait = WebDriverWait(browser_chrome, 10)
    name_file = time_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#uploaded-files")))
    assert name_file.text == file_path.name, f"Загрузился файл {name_file.text}. Ожидался {file_path.name}"


@pytest.mark.advanced
def test_frames(browser_chrome):
    browser_chrome.get("https://the-internet.herokuapp.com/frames")
    browser_chrome.find_element(By.XPATH, "//a[@href='/iframe']").click()
    time_wait = WebDriverWait(browser_chrome, 10)
    iframe = time_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mce_0_ifr")))
    browser_chrome.switch_to.frame(iframe)
    text_frame = browser_chrome.find_element(By.CSS_SELECTOR, "#tinymce > p")
    assert text_frame.text == "Your content goes here.", f"Ожидалось 'Your content goes here.'. Получено {text_frame.text}"
    browser_chrome.switch_to.default_content()


@pytest.mark.advanced
def test_file_download(browser_chrome):
    downloads_dir = os.path.abspath("downloads")
    os.makedirs(downloads_dir, exist_ok=True)
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": downloads_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)
    browser_chrome = webdriver.Chrome(options=options)
    browser_chrome.get("https://the-internet.herokuapp.com/download")
    browser_chrome.find_element(By.CSS_SELECTOR, "a[href*='Slutskiya_tkachykhi']").click()
    file_path = Path(downloads_dir) / "Slutskiya_tkachykhi.txt"
    time_wait = WebDriverWait(browser_chrome, 10)
    time_wait.until(lambda driver: file_path.exists() and not list(
        Path(downloads_dir).glob("*.crdownload")
    ))
    assert file_path.is_file()
    browser_chrome.quit()


