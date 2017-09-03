# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Test7Auth(unittest.TestCase):
    print("Тестирование кнопок соц.сетей на Mozilla Firefox в английском ЛК")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли форму авторизации сайта cab-test7.skyway.capital")

    def test_auth_in_test7(self):
        self.login__form_email = self.driver.find_element_by_name("LoginForm[email]")
        self.login__form_email.send_keys("n.chagdurova@skyway.capital")
        self.login__form_email.send_keys(Keys.RETURN)
        print("Ввели логин")
        self.login__form_password = self.driver.find_element_by_name("LoginForm[password]")
        #self.login__form_password.send_keys("Xfulehjd")
        #self.login__form_password.send_keys(Keys.RETURN)
        #self.mes = self.driver.find_element_by_xpath("/html/body/div/div/div/form/span")
        #self.assertIn("The username or password you entered is incorrect.", self.mes)
        #self.login__form_password.clear()
        self.login__form_password.send_keys("Xfulehjdf!1")
        self.login__form_password.send_keys(Keys.RETURN)
        print("Ввели пароль")
        self.assertIn("Sky Way", self.driver.title)
        print("Переход в ЛК")
        #self.cabinet = self.driver.find_element_by_link_text("Go to Partner Cabinet")
        #self.assertTrue("Go to Partner Cabinet", self.cabinet)
        #self.cabinet.click()
        #self.cabinet.implicitly_wait(5)
        time.sleep(3)

        print("Проверка кнопок социальных сетей:")
        self.facebook = self.driver.find_element_by_xpath("//img[@alt='Фейсбук']")
        #print(self.facebook.location)
        #print(self.facebook.size)
        time.sleep(2)
        self.facebook.click()
        time.sleep(2)
        self.assertIn("SkyWay Capital England public group | Facebook", self.driver.title)
        print(' - Проверили кнопку "Фейсбук"')
        time.sleep(3)
        self.driver.execute_script("window.history.go(-3)")
        time.sleep(3)
        self.assertIn("Sky Way", self.driver.title)
        print(' - После проверки кнопки "Фейсбук" вернулись обратно в ЛК')

        self.viber = self.driver.find_element_by_xpath("//img[@alt='Вайбер чат']")
        time.sleep(2)
        self.viber.click()
        time.sleep(3)
        self.assertIn("Sky Way Capital (EN)", self.driver.title)
        print(' - Проверили кнопку Вайбер чата')
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        self.assertIn("Sky Way", self.driver.title)
        print(' - После проверки кнопки "Вайбер чат" вернулись обратно в ЛК')

        self.youtube = self.driver.find_element_by_xpath("//img[@alt='Ютюб']")
        time.sleep(2)
        self.youtube.click()
        time.sleep(3)
        self.assertIn("➨ SkyWay Capital - the Investment Company of String Transport of the Future - YouTube", self.driver.title)
        print(' - Проверили кнопку "Ютюб"')
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(4)
        self.assertIn("Sky Way", self.driver.title)
        print(' - После проверки кнопки "Ютюб" вернулись обратно в ЛК')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()