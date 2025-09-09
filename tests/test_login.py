from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest 

class TestLogin(BaseTest):
    
    def test_login(self):
            username = self.driver.find_element(By.XPATH,"//input[@name='username']")
            password = self.driver.find_element(By.XPATH,"//input[@name='password']")
            username.send_keys('Admin')
            password.send_keys('admin123')

            sleep(2)
            btnlogin = self.driver.find_element(By.XPATH,"//button[@type='submit']")
            
            btnlogin.click()
            sleep(5)  # import time
           
        