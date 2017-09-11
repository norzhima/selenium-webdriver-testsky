import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .method_login import autorization, login

class Login(unittest.TestCase):
    print()
    print('Тестирование авторизации в ЛК')
    def setUp(self):
        self.delay = 10
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("SkyWay", self.driver.title)
        print()
        print("Открыли тест7:")
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='login__header-lang-title dropdown-toggle']")))
        self.search_leng = self.driver.find_element_by_xpath("//span[@class='login__header-lang-title dropdown-toggle']")
        if self.search_leng.text == "EN":
            print("Язык: Английский")
        else:
            print("Сайт SkyWay Capital открыт на ", self.search_leng.text)

    self.autorization()
    self.login()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)