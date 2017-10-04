#Этот тест можно будет запускать только после того, как уберут капчу с тестовых стендов

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Login(unittest.TestCase):
    print()
    print('Тестирование авторизации в ЛК с разными условиями')
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
            self.page_auth = "Enter the system"
            self.enter_email_address = "Enter email address"
            self.enter_password = "Enter password"
            self.username_or_password_incorrect = "The username or password you entered is incorrect."
            self.email_valid = "Email is not a valid email address."
        else:
            print("Сайт SkyWay Capital открыт на ", self.search_leng.text)
            self.page_auth = "Вход в систему"
            self.enter_email_address = "Нужно ввести email"
            self.enter_password = "Нужно ввести пароль"
            self.username_or_password_incorrect = "Неверное имя пользователя или пароль. "
            self.email_valid = "Значение «Email» не является правильным email адресом."

    def autorization(self, login, passw):
        #WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='LoginForm[email]']")))
        self.login_field = self.driver.find_element_by_name("LoginForm[email]")
        self.passw_field = self.driver.find_element_by_name("LoginForm[password]")
        self.login_button = self.driver.find_element_by_name("button")
        self.login_field.send_keys(login)
        print("Ввели логин")
        self.passw_field.send_keys(passw)
        print("Ввели пароль")
        self.login_button.click()

    def autorization_field_clear(self):
        self.login_field.clear()
        self.passw_field.clear()

    def test_login(self):
        print("1) Пробуем c пустым логином и паролем зайти в ЛК:")
        self.autorization("", "")
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.enter_email_address)]")))
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.enter_password)]")))
        self.assertTrue( self.driver.page_source.__contains__(self.enter_email_address))
        print("- Выдается сообщение: ", self.enter_email_address)
        self.assertTrue(self.driver.page_source.__contains__(self.enter_password))
        print("- Выдается сообщение: ", self.enter_password)

        print("2) Пробуем ввести логин и зайти в ЛК с пустым паролем:")
        self.autorization_field_clear()
        self.autorization("n.chagdurova@skyway.capital", "")
        WebDriverWait(self.driver, self.delay).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.enter_password)]")))
        self.assertTrue(self.driver.page_source.__contains__(self.enter_password))
        print("- Выдается сообщение: ", self.enter_password)

        print('3) Пробуем ввести неверный пароль:')
        self.autorization_field_clear()
        self.autorization("n.chagdurova@skyway.capital", "nnnn")
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[@for='button']")))
        print(self.username_or_password_incorrect)
        self.assertTrue(self.driver.page_source.__contains__(self.username_or_password_incorrect))
        print('- При вводе неверного пароля выходит сообщение: ', self.username_or_password_incorrect)

        print('4) Проверка формы авторизации путем ввода логина неверного формата.')
        self.autorization_field_clear()
        self.autorization("nnnn", "nnnn")
        WebDriverWait(self.driver, self.delay).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@for='button']")))
        self.assertTrue(self.driver.page_source.__contains__(self.email_valid))
        print("- Выдается сообщение:", self.email_valid)

        print('5) Вводим верный пароль и логин:')
        self.autorization_field_clear()
        self.autorization("n.chagdurova@skyway.capital", "Xfulehjdf!1")

        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
            (By.XPATH, "//h3[@class='personal-card__name personal-card__name_verified']")))
        try:
            self.assertEqual("SkyWay Capital", self.driver.title)
            print("Зашли в Личный кабинет:", self.driver.title)
            #self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
            self.username = self.driver.find_element_by_xpath("//h3[@class='personal-card__name personal-card__name_verified']")
            self.current_url = self.driver.current_url
            if self.username.text == "Norzhima Чагдурова":
                print("пользователя: ", self.username.text)
            else:
                pass
            print("- Тестирование авторизации на сайте", self.current_url, "прошло успешно.")
        except TimeoutException:
            print("Попытка авторизации провалилась")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
