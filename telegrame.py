# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test7Auth(unittest.TestCase):

    print("Тестирование кнопок соц.сетей на Google Chrome в русском ЛК")
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=self.options)
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
        # self.login__form_password.send_keys("Xfulehjd")
        # self.login__form_password.send_keys(Keys.RETURN)
        # self.mes = self.driver.find_element_by_xpath("/html/body/div/div/div/form/span")
        # self.assertIn("The username or password you entered is incorrect.", self.mes)
        # self.login__form_password.clear()
        self.login__form_password.send_keys("Xfulehjdf!1")
        self.login__form_password.send_keys(Keys.RETURN)
        print("Ввели пароль")
        self.assertIn("Sky Way", self.driver.title)
        print("Переход в ЛК")
        # self.cabinet = self.driver.find_element_by_link_text("Go to Partner Cabinet")
        # self.assertTrue("Go to Partner Cabinet", self.cabinet)
        # self.cabinet.click()
        # self.cabinet.implicitly_wait(5)
        time.sleep(3)

        print("Проверка кнопки 9 - Телеграм:")
        self.telegram = self.driver.find_element_by_xpath("//img[@alt='Телеграм']")
        # time.sleep(2)
        self.telegram.click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Telegram: Contact @skywaycapital")))
        #self.assertIn("Telegram: Contact @skywaycapital", self.driver.title)
        print(' - Проверили кнопку "Телеграм"')
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.execute_script("window.history.go(-2)")
        self.driver.implicitly_wait(30)
        time.sleep(5)
        self.assertIn("Sky Way", self.driver.title)
        print(' - После проверки кнопки "Телеграм" вернулись обратно в ЛК')

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()