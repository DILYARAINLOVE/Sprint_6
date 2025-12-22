import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture
def driver():
    # Указываем путь к geckodriver (на Mac после Homebrew он обычно здесь)
    service = FirefoxService('/opt/homebrew/bin/geckodriver')
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()