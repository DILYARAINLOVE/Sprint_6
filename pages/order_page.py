import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class OrderPage(BasePage):
    # Локаторы первой страницы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='{station}']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы второй страницы
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{period}']")
    BLACK_CHECKBOX = (By.ID, 'black')
    GREY_CHECKBOX = (By.ID, 'grey')
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    
    # Локаторы модального окна
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[@class='Order_Text__2broi']")
    
    @allure.step('Ввести имя: {name}')
    def enter_name(self, name):
        self.send_keys_to_element(self.NAME_FIELD, name)
    
    @allure.step('Ввести фамилию: {surname}')
    def enter_surname(self, surname):
        self.send_keys_to_element(self.SURNAME_FIELD, surname)
    
    @allure.step('Ввести адрес: {address}')
    def enter_address(self, address):
        self.send_keys_to_element(self.ADDRESS_FIELD, address)
    
    @allure.step('Выбрать станцию метро: {station}')
    def select_metro_station(self, station):
        self.click_element(self.METRO_FIELD)
        station_locator = (self.METRO_STATION[0], self.METRO_STATION[1].format(station=station))
        self.click_element(station_locator)
    
    @allure.step('Ввести телефон: {phone}')
    def enter_phone(self, phone):
        self.send_keys_to_element(self.PHONE_FIELD, phone)
    
    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
    
    @allure.step('Заполнить первую страницу заказа')
    def fill_first_page(self, name, surname, address, metro, phone):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.select_metro_station(metro)
        self.enter_phone(phone)
        self.click_next_button()
    
    @allure.step('Ввести дату доставки: {date}')
    def enter_date(self, date):
        self.send_keys_to_element(self.DATE_FIELD, date)
    
    @allure.step('Выбрать срок аренды: {period}')
    def select_rental_period(self, period):
        self.click_element(self.RENTAL_PERIOD_FIELD)
        period_locator = (self.RENTAL_PERIOD_OPTION[0], 
                         self.RENTAL_PERIOD_OPTION[1].format(period=period))
        self.click_element(period_locator)
    
    @allure.step('Выбрать цвет самоката: {color}')
    def select_color(self, color):
        if color == 'black':
            self.click_element(self.BLACK_CHECKBOX)
        elif color == 'grey':
            self.click_element(self.GREY_CHECKBOX)
    
    @allure.step('Ввести комментарий: {comment}')
    def enter_comment(self, comment):
        self.send_keys_to_element(self.COMMENT_FIELD, comment)
    
    @allure.step('Нажать кнопку "Заказать" на второй странице')
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)
    
    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)
    
    @allure.step('Проверить успешное оформление заказа')
    def is_order_successful(self):
        try:
            self.find_element(self.ORDER_SUCCESS_MODAL)
            return True
        except:
            return False
    
    @allure.step('Получить текст успешного оформления')
    def get_success_message(self):
        return self.get_element_text(self.ORDER_SUCCESS_TEXT)