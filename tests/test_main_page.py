import pytest
import allure
from pages.main_page import MainPage
from data.test_data import TestData

class TestMainPage:
    @pytest.mark.parametrize('question_index, expected_answer', 
                             enumerate(TestData.EXPECTED_ANSWERS))
    @allure.title('Проверка ответа на вопрос №{question_index}')
    def test_question_answer(self, driver, question_index, expected_answer):
        page = MainPage(driver)
        page.open_and_accept_cookies()
        
        page.click_question(question_index)
        actual_answer = page.get_answer_text(question_index)
        
        assert expected_answer in actual_answer, \
            f'Ожидался текст: {expected_answer[:50]}...\nПолучен: {actual_answer[:50]}...'
    
    @allure.title('Переход на главную по логотипу Самоката')
    def test_scooter_logo_redirect(self, driver):
        page = MainPage(driver)
        page.open_and_accept_cookies()
        page.click_scooter_logo()
        
        current_url = page.get_current_url()
        assert 'qa-scooter.praktikum-services.ru' in current_url