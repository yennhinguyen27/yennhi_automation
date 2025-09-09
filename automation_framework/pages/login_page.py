from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest 

class LoginPage(BaseTest):
    USERNAME_INPUT = (By.XPATH,"//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit']")
        
    def __init__(self, driver):
        self.driver = driver

    def test_login (self):
            username = self.driver.find_element(*LoginPage.USERNAME_INPUT)
            password = self.driver.find_element(*LoginPage.PASSWORD_INPUT)
            username.send_keys('Admin')
            password.send_keys('admin123')

            sleep(2)
            btnlogin = self.driver.find_element(*LoginPage.LOGIN_BUTTON)
            
            btnlogin.click()
            sleep(5)  # import time