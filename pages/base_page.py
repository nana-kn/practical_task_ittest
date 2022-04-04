from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import LoginPageLocators
from ..test_data.users import TestUser

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url    
        self.browser.implicitly_wait(timeout)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
       
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()    
    
    def go_to_register_page(self):
        register_link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        register_link.click()
    
    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self,users: TestUser):
        assert users.email == self.browser.find_element(*LoginPageLocators.USER).text, "Пользователь не авторизован"
        
    
        