import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def autorization(self, login, passw):
    # WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='LoginForm[email]']")))
    self.login_field = self.driver.find_element_by_name("LoginForm[email]")
    self.passw_field = self.driver.find_element_by_name("LoginForm[password]")
    self.login_button = self.driver.find_element_by_name("button")
    self.login_field.send_keys(login)
    print("1) Ввели логин.")
    self.passw_field.send_keys(passw)
    print("2) Ввели пароль")
    self.login_button.click()


def login(self):
    print('Вводим логин и пароль:')
    self.autorization("n.chagdurova@skyway.capital", "Xfulehjdf!1")
    WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
        (By.XPATH, "//h3[@class='personal-card__name personal-card__name_verified']")))
    try:
        self.assertEqual("SkyWay Capital", self.driver.title)
        print("Зашли в Личный кабинет:", self.driver.title)
        # self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
        self.username = self.driver.find_element_by_xpath(
            "//h3[@class='personal-card__name personal-card__name_verified']")
        self.current_url = self.driver.current_url
        if self.username.text == "Norzhima Чагдурова":
            print("пользователя: ", self.username.text)
        else:
            pass
        print("- Тестирование авторизации на сайте", self.current_url, "прошло успешно.")
    except TimeoutException:
        print("Попытка авторизации провалилась")