from selenium.webdriver.common.by import By

class BasePageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")


class LoginPageLocators():
    BUTTON_TO_LOGIN = (By.CSS_SELECTOR, ".button-1.login-button")
    FORM_Returning_Customer = (By.XPATH, '//strong[text() = "Returning Customer"]')
    USER = (By.CSS_SELECTOR, ".account")
    LINK = "http://demowebshop.tricentis.com/login"
    MESSAGE_ERROR = (By.CSS_SELECTOR, '.validation-summary-errors span')
        
  
class RegisterPageLocators():
    BUTTON_TO_REGISTER = (By.ID, "register-button")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    CONFIRM_PASSWORD_ERROR = (By.XPATH, "//span[@for = 'ConfirmPassword']")
    EMAIL_ERROR = (By.XPATH, "//span[@for = 'Email']")
    FIRST_NAME = (By.ID, "FirstName")
    FIRST_NAME_IS_REQUIRED = (By.XPATH, "//span[@for = 'FirstName']")    
    FORM_Your_Personal_Details = (By.XPATH, '//strong[text() = "Your Personal Details"]')
    FORM_Your_Password = (By.XPATH, '//strong[text() = "Your Password"]') 
    GENDER = (By.ID, "gender-female")
    LAST_NAME = (By.ID, "LastName")
    LAST_NAME_IS_REQUIRED = (By.XPATH, "//span[@for = 'LastName']")
    LINK = "http://demowebshop.tricentis.com/register"
    PASSWORD_IS_REQUIRED = (By.XPATH, "//span[@for = 'Password']")
    RESULT_OF_REGISTER = (By.CLASS_NAME, "result")
    RE_REGISTRATION = (By.CSS_SELECTOR, '.validation-summary-errors ul li')
    
     
    
