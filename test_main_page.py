from .main_page import MainPage
import pytest

class TestRegisterFromMainPage():
    def test_guest_can_go_to_register_page(self, browser):
        link = "http://demowebshop.tricentis.com/"
        main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        main_page.open()                      # открываем страницу
        main_page.go_to_register_page()       # выполняем метод страницы — переходим на страницу регистрации