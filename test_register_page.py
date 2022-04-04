from .pages.register_page import RegisterPage
from .pages.locators import RegisterPageLocators
import time
from .test_data.users import User_Successful, User_Wrong, User_Name, User_Sername, User_Email, User_Wrong_Email, User_Wrong_Email2, User_Password, User_Confirm_Password, User_Empty, User_Wrong_Password
import pytest

class TestRegistration():    
    # тест на успешную регистрацию
    @pytest.mark.need_review
    def test_guest_can_register(self, browser):      
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Successful)
        register_page.should_be_successful_registration_message()
        
        
    # пароли не совпадают
    @pytest.mark.need_review
    def test_guest_can_not_register_passwords_do_not_match(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Wrong)
        register_page.should_be_unsuccessful_registration_message_passwords_do_not_match()
        
        
    # Имя пользователя не указано
    @pytest.mark.need_review
    def test_guest_can_not_register_First_name_is_required(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Name)
        register_page.should_be_unsuccessful_registration_message_First_name_is_required()
        

    # Фамилия пользователя не указана
    @pytest.mark.need_review
    def test_guest_can_not_register_Last_name_is_required(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Sername)
        register_page.should_be_unsuccessful_registration_message_Last_name_is_required()
        
    
    # Почта не указана
    @pytest.mark.need_review
    def test_guest_can_not_register_Email_name_is_required(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Email)
        register_page.should_be_unsuccessful_registration_message_Email_is_required()


    # Неверный формат почты (не указана @)
    @pytest.mark.need_review
    def test_guest_can_not_register_Wrong_email(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Wrong_Email)
        register_page.should_be_unsuccessful_registration_message_Wrong_email()    


    # Неверный формат почты (не указана .)
    @pytest.mark.need_review
    def test_guest_can_not_register_Wrong_email2(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Wrong_Email2)
        register_page.should_be_unsuccessful_registration_message_Wrong_email()    
    
        
    # Пароль не указан
    @pytest.mark.need_review
    def test_guest_can_not_register_Password_is_required(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Password)
        register_page.should_be_unsuccessful_registration_message_Password_is_required()


    # Неверный формат пароля (указано меньше 6 символов)
    @pytest.mark.need_review
    def test_guest_can_not_register_Password_is_wrong(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Wrong_Password)
        register_page.should_be_unsuccessful_registration_message_Password_is_wrong()


    # Пароль для подтверждения не указан
    @pytest.mark.need_review
    def test_guest_can_not_register_Confirm_password_is_required(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Confirm_Password)
        register_page.should_be_unsuccessful_registration_message_Confirm_password_is_required()


    # Поля не заполнены
    def test_guest_can_not_register_Form_is_empty(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Empty)
        register_page.should_be_unsuccessful_registration_message_First_name_is_required()


    # Повторная регистрация
    @pytest.mark.need_review
    def test_guest_can_not_register_re_registration(self, browser):
        register_page = RegisterPage(browser, RegisterPageLocators.LINK)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                                    # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(User_Successful)
        time.sleep(15)
        register_page.should_be_unsuccessful_registration_message_re_registration()



        