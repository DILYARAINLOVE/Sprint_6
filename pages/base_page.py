import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step('Открыть страницу')
    def open(self):
        self.driver.get(self.url)
    
    @allure.step('Найти элемент {locator}')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Найти элементы {locator}')
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step('Кликнуть на элемент {locator}')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    @allure.step('Получить текст элемента {locator}')
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step('Ввести текст "{text}" в элемент {locator}')
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)
    
    @allure.step('Проскроллить к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Проскроллить к переданному элементу')
    def scroll_to_element_object(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title