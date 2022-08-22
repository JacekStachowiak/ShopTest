from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
class TestLogShop:
    
    @classmethod
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://skleptest.pl/')
        self.driver.maximize_window()
                
    def test_order(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a').click()
        driver.find_element(By.ID, 'username').send_keys('testeroprogramowania@gmail.com')
        driver.implicitly_wait(10)
        driver.find_element(By.ID, 'password').send_keys('testeroprogramowania')
        driver.find_element(By.XPATH, "//input[@name='login']").click()
        driver.save_screenshot('zrzut_1.png')
        source = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
        source.screenshot('zrzut_3.png')
        target = driver.find_element(By.ID, 'menu-item-127')
        webdriver.ActionChains(driver).move_to_element(source).move_to_element(target).click().perform()
        time.sleep(2)
        #zdjecie = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div[2]/div/ul/li[4]/a[1]/img').click()
        zdjecie = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div[2]/div/ul/li[4]/a[1]/img')
        zdjecie.screenshot('zrzut_4.png')
        zdjecie.click()
        time.sleep(2)
        zoom = driver.find_element(By.CLASS_NAME, 'woocommerce-product-gallery__trigger')
        webdriver.ActionChains(driver).move_to_element(zoom).click().perform()
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(zoom).key_down(Keys.ESCAPE).perform()
        driver.find_element(By.LINK_TEXT, 'Trends').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div[2]/div/ul/li[4]/a[2]').click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'top-cart').click()
        
        
    @classmethod
    def down(self):
        self.driver.quit()          
              