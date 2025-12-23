import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData

class TestOrder:
    @pytest.mark.parametrize('order_data', TestData.ORDER_DATA)
    @allure.title('Оформление заказа: {order_data.name} {order_data.surname}')
    def test_successful_order(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step('Открыть главную и принять куки'):
            main_page.open_and_accept_cookies()
        
        with allure.step('Нажать кнопку "Заказать"'):
            if order_data.use_top_button:
                main_page.click_top_order_button()
            else:
                main_page.click_bottom_order_button()
        
        with allure.step('Заполнить первую страницу заказа'):
            order_page.fill_first_page(
                order_data.name,
                order_data.surname,
                order_data.address,
                order_data.metro_station,
                order_data.phone
            )
        
        with allure.step('Заполнить вторую страницу заказа'):
            order_page.enter_date(order_data.date)
            order_page.select_rental_period(order_data.rental_period)
            order_page.select_color(order_data.color)
            order_page.enter_comment(order_data.comment)
            order_page.click_order_button()
        
        with allure.step('Подтвердить заказ'):
            order_page.confirm_order()
        
        with allure.step('Проверить успешное оформление'):
            assert order_page.is_order_successful(), 'Не появилось окно успешного оформления'