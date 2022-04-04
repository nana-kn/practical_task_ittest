from selenium.webdriver.common.by import By

class BasePageLocators():
    LINK = "http://demowebshop.tricentis.com/"
    EMAIL = (By.ID, "Email")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    PASSWORD = (By.ID, "Password")
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")

class ChangePasswordPageLocators():
    BUTTON_CHANGE = (By.XPATH, "//input[@value = 'Change password']")
    CONFIRM_NEW_PASSWORD = (By.ID, "ConfirmNewPassword")
    LINK = "http://demowebshop.tricentis.com/customer/changepassword"
    NEW_PASSWORD = (By.ID, "NewPassword")
    OLD_PASSWORD = (By.ID, "OldPassword")
    OLD_PASSWORD_IS_REQUIRED = (By.XPATH, "//span[@for =  'OldPassword']")
    PASSWORDS_DO_NOT_MATCH = (By.XPATH, "//span[@for = 'ConfirmNewPassword']")
    RESULT_OF_CHANGE_PASSWORD = (By.XPATH, "//div[@class = 'result']")
    WRONG_NEW_PASSWORD = (By.XPATH, "//span[@for = 'NewPassword']")
    WRONG_OLD_PASSWORD = (By.XPATH, "//div[@class = 'validation-summary-errors']/ul/li")
    

class LoginPageLocators():
    BUTTON_TO_LOGIN = (By.CSS_SELECTOR, ".button-1.login-button")
    FORM_Returning_Customer = (By.XPATH, '//strong[text() = "Returning Customer"]')
    LINK = "http://demowebshop.tricentis.com/login"
    MESSAGE_ERROR = (By.CSS_SELECTOR, '.validation-summary-errors span')
    USER = (By.CSS_SELECTOR, " .header-links li .account")
    EMAIL_IS_WRONG = (By.CSS_SELECTOR, ".field-validation-error span")
    REMEMBER = (By.ID, "RememberMe")
        
  
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
    PASSWORD_WRONG = (By.XPATH, "//span[@for = 'Password']")
    RESULT_OF_REGISTER = (By.CLASS_NAME, "result")
    RE_REGISTRATION = (By.CSS_SELECTOR, '.validation-summary-errors ul li')
    
     
    
