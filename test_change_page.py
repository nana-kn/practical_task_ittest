from .pages.register_page import RegisterPage
from .pages.change_password_page import ChangePasswordPage
from .pages.login_page import LoginPage
from .pages.locators import RegisterPageLocators, LoginPageLocators, ChangePasswordPageLocators
from .test_data.users import User_Successful, ChangePassword_Successful
import time
import pytest

class TestChangePassword():  
    # тест на успешную смену пароля 
    @pytest.mark.need_review
    def test_guest_can_register(self, browser):      
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Successful)
        register_page.should_be_successful_registration_message()

    def test_quest_can_change_password(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Successful.password, ChangePassword_Successful.confirm_password)
        change_password_page.should_be_successful_change_password_message()
