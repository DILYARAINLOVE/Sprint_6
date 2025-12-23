import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData

class TestOrder:
    @allure.title('Оформление заказа через верхнюю кнопку')
    @pytest.mark.parametrize('order_data', [TestData.ORDER_DATA[0]])
    def test_successful_order_via_top_button(self, driver, order_data):
        """Тест оформления заказа через верхнюю кнопку."""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу и принять куки'):
            main_page.open_and_accept_cookies()
        
        with allure.step('Нажать верхнюю кнопку "Заказать"'):
            main_page.click_top_order_button()
        
        with allure.step('Заполнить форму заказа'):
            order_page.fill_first_page(
                order_data.name,
                order_data.surname,
                order_data.address,
                order_data.metro_station,
                order_data.phone
            )
            
            order_page.fill_second_page(
                order_data.date,
                order_data.rental_period,
                order_data.color,
                order_data.comment
            )
        
        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()
        
        with allure.step('Проверить успешное оформление'):
            assert order_page.is_order_successful(), 'Заказ не был оформлен успешно'
    
    @allure.title('Оформление заказа через нижнюю кнопку')
    @pytest.mark.parametrize('order_data', [TestData.ORDER_DATA[1]])
    def test_successful_order_via_bottom_button(self, driver, order_data):
        """Тест оформления заказа через нижнюю кнопку."""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную страницу и принять куки'):
            main_page.open_and_accept_cookies()
        
        with allure.step('Нажать нижнюю кнопку "Заказать"'):
            main_page.click_bottom_order_button()
        
        with allure.step('Заполнить форму заказа'):
            order_page.fill_first_page(
                order_data.name,
                order_data.surname,
                order_data.address,
                order_data.metro_station,
                order_data.phone
            )
            
            order_page.fill_second_page(
                order_data.date,
                order_data.rental_period,
                order_data.color,
                order_data.comment
            )
        
        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()
        
        with allure.step('Проверить успешное оформление'):
            assert order_page.is_order_successful(), 'Заказ не был оформлен успешно'