from .base_page import BasePage
from .locators import RegisterPageLocators
import time

class RegisterPage(BasePage):
     
    def register_new_user(self, first_name, last_name, email, password, confirm_password):
        fild_gender = self.browser.find_element(*RegisterPageLocators.GENDER)
        fild_gender.click()
        fild_first_name = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        fild_first_name.send_keys(first_name)
        fild_last_name = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        fild_last_name.send_keys(last_name)
        fild_email = self.browser.find_element(*RegisterPageLocators.EMAIL)
        fild_email.send_keys(email)
        fild_password = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        fild_password.send_keys(password)
        fild_password_confirm = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        fild_password_confirm.send_keys(confirm_password)
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
        assert self.is_element_present(*RegisterPageLocators.PASSWORD_IS_REQUIRED), "Регистрация прошла успешно! Пароль указан!"        

    def should_be_passwords_do_not_match(self):
        assert self.is_element_present(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR), "Регистрация прошла успешно! Пароли совпадают!"

    def should_be_successful_registration_message(self):
        result = self.browser.find_element(*RegisterPageLocators.RESULT_OF_REGISTER).text
        success_message = "Your registration completed"
        assert result == success_message, "Пользователь не зарегистрирован"        
     
    def should_be_unsuccessful_registration_message_Confirm_password_is_required(self):
        self.should_be_not_confirm_password()
        result = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR).text
        message = "Password is required."
        assert result == message, "Регистрация прошла успешно! Пароль для подтверждения не указан!" 
    
    def should_be_unsuccessful_registration_message_Email_is_required(self):
        self.should_be_not_email()
        result = self.browser.find_element(*RegisterPageLocators.EMAIL_ERROR).text
        message = "Email is required."
        assert result == message, "Регистрация прошла успешно! Почта указано"
        
    def should_be_unsuccessful_registration_message_First_name_is_required(self):
        self.should_be_not_first_name()
        result = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_IS_REQUIRED).text
        message = "First name is required."
        assert result == message, "Регистрация прошла успешно! Имя пользователя указано" 
    
    def should_be_unsuccessful_registration_message_Last_name_is_required(self):
        self.should_be_not_last_name()
        result = self.browser.find_element(*RegisterPageLocators.LAST_NAME_IS_REQUIRED).text
        message = "Last name is required."
        assert result == message, "Регистрация прошла успешно! Фамилия пользователя указано" 
        
    def should_be_unsuccessful_registration_message_Password_is_required(self):
        self.should_be_not_password()
        result = self.browser.find_element(*RegisterPageLocators.PASSWORD_IS_REQUIRED).text
        message = "Password is required."
        assert result == message, "Регистрация прошла успешно! Пароль указан!" 

    def should_be_unsuccessful_registration_message_passwords_do_not_match(self):
        self.should_be_passwords_do_not_match()
        result = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_ERROR).text
        message = "The password and confirmation password do not match."
        assert result == message, "Регистрация прошла успешно! Пароли совпадают!"   
        
    def should_be_unsuccessful_registration_message_Wrong_email(self):
        self.should_be_wrong_email()
        result = self.browser.find_element(*RegisterPageLocators.EMAIL_ERROR).text
        message = "Wrong email"
        assert result == message, "Регистрация прошла успешно! Почта указана верно!"   
        
    def should_be_wrong_email(self):
        assert self.is_element_present(*RegisterPageLocators.EMAIL_ERROR), "Регистрация прошла успешно! Почта указана верно!"   
           

    
        