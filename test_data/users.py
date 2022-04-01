from dataclasses import dataclass
import time
from faker import Faker

faker = Faker()

@dataclass(frozen=True)
class  TestUser:
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str

@dataclass(frozen=True)
class ChangePassword:
    password: str
    confirm_password: str


first_name = faker.first_name()
last_name = faker.last_name()
email = faker.email()
password = faker.password()
confirm_password = faker.password()

User_Successful = TestUser(first_name, last_name, email, password, password)
User_Wrong = TestUser(first_name, last_name, email, password, confirm_password)
User_Name = TestUser('', last_name, email, password, password)
User_Sername = TestUser(first_name, '', email, password, password)
User_Email = TestUser(first_name, last_name, '', password, password)
User_Wrong_Email = TestUser(first_name, last_name, 'wrong', password, password)
User_Wrong_Email2 = TestUser(first_name, last_name, 'wrong@mail', password, password)
User_Password = TestUser(first_name, last_name, email, '', '')
User_Wrong_Password = TestUser(first_name, last_name, email, '123', '123')
User_Confirm_Password = TestUser(first_name, last_name, email, password, '')
User_Empty = TestUser('', '', '', '', '')

ChangePassword_Successful = ChangePassword(password, password)
ChangePassword_Wrong = ChangePassword(password, confirm_password)
ChangePassword_Wrong_Format = ChangePassword('123', '123')
ChangePassword_Confirm_Password = ChangePassword(password, '')
ChangePassword_Password = ChangePassword('', '')




