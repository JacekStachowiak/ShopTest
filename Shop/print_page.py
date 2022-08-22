import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.print_page_options import PrintOptions

driver = webdriver.Chrome(ChromeDriverManager().install())
print_options = PrintOptions()
print_options.page_ranges = [1,2,3]     # strony
driver.get('wydruk1.html')

base64code = driver.print_page(print_options)


