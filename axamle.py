import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

class NavigationTest(unittest.TestCase):
    def setUp(self):
        chrom_options = webdriver.ChromeOptions()

        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path='C:\1', chrome_options=chrom_options)
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com")

    def testBrowserNavigation(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_name("q")
        search_field.clear()
      # enter search keyword and submit
        search_field.send_keys("selenium webdriver")
        search_field.submit()
        se_wd_link = driver.find_element_by_link_text("Selenium WebDriver")
        se_wd_link.click()
        self.assertEqual("Selenium WebDriver", driver.title)
        driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("selenium webdriver - Google Search")))
        driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))
        driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
