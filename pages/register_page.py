from .base_page import BasePage
from .locators import RegisterPageLocators
from .locators import BasePageLocators
from ..test_data.users import TestUser

class RegisterPage(BasePage):
     
    def register_new_user(self, users:TestUser):
        fild_gender = self.browser.find_element(*RegisterPageLocators.GENDER)
        fild_gender.click()
        fild_first_name = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        fild_first_name.send_keys(users.first_name)
        fild_last_name = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        fild_last_name.send_keys(users.last_name)
        fild_email = self.browser.find_element(*BasePageLocators.EMAIL)
        fild_email.send_keys(users.email)
        fild_password = self.browser.find_element(*BasePageLocators.PASSWORD)
        fild_password.send_keys(users.password)
        fild_password_confirm = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        fild_password_confirm.send_keys(users.confirm_password)
        button = self.browser.find_element(*RegisterPageLocators.BUTTON_TO_REGISTER)
        button.click()      
        
    def should_be_button_to_register(self):   
        assert self.is_element_present(*RegisterPageLocators.BUTTON_TO_REGISTER), 'Кнопка "Register" отсутствует' 
    
    def should_be_elements_for_register(self):
        self.should_be_button_to_register()
        self.should_be_form_Your_Password()
        self.should_be_form_Your_Personal_Details() 
   
    def should_be_form_Your_Password(self):   
        assert self.is_element_present(*RegisterPageLocators.FORM_Your_Password), 'Форма "Your Password" отсутствует' 
        
    def should_be_form_Your_Personal_Details(self):   
        assert self.is_element_present(*RegisterPageLocators.FORM_Your_Personal_Details), 'Форма "Your Personal Details" отсутствует'

    def should_be_not_confirm_password(self):
        assert self.is_element_present(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR), "Регистрация прошла успешно! Пароль для подтверждения указан!"        
    
    def should_be_not_email(self):
        assert self.is_element_present(*RegisterPageLocators.EMAIL_ERROR), "Регистрация прошла успешно! Почта указано!"
    
    def should_be_not_first_name(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME_IS_REQUIRED), "Регистрация прошла успешно! Имя пользователя указано!"

    def should_be_not_last_name(self):
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME_IS_REQUIRED), "Регистрация прошла успешно! Фамилия пользователя указано!"

    def should_be_not_password(self):
        assert self.is_element_present(*RegisterPageLocators.PASSWORD_WRONG), "Регистрация прошла успешно! Пароль указан и соответствует заданному формату!"        

    def should_be_not_re_registration(self):
        assert self.is_element_present(*RegisterPageLocators.RE_REGISTRATION), 'Повторная регистрация прошла успешно! '

    def should_be_passwords_do_not_match(self):
        assert self.is_element_present(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR), "Регистрация прошла успешно! Пароли совпадают!"
        
    def should_be_successful_registration_message(self):
        result = self.browser.find_element(*RegisterPageLocators.RESULT_OF_REGISTER).text
        success_message = "Your registration completed"
        assert result == success_message, "Пользователь не зарегистрирован"        
     
    def should_be_unsuccessful_registration_message_Confirm_password_is_required(self):
        self.should_be_passwords_do_not_match()
        result = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR)
        assert result, "Регистрация прошла успешно! Пароль для подтверждения не указан!" 
    
    def should_be_unsuccessful_registration_message_Email_is_required(self):
        self.should_be_not_email()
        result = self.browser.find_element(*RegisterPageLocators.EMAIL_ERROR)
        assert result, "Регистрация прошла успешно! Почта указано"
        
    def should_be_unsuccessful_registration_message_First_name_is_required(self):
        self.should_be_not_first_name()
        result = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_IS_REQUIRED)
        assert result, "Регистрация прошла успешно! Имя пользователя указано" 
    
    def should_be_unsuccessful_registration_message_Last_name_is_required(self):
        self.should_be_not_last_name()
        result = self.browser.find_element(*RegisterPageLocators.LAST_NAME_IS_REQUIRED)
        assert result, "Регистрация прошла успешно! Фамилия пользователя указанa" 
        
    def should_be_unsuccessful_registration_message_Password_is_required(self):
        self.should_be_not_password()
        result = self.browser.find_element(*RegisterPageLocators.PASSWORD_WRONG)
        assert result, "Регистрация прошла успешно! Пароль указан!" 


    def should_be_unsuccessful_registration_message_Password_is_wrong(self):
        self.should_be_not_password()
        result = self.browser.find_element(*RegisterPageLocators.PASSWORD_WRONG)
        assert result, "Регистрация прошла успешно! Пароль соответствует заданному формату!" 


    def should_be_unsuccessful_registration_message_passwords_do_not_match(self):
        self.should_be_passwords_do_not_match()
        result = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR)
        assert result, "Регистрация прошла успешно! Пароли совпадают!"   

    def should_be_unsuccessful_registration_message_re_registration(self):
        self.should_be_not_re_registration()
        result = self.browser.find_element(*RegisterPageLocators.RE_REGISTRATION)
        assert result, "Регистрация прошла успешно!"   
        
    def should_be_unsuccessful_registration_message_Wrong_email(self):
        result = self.browser.find_element(*RegisterPageLocators.EMAIL_ERROR)
        assert result, "Регистрация прошла успешно! Почта указана верно!"   
   
        
    
        