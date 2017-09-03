import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class Login(unittest.TestCase):
    print('Тестирование авторизации в ЛК')
    def setUp(self):
        self.driver=webdriver.Firefox()

    def test_login(self):
        self.driver.set_page_load_timeout(10)
        self.momondo = self.driver.get("https://cab-test4.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли тест4:")
        print()
        self.leng_checkout = self.driver.find_element_by_xpath("//span[@class='login__header-lang-title dropdown-toggle']")
        self.leng_checkout.click()
        self.leng_checkout_ru = self.driver.find_element_by_xpath("//a[@class='multilanguage-set']")
        self.leng_checkout_ru.click()
        time.sleep(2)

        print("1) Пробуем без ввода логина и пароля зайти в ЛК:")
        self.login_button = self.driver.find_element_by_name("button")
        self.login_button.click()
        time.sleep(2)
        self.assertTrue( self.driver.page_source.__contains__("Нужно ввести email"))
        print('- Выдается сообщение: "нужно ввести логин" и ')
        self.assertTrue(self.driver.page_source.__contains__("Нужно ввести пароль"))
        print('- Выдается сообщение: "нужно ввести пароль"')

        print("2) Пробуем ввести логин и зайти в ЛК без пароля:")
        self.login_find = self.driver.find_element_by_name("LoginForm[email]")
        self.login_find.send_keys("n.chagdurova@skyway.capital")
        self.login_button.click()
        self.assertTrue(self.driver.page_source.__contains__("Нужно ввести пароль"))
        print('- Выдается сообщение: "нужно ввести пароль"')

        print('3) Пробуем ввести неверный пароль:')
        self.password = self.driver.find_element_by_name("LoginForm[password]")
        self.password.send_keys("absxcsdmfcd")
        #self.password.send_keys(Keys.RETURN)
        self.login_button.click()
        time.sleep(2)
        self.assertTrue(self.driver.page_source.__contains__("Неверное имя пользователя или пароль."))
        print('- При вводе неверного пароля выходит сообщение: "Неверное имя пользователя или пароль."')

        print('4) Проверка формы авторизации путем ввода логина неверного формата.')
        self.login_find.clear()
        self.password.clear()
        self.login_find.send_keys("nnnnnn")
        #self.login_find.send_keys(Keys.RETURN)
        self.password.send_keys("ererer")
        #self.password.send_keys(Keys.RETURN)
        self.login_button.click()
        time.sleep(2)
        self.assertTrue(self.driver.page_source.__contains__("Значение «Email» не является правильным email адресом."))
        print('Выдается сообщение "Значение «Email» не является правильным email адресом."')

        print('5) Вводим верный пароль и логин:')
        self.login_find.clear()
        self.password.clear()
        self.login_find.send_keys("n.chagdurova@skyway.capital")
        #self.login_find.send_keys(Keys.RETURN)
        self.password.send_keys("aa1bb2cc")
        #self.password.send_keys(Keys.RETURN)
        self.login_button.click()
        time.sleep(2)
        self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
        print('Зашли в ЛК под логином Norzhima Чагдурова')
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()