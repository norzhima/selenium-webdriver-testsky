import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class innotrans_firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        self.driver.get("https://cab-test4.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли окно авторизации:")
        self.delay = 10

    def test_innotrans(self):
        self.login = self.driver.find_element_by_name("LoginForm[email]")
        self.login.send_keys("n.chagdurova@skyway.capital")
        print("Ввели логин")
        self.password = self.driver.find_element_by_name("LoginForm[password]")
        self.password.send_keys("aa1bb2cc")
        print("Ввели пароль")
        self.button_login = self.driver.find_element_by_id("buttonLoginSubmit")
        self.button_login.click()
        try:
            self.assertTrue(WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='username pull-left']"))))
        except TimeoutException:
            print("-----------Загрузка страницы после авторизации занимает слмшком много времени!------------")
        self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
        print("Зашли в ЛК Norzhima Чагдурова;")

        print()
        print("1) Покупка через основной счет:")
        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/investment/programs?packet=390']")))
        except TimeoutException:
            print('-----------Поиск кнопки "Выбрать" у пакета innotrans занял слишком много времени!-----------')
        self.innotrans = self.driver.find_element_by_xpath("//a[@href='/investment/programs?packet=390']")
        self.innotrans.click()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pay-w-acc']")))
        except TimeoutException:
            print('-----------Поиск элемента "Оплатить с внутренних кошельков" поля "Основной" занял слишком много времени!-----------')
        self.pay_acc = self.driver.find_element_by_xpath("//input[@id='pay-w-acc']")
        print(" - Выбрали пакет innotrans")
        '''self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.pay_acc)
        self.actions.click(self.pay_acc)
        self.actions.perform()'''
        self.pay_acc.click()
        print(" - Выбрали оплату с внутренних кошельков")

        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "input5")))
        except TimeoutException:
            print('-----------Поиск поля "Основной" занял слишком много времени!-----------')
        self.input5 = self.driver.find_element_by_id("input5")
        self.input5.send_keys("1000")
        print(" - Ввели сумму 1000$ в поле для основного счета")

        self.checkout_innotrans = self.driver.find_element_by_xpath(
            "//input[@class='btn pay-btn do-pay-button col-xs-12']")
        self.checkout_innotrans.click()

        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@id='progressStart']")))
        except TimeoutException:
            print('-----------Поиск кнопки "да" для подтверждения инвестиции занял слишком много времени!-----------')
        self.progress_start = self.driver.find_element_by_xpath("//button[@id='progressStart']")
        self.progress_start.click()
        print(" - Подтвердили инвестицию во всплывающем окне")

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "agree")))
        except TimeoutException:
            print('-----------Поиск элемента для подтверждения инвестиции занял слишком много времени!-----------')
        self.agree = self.driver.find_element_by_id("agree")
        self.agree.click()
        print(' - Нажали галочку для принятия условий договора конвертируемого займа;')

        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "buy-btn")))
        except TimeoutException:
            print(
                '-----------Поиск кнопки "Инвестировать" для подтверждения инвестиции занял слишком много времени!-----------')
        self.buy_btn = self.driver.find_element_by_id("buy-btn")
        self.buy_btn.click()
        print(' - После этого нажали на кнопку "Инвестировать";')

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.NAME, "sign")))
        except TimeoutException:
            print('-----------Поиск кнопки "Подписать" для подтверждения инвестиции занял слишком много времени!-----------')
        self.sign = self.driver.find_element_by_name("sign")
        self.sign.click()
        print(' - Нажали кнопку "Подписать" в открывшемся требовании')
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='col-xs-12']")))
        except TimeoutException:
            print('-----------Поиск надписи "Мои сертификаты" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("My certificates"))
        print(' - Убедились, что после покупки пакета "INNOTRANS" перешли на страницу "Мои сертификаты".')

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='navbar-brand']")))
        except TimeoutException:
            print('-----------Поиск логотипа компании для перехода на главную страницу ЛК занял слишком много времени!-----------')
        self.skyway_capital = self.driver.find_element_by_xpath("//a[@class='navbar-brand']")
        self.skyway_capital.click()
        time.sleep(10)

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='back-to-news']")))
        except TimeoutException:
            print('-----------Поиск кнопки "Все инвестиционнае обновления" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("All investments"))
        print("После проверки покупки пакета innotrans через основной счет перешли на главную страницу сайта")
        print('++++++++++Покупка пакета "INNOTRANS" с основного счета прошла успешно!+++++++++++++++')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
