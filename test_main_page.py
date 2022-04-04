from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.locators import BasePageLocators


class TestRegisterFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, BasePageLocators.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        main_page.open()                      # открываем страницу
        main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу авторизации
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_elements_for_login()

class TestLoginFromMainPage():    
    def test_guest_can_go_to_register_page(self, browser):
        main_page = MainPage(browser, BasePageLocators.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        main_page.open()                      # открываем страницу
        main_page.go_to_register_page()       # выполняем метод страницы — переходим на страницу регистрации
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_elements_for_register()
