
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
        
     
    def select_text_from_dropdown (self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(xpath)).click()
        select = Select(element)
        select.select_by_visible_text(value)
    
    
    def select_by_java_script(self, xpath):
        self.driver.execute_script("arguments[0].click();", xpath)
    
    
     
        
        
                   
    
    





    
     
        
        
                   
    
    




