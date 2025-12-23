import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    @allure.step('Инициализация Firefox драйвера')
    def init_driver():
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        return driver
    
    driver = init_driver()
    yield driver
    
    @allure.step('Закрытие браузера')
    def quit_driver():
        driver.quit()
    
    quit_driver()