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
        self.assertTrue(self.driver.page_source.__contains__("Вход в систему"))
        print("Открыли тест7:")
        print()

    def autorization(self, login, passw):
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='LoginForm[email]']")))
        self.login_field = self.driver.find_element_by_name("LoginForm[email]")
        self.passw_field = self.driver.find_element_by_name("LoginForm[password]")
        self.login_button = self.driver.find_element_by_name("button")
        self.login_field.send_keys(login)
        print("Ввели логин.")
        self.passw_field.send_keys(passw)
        print("Ввели пароль")
        self.login_button.click()

    def test_login(self):
        self.delay = 10
        self.autorization("n.chagdurova@skyway.capital", "Xfulehjdf!1")
        try:
            self.assertTrue(WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='personal-card__name personal-card__name_verified']"))))
            self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
            print("Зашли в ЛК Norzhima Чагдурова")
            print("Тестирование авторизации на сайт https://cab-test7.skyway.capital прошло успешно.")
        except TimeoutException:
            print("-----------Загрузка страница занимает слмшком много времени!------------")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
