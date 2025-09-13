
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath))
        return element
    

    def send_keys(self, xpath, value):
        element = self.get_element(xpath)     
        element.send_keys(value)
        
     
    # def dropdown (self, xpath, value):
    #     element = self.get_element(xpath)
    #     select = Select(element)
    #     return select.select_by_value(value)
        
    # def wait_for(self, condition, locator):
    #     wait = WebDriverWait (self.driver, 10)
    #     return wait.until(condition(locator))
    
     
        
        
                   
    
    




