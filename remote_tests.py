import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class innotrans_testing(unittest.TestCase):
    print('     ПРОВЕРКА ПРИОБРЕТЕНИЯ ПАКЕТА "ИМЕННОЕ ДЕРЕВО 5000" в браузере Chrome(Руский ЛК).')
    print()
    print('Тестирование авторизации в ЛК')


    def setUp(self):
        # self.listhub = ('http://10.0.3.227:4444/wd/hub', 'http://31.xxx.96.183:4444/wd/hub')
        # self.hub = str(random.sample(self.listhub, 1)[0])
        self.hub = 'http://10.0.3.231:4444/wd/hub'
        self.driver = webdriver.Remote(
            command_executor=self.hub,
            desired_capabilities={
                "seleniumProtocol": "WebDriver",
                "browserName": "chrome",
                "maxInstances": "2",  # on hub "docker-compose scale chrome=3"
                "maxSession": "6",
                "version": "any",
                "applicationName": "",
                "platform": "LINUX",
                "chrome.switches": '--proxy-server=kakawka:ZbhZVEF1@31.xxx.96.183:65534'
            }
        )
        self.delay = 10
        self.success = True
        return self.success
        self.driver.implicitly_wait(1200)
        self.driver.set_window_size(1400, 1000)
        print
        bcolors.OKGREEN + "logs in " + self.hub + "/session/" + self.wd.session_id + "/log" + bcolors.ENDC
        return self.driver
        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("SkyWay", self.driver.title)
        print()
        print("Открыли тест7:")
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//span[@class='login__header-lang-title dropdown-toggle']")))
        self.search_leng = self.driver.find_element_by_xpath(
            "//span[@class='login__header-lang-title dropdown-toggle']")
        if self.search_leng.text == "EN":
            print("Язык: Английский")
        else:
            print("Сайт SkyWay Capital открыт на ", self.search_leng.text)

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

    def test_login(self):
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

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)