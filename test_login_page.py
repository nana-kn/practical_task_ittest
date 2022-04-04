from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .test_data.users import User_Successful, User_Empty, User_Wrong
from .pages.locators import LoginPageLocators
from .pages.locators import RegisterPageLocators
import pytest

class TestAuthorization(): 
    
    @pytest.mark.need_review
    def test_guest_can_register(self, browser):      
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Successful)
        register_page.should_be_successful_registration_message()


    @pytest.mark.need_review
    #тест на успешную авторизацию
    def test_guest_can_login(self, browser):
        login_page = LoginPage(browser, LoginPageLocators.LINK)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        login_page.open()                                               # открываем страницу
        login_page.login_user(User_Successful.email, User_Successful.password)
        login_page.should_be_authorized_user(User_Successful)
    

    @pytest.mark.need_review
    # указан неверный пароль
    def test_guest_can_not_login_wrong_password(self, browser):
        password = "1234567_Ittest"
        
        login_page = LoginPage(browser,  LoginPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        login_page.open()                                               # открываем страницу
        login_page.login_user(User_Successful.email, password)
        login_page.should_be_unsuccessful_login()
    
    
    # данные не введены
    def test_guest_can_not_login_no_data_entered(self, browser):       
        login_page = LoginPage(browser,  LoginPageLocators.LINK)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        login_page.open()                                  # открываем страницу
        login_page.login_user(User_Empty.email, User_Empty.password)
        login_page.should_be_unsuccessful_login()