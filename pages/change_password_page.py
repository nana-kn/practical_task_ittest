from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators, ChangePasswordPageLocators
from ..test_data.users import TestUser, ChangePassword

class ChangePasswordPage(BasePage):
   
    def change_password(self, old_password, new_password, confirm_new_password):
        old_password = self.browser.find_element(*ChangePasswordPageLocators.OLD_PASSWORD).send_keys(old_password)
        new_password = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD).send_keys(new_password)
        confirm_password = self.browser.find_element(*ChangePasswordPageLocators.CONFIRM_NEW_PASSWORD).send_keys(confirm_new_password)
        button = self.browser.find_element(*ChangePasswordPageLocators.BUTTON_CHANGE).click()
    

    def login_user(self, email, password):
        fild_email = self.browser.find_element(*BasePageLocators.EMAIL)
        fild_email.send_keys(email)
        fild_password = self.browser.find_element(*BasePageLocators.PASSWORD)
        fild_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_TO_LOGIN)
        button.click()


    def should_be_button_change_password(self):
        assert self.is_element_present(*ChangePasswordPageLocators.BUTTON_CHANGE), "Кнопка 'Change password' отсутствует!"


    def should_be_elements_for_change_password(self):
        self.should_be_field_old_password()
        self.should_be_field_new_password()
        self.should_be_field_confirm_new_password()
        self.should_be_button_change_password()


    def should_be_field_new_password(self):
        assert self.is_element_present(*ChangePasswordPageLocators.NEW_PASSWORD), "Поле 'New password' отсутствует!"


    def should_be_field_old_password(self):
        assert self.is_element_present(*ChangePasswordPageLocators.OLD_PASSWORD), "Поле 'Old password' отсутствует!"


    def should_be_field_confirm_new_password(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CONFIRM_NEW_PASSWORD), "Поле 'Confirm password' отсутствует!"


    def should_be_message_confirm_password_is_required(self):
        assert self.is_element_present(*ChangePasswordPageLocators.PASSWORDS_DO_NOT_MATCH), "Confirm password указан!"
    
    
    def should_be_message_new_password_and_confirm_password_do_not_match(self):
        assert self.is_element_present(*ChangePasswordPageLocators.PASSWORDS_DO_NOT_MATCH), "New password и Confirm password совпадают!"

    
    def should_be_message_new_password_is_required(self):
        assert self.is_element_present(*ChangePasswordPageLocators.WRONG_NEW_PASSWORD), "New password указан!"
    
    
    def should_be_message_old_password_is_wrong(self):
        assert self.is_element_present(*ChangePasswordPageLocators.WRONG_OLD_PASSWORD), "Old password указан верно!"


    def should_be_message_old_password_is_required(self):
        assert self.is_element_present(*ChangePasswordPageLocators.OLD_PASSWORD_IS_REQUIRED), "Old password указан!"

    
    def should_be_message_wrong_format_new_password(self):
        assert self.is_element_present(*ChangePasswordPageLocators.WRONG_NEW_PASSWORD), "New password соответствует требованиям формата!"


    def should_be_successful_change_password_message(self):
        result = self.browser.find_element(*ChangePasswordPageLocators.RESULT_OF_CHANGE_PASSWORD).text
        success_message = "Password was changed"
        assert result == success_message, "Пароль не изменен!"


    def should_be_unsuccessful_change_confirm_password_is_required(self):
        self.should_be_message_confirm_password_is_required()
        result = self.browser.find_element(*ChangePasswordPageLocators.PASSWORDS_DO_NOT_MATCH).text
        assert result, "Пароль изменен! Confirm password указан!"

    
    def should_be_unsuccessful_change_new_password_is_required(self):
        self.should_be_message_new_password_is_required()
        result = self.browser.find_element(*ChangePasswordPageLocators.WRONG_NEW_PASSWORD).text
        assert result, "Пароль изменен! New password указан!"

    
    def should_be_unsuccessful_change_old_password_is_wrong(self):
        self.should_be_message_old_password_is_wrong()
        result = self.browser.find_element(*ChangePasswordPageLocators.WRONG_OLD_PASSWORD).text
        assert result, "Пароль изменен! Old password указан верно!"
    

    def should_be_unsuccessful_change_old_password_is_required(self):
        self.should_be_message_old_password_is_required()
        result = self.browser.find_element(*ChangePasswordPageLocators.OLD_PASSWORD_IS_REQUIRED).text
        assert result, "Пароль изменен! Old password указан!"


    def should_be_unsuccessful_change_new_password_and_confirm_password_do_not_match(self):
        self.should_be_message_new_password_and_confirm_password_do_not_match()
        result = self.browser.find_element(*ChangePasswordPageLocators.PASSWORDS_DO_NOT_MATCH).text
        assert result, "Пароль изменен! New password и Confirm password совпадают!"


    def should_be_unsuccessful_change_wrong_format_new_password(self):
        self.should_be_message_wrong_format_new_password()
        result = self.browser.find_element(*ChangePasswordPageLocators.WRONG_NEW_PASSWORD).text
        assert result, "Пароль изменен! New password соответствует требованиям формата!"
    
    

        
