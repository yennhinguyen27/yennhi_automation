import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BaseTest:
    @pytest.fixture(scope= "class", autouse=True)
    def setup(self, request):
        options = webdriver.ChromeOptions()
        #down ve may command cau Headless lai de mo Chrome len
        options.add_argument("--headless=new")
        
        self.driver = webdriver.Chrome(options)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   
        
        request.cls.driver = self.driver
        yield
        self.driver.quit()
    # end def