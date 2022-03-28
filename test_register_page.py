from .register_page import RegisterPage
import time


class TestRegistration():   
    #тест на успешную регистрацию
    def test_guest_can_register(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "_Itetst"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_successful_registration_message()
        
        
    # пароли не совпадают
    def test_guest_can_not_register_passwords_do_not_match(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "_Itetst"
        confirm_password = str(time.time()) + "_Itetst1"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, confirm_password)
        register_page.should_be_unsuccessful_registration_message_passwords_do_not_match()
        
        
    # Имя пользователя не указано
    def test_guest_can_not_register_First_name_is_required(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = ""
        last_name = "Popova"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "_Itetst"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_unsuccessful_registration_message_First_name_is_required()
        time.sleep(3)
        
    # Фамилия пользователя не указана
    def test_guest_can_not_register_Last_name_is_required(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = ""
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "_Itetst"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_unsuccessful_registration_message_Last_name_is_required()
        time.sleep(3)
        
        #Почта не указана
    def test_guest_can_not_register_Email_name_is_required(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = ""
        password = str(time.time()) + "_Itetst"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_unsuccessful_registration_message_Email_is_required()
        time.sleep(3)
        
    #Неверный формат почты
    def test_guest_can_not_register_Wrong_email(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = str(time.time())
        password = str(time.time()) + "_Itetst"
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_unsuccessful_registration_message_Wrong_email()
        time.sleep(3)    
        
    # Пароль не указан
    def test_guest_can_not_register_Password_is_required(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = str(time.time()) + "@fakemail.org"
        password = ""
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, password)
        register_page.should_be_unsuccessful_registration_message_Password_is_required()
        time.sleep(3)
        
     # Пароль для подтверждения не указан
    def test_guest_can_not_register_Confirm_password_is_required(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        first_name = "Ekaterina"
        last_name = "Popova"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "_Itetst"
        confirm_password = ""
       
        register_page = RegisterPage(browser, link)              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        register_page.open()                                     # открываем страницу
        register_page.should_be_elements_for_register()
        register_page.register_new_user(first_name, last_name, email, password, confirm_password)
        register_page.should_be_unsuccessful_registration_message_Confirm_password_is_required()
        time.sleep(3)
        