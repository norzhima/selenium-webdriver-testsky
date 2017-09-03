import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Login(unittest.TestCase):
    print('Тестирование авторизации в ЛК')
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли тест7:")
        print()

    def test_login(self):
        self.login_button = self.driver.find_element_by_name("button")
        self.login_find = self.driver.find_element_by_name("LoginForm[email]")
        self.password = self.driver.find_element_by_name("LoginForm[password]")
        self.delay = 10
        self.login_find.send_keys("n.chagdurova@skyway.capital")
        print("Ввели логин.")
        self.password.send_keys("Xfulehjdf!1")
        print("Ввели пароль")
        self.login_button.click()
        try:
            self.assertTrue(WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='username pull-left']"))))
            self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
            print("Зашли в ЛК Norzhima Чагдурова")
            print("Тестирование авторизации на сайт https://cab-test7.skyway.capital прошло успешно.")
        except TimeoutException:
            print("-----------Загрузка страница занимает слмшком много времени!------------")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()