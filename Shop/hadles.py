import timeit
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

start = timeit.default_timer()
chrome_options = Options()
chrome_options.add_argument('--headles')    # otwórz w trybie headles
chrome_options.add_argument('--window-size=1920x1080')  # ustawiam rozdzielczość

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://skleptest.pl/')
# driver.maximize_window()
             
def test_order_2():
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
        
stop = timeit.default_timer()
print('CZas wykonania: ', stop - start)
                                                 
            
              