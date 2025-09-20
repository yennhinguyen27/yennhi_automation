from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class VacanciesPage(BasePage):
    RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    VACANCIES = (By.XPATH, "//a[text()='Vacancies']")
    ADD_VACANCIES_BTN = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    VACANCY_NAME =  (By.XPATH, "//label[text()='Vacancy Name']/../following-sibling::div//input")
    JOB_TITLE = (By.XPATH, "//i[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder= 'Type description here']")
    NUMBER_OF_POSITION = (By.XPATH, "//label[text()='Number of Positions']/following-sibling::input")
    HIRING_MANAGER = (By.XPATH, "//input[@placeholder='Type for hints...']")
    HIRING_MANAGER_LOGINED = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    SAVE_BTN = (By.XPATH, "//button[@type= 'submit']")
    DROP_DOWN = (By.XPATH, "//div[@class='oxd-select-wrapper']")   
    DROP_DOWN_OPTION = (By.XPATH, "//div[@role='listbox']//span[text()='Automation Tester']")
    
    
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
    
    def get_text_hiring_manager(self):
        return self.get_element(self.HIRING_MANAGER_LOGINED).get_attribute("value")
    
    #def add_vacanies(self, vacancy_name, job_title, description, number_of_position):
    def enter_vacancy_name(self, vacancy_name):
        vacancyname = self.get_element(self.VACANCY_NAME)
        vacancyname.send_keys(vacancy_name)
        
    def select_text_from_dropdown(self):
        self.get_element(self.DROP_DOWN).click()
        sleep(3)
        self.get_element(self.DROP_DOWN_OPTION).click()
        sleep(3)
    
        
        
        
    def enter_description(self, description):
        description_field = self.get_element(self.DESCRIPTION)
        description_field.send_keys(description)
    
    def enter_number_of_position(self, number_of_position):
        numberofposition = self.get_element(self.NUMBER_OF_POSITION)
        numberofposition.send_keys(number_of_position)
    
    def add_vacanies(self, vacancy_name, number_of_position):
        self.get_element(self.RECRUITMENT).click()
        self.get_element(self.VACANCIES).click()
        self.get_element(self.ADD_VACANCIES_BTN).click()
        self.enter_vacancy_name(vacancy_name)
        self.select_text_from_dropdown()
        
        sleep(5)
        
        self.enter_description("This is the description for " + vacancy_name)
        self.get_element(self.HIRING_MANAGER).send_keys(self.get_text_hiring_manager())
        self.enter_number_of_position(number_of_position)
        self.get_element(self.SAVE_BTN).click()
        
        
        
        
        # vacancyname = self.get_element(self.VACANCY_NAME)
        # vacancyname.send_keys(vacancy_name)
        
        # jobtitle = self.select_text_from_dropdown(self.JOB_TITLE, job_title)
        
        # description = self.get_element(self.DESCRIPTION)
        # description.send_keys(description)
        
        # hiringmanager = self.get_element(self.HIRING_MANAGER)
        # hiringmanager.send_keys(self.get_text_hiring_manager())
        
        # numberofposition = self.get_element(self.NUMBER_OF_POSITION)
        # numberofposition.send_keys(number_of_position)
        sleep(3)
        
        
        
           
           
            

           