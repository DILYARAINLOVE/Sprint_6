from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # URL тестового стенда
    URL = 'https://qa-scooter.praktikum-services.ru/'

    # Локаторы
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    QUESTION_BUTTONS = (By.CSS_SELECTOR, '[class*="accordion__button"]')
    QUESTION_ANSWERS = (By.CSS_SELECTOR, '[class*="accordion__panel"]')
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[text()="Заказать"][@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_and_accept_cookies(self):
        self.open()
        self.click_element(self.COOKIE_BUTTON)

    def get_question_buttons(self):
        return self.find_elements(self.QUESTION_BUTTONS)

    def click_question(self, index):
        buttons = self.get_question_buttons()
        buttons[index].click()

    def get_answer_text(self, index):
        answers = self.find_elements(self.QUESTION_ANSWERS)
        return answers[index].text

    def click_top_order_button(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        # Прокрутка к элементу перед кликом
        element = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()