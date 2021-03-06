from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
     
    def login_user(self, email, password):
        fild_email = self.browser.find_element(*BasePageLocators.EMAIL)
        fild_email.send_keys(email)
        fild_password = self.browser.find_element(*BasePageLocators.PASSWORD)
        fild_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_TO_LOGIN)
        button.click()

    '''
    def login_user_remeber(self, email, password):
        fild_email = self.browser.find_element(*BasePageLocators.EMAIL)
        fild_email.send_keys(email)
        fild_password = self.browser.find_element(*BasePageLocators.PASSWORD)
        fild_password.send_keys(password)
        check_box = self.browser.find_element(*LoginPageLocators.REMEMBER)
        check_box.click()
        button = self.browser.find_element(*LoginPageLocators.BUTTON_TO_LOGIN)
        button.click()
    '''
    
    def should_be_button_for_login(self):   
        assert self.is_element_present(*LoginPageLocators.BUTTON_TO_LOGIN), 'Кнопка "Log in" отсутствует' 
    
    def should_be_elements_for_login(self):
        self.should_be_button_for_login()
        self.should_be_form_Returning_Customer()

    def should_be_form_Returning_Customer(self):   
        assert self.is_element_present(*LoginPageLocators.FORM_Returning_Customer), 'Форма "Returning Customer" отсутствует' 

    def should_be_unsuccessful_message(self):
        message_error = self.is_element_present(*LoginPageLocators.MESSAGE_ERROR)
        assert message_error, "Пользователь авторизован!"
    
    def should_be_unsuccessful_login(self):
        self.should_be_unsuccessful_message()
        result = self.browser.find_element(*LoginPageLocators.MESSAGE_ERROR)
        assert result, "Пользователь авторизован!"


    def should_be_unsuccessful_message_email_is_wrong(self):
        message_error = self.is_element_present(*LoginPageLocators.EMAIL_IS_WRONG)
        assert message_error, "Пользователь авторизован!"

    def should_be_unsuccessful_login_email_is_wrong(self):
        self.should_be_unsuccessful_message_email_is_wrong()
        result = self.browser.find_element(*LoginPageLocators.EMAIL_IS_WRONG)
        assert result, "Пользователь авторизован! Email указан верно!"