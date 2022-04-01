from .pages.register_page import RegisterPage
from .pages.change_password_page import ChangePasswordPage
from .pages.login_page import LoginPage
from .pages.locators import RegisterPageLocators, LoginPageLocators, ChangePasswordPageLocators
from .test_data.users import User_Successful, ChangePassword_Successful, ChangePassword_Wrong, ChangePassword_Wrong_Format, ChangePassword_Confirm_Password, ChangePassword_Password
import time
import pytest

class TestChangePassword():  
    # регистрация пользователя 
    @pytest.mark.need_review
    def test_guest_can_register(self, browser):      
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Successful)
        register_page.should_be_successful_registration_message()
    

    # тест на успешную смену пароля
    def test_quest_can_change_password(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Successful.password, ChangePassword_Successful.confirm_password)
        change_password_page.should_be_successful_change_password_message()


    # неверно указан старый пароль
    def test_quest_can_not_change_password_old_password_is_wrong(self, browser):
        password = "1234567_Ittest"

        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(password, ChangePassword_Successful.password, ChangePassword_Successful.confirm_password)
        change_password_page.should_be_unsuccessful_change_old_password_is_wrong()


    # не указан старый пароль
    def test_quest_can_not_change_password_old_password_is_required(self, browser):
        password = ""

        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(password, ChangePassword_Successful.password, ChangePassword_Successful.confirm_password)
        change_password_page.should_be_unsuccessful_change_old_password_is_required()
    

    # new password и confirm password не совпадают
    def test_quest_can_not_change_password_new_password_and_confirm_password_do_not_match(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Wrong.password, ChangePassword_Wrong.confirm_password)
        change_password_page.should_be_unsuccessful_change_new_password_and_confirm_password_do_not_match()


    # new password не соответствует формату (указано меньше 6 символов)
    def test_quest_can_not_change_password_new_password_and_confirm_password_do_not_match(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Wrong_Format.password, ChangePassword_Wrong_Format.confirm_password)
        change_password_page.should_be_unsuccessful_change_wrong_format_new_password()


    # не указан confirm password
    def test_quest_can_not_change_password_confirm_password_is_required(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Confirm_Password.password, ChangePassword_Confirm_Password.confirm_password)
        change_password_page.should_be_unsuccessful_change_confirm_password_is_required()


    # не указан новый пароль
    def test_quest_can_not_change_password_new_password_is_required(self, browser):
        change_password_page = ChangePasswordPage(browser, ChangePasswordPageLocators.LINK)     
        change_password_page.open()                                           
        change_password_page.login_user(User_Successful.email, User_Successful.password)
        change_password_page.should_be_elements_for_change_password()
        change_password_page.change_password(User_Successful.password, ChangePassword_Password.password, ChangePassword_Password.confirm_password)
        change_password_page.should_be_unsuccessful_change_new_password_is_required()
