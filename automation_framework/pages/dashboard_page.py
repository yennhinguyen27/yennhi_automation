from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class DashboardPage(BasePage):
    DASHBOARD = (By.XPATH,"//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed (self):
            dashboard = self.get_element(self.DASHBOARD)
            return dashboard.is_displayed()
         
            
