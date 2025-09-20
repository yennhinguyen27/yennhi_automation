from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest 
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestLogin(BaseTest):
    
    @pytest.mark.smoke
    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        
        dashboardpage = DashboardPage(self.driver)
        assert dashboardpage.is_dashboard_displayed() is True
        
        sleep(3)