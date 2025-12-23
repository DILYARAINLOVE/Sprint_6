import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    URL = 'https://qa-scooter.praktikum-services.ru/'
    
    # Локаторы
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    QUESTION_BUTTONS = (By.CSS_SELECTOR, '[class*="accordion__button"]')
    QUESTION_ANSWERS = (By.CSS_SELECTOR, '[class*="accordion__panel"]')
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[text()="Заказать"][@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    
    def __init__(self, driver):
        super().__init__(driver, self.URL)
    
    @allure.step('Открыть страницу и принять куки')
    def open_and_accept_cookies(self):
        self.open()
        self.click_element(self.COOKIE_BUTTON)
    
    @allure.step('Получить список вопросов')
    def get_question_buttons(self):
        return self.find_elements(self.QUESTION_BUTTONS)
    
    @allure.step('Нажать на вопрос с индексом {index}')
    def click_question(self, index):
        buttons = self.get_question_buttons()
        self.scroll_to_element_object(buttons[index])
        buttons[index].click()
    
    @allure.step('Получить текст ответа с индексом {index}')
    def get_answer_text(self, index):
        answers = self.find_elements(self.QUESTION_ANSWERS)
        return answers[index].text
    
    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click_element(self.ORDER_BUTTON_TOP)
    
    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
        self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
    
    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)