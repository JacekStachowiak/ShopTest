from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

class TestLogShop:
    
    @classmethod
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://skleptest.pl/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
           
    def test_create_account(self):
        driver = self.driver
        email = str(random.randint(0, 10000)) + 'testeroprogramowania@gmail.com'
        driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a').click()
        driver.find_element(By.ID, 'reg_email').send_keys(email)
        time.sleep(2)
        driver.find_element(By.ID, 'reg_password').send_keys('testeroprogramowania')
        driver.find_element(By.XPATH, '//input[@name="register"]').click()
        
    def test_login_in(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a').click()
        driver.find_element(By.ID, 'username').send_keys('testeroprogramowania@gmail.com')
        time.sleep(2)
        driver.find_element(By.ID, 'password').send_keys('testeroprogramowania')
        driver.find_element(By.XPATH, "//input[@name='login']").click()
        driver.quit()
    
    @classmethod
    def down(self):
        self.driver.quit()
            
    # assert str(email) in driver.find_element(By.XPATH, "//*[@id='post-8']/div/div/p/strong[1]").is_displayed()
    
