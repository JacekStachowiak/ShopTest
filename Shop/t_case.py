import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import page

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.python.org/')
    
    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = 'pycon'
        main_page.click_go_to_button()
        search_results_page = page.SearchResultPage(self.driver)
        assert search.result.page.is_result_found(), 'Nie znaleziono.'
            
if __name__ == '__main__':
    unittest.main()

    