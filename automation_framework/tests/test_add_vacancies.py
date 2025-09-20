from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from base.base_test import BaseTest 
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage
from automation_framework.base.base_test import BaseTest



class TestLogin(BaseTest):
    
    def test_add_vacancies(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        
        sleep(5)
        vacanciespage = VacanciesPage(self.driver)
        vacanciespage.add_vacanies("Vacancy 01", "5")
        sleep(3)
        
        
        # vacancyname = "Vacancy 01",
        #     jobtitle = "Automaton Tester",
        #     description = "This is the description for vacancy 01",
        #     numberofposition = "5"