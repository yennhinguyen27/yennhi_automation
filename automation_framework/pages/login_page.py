from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest 
from base.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH,"//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit']")
        
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        

    def login(self, user_name, pass_word):
        username = self.get_element(self.USERNAME_INPUT)
        username.send_keys(user_name)
        password = self.get_element(self.PASSWORD_INPUT)
        password.send_keys(pass_word)
        self.get_element(self.LOGIN_BUTTON).click()
           
            

           