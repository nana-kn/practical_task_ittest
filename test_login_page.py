from .login_page import LoginPage
import time

class TestAuthorization():
    #тест на успешную авторизацию
    def test_guest_can_login(self, browser):
        link = "http://demowebshop.tricentis.com/login"
        email = "Katerina_Popova@fakemail.org"
        password = '1234567_Itetst'
       
        login_page = LoginPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        login_page.open()                                  # открываем страницу
        login_page.login_user(email, password)
        login_page.should_be_authorized_user(email)
    