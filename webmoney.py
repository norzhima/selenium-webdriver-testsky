import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


class innotrans_testing(unittest.TestCase):
    print("     ПРОВЕРКА ОСНОВНОГО ФУНКЦИОНАЛА САЙТА new.skyway.capital В БРАУЗЕРЕ CHROME(РУССКИЙ ЛК)")
    print()

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=self.options)

        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли окно авторизации:")

        self.delay = 10
        self.login_key = "n.chagdurova@skyway.capital"
        self.password_key = "Xfulehjdf!1"
        self.sum_req1 = 50

    def test_qiwi(self):
        self.login = self.driver.find_element_by_name("LoginForm[email]")
        self.login.send_keys(self.login_key)
        print("Ввели логин")
        self.password = self.driver.find_element_by_name("LoginForm[password]")
        self.password.send_keys(self.password_key)
        print("Ввели пароль")
        self.button_login = self.driver.find_element_by_id("buttonLoginSubmit")
        self.button_login.click()
        try:
            self.assertTrue(WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@class='username pull-left']"))))
        except TimeoutException:
            print("-----------Загрузка страницы после авторизации занимает слмшком много времени!------------")
        self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
        print("Зашли в ЛК Norzhima Чагдурова;")


        print()
        print('Переход в раздел "Транзакции/Пополнение счета":')

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.XPATH, "//li[@data-class='account/index']")))
        except TimeoutException:
            print('-----------Поиск раздела "Банкинг" в шапке сайта занял слишком много времени!-----------')
        self.banking = self.driver.find_element_by_xpath("//li[@data-class='account/index']")
        self.actions_banking_deposit = ActionChains(self.driver)
        self.actions_banking_deposit.move_to_element(self.banking)
        '''try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.XPATH, "//a[@href='/account/cashin']")))
        except TimeoutException:
            print('-----------Поиск раздела "Пополнить счет" в шапке сайта занял слишком много времени!-----------')'''
        print(' - Навели курсор на "Банкинг";')
        self.deposit = self.driver.find_element_by_xpath("//a[@href='/account/cashin']")
        self.actions_banking_deposit.click(self.deposit)
        self.actions_banking_deposit.perform()
        print(' - Кликнули по "Пополнению счета;"')

        print('1) Проверка пополнеия счета через Mera:')
        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "req1")))
        except TimeoutException:
            print('-----------Поиск поля для ввода суммы занял слишком много времени!-----------')
        print(' - Перешли в раздел пополнения счета;')
        self.req1 = self.driver.find_element_by_id("req1")
        self.req1.send_keys(self.sum_req1)
        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "buttonPay")))
        except TimeoutException:
            print('-----------Поиск кнопки "Пополнить" занял слишком много времени!-----------')
        print(' - Ввели в поле сумму для пополнения;')
        self.deposit_sum = self.driver.find_element_by_id("buttonPay")
        self.deposit_sum.click()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "payment-mera")))
        except TimeoutException:
            print('-----------Поиск кнопки "mera" занял слишком много времени!-----------')
        print(' - Появился список платежный систем для пополнения;')
        self.mera = self.driver.find_element_by_id("payment-mera")
        self.mera.click()


        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "mera-success")))
        except TimeoutException:
            print('-----------Поиск кнопки "Согласен" занял слишком много времени!-----------')
        print(' - Выбрали в качестве платежной системы "QIWI";')
        self.qiwi_submit = self.driver.find_element_by_id("mera-success")
        self.qiwi_submit.click()


        self.cicle = 0
        while self.cicle <48:
            self.driver.get("https://cab-test7.skyway.capital")
            print()
            print('Переход в раздел "Транзакции/Пополнение счета":')

            try:
                WebDriverWait(self.driver, self.delay).until(
                    EC.visibility_of_any_elements_located((By.XPATH, "//li[@data-class='account/index']")))
            except TimeoutException:
                print('-----------Поиск раздела "Банкинг" в шапке сайта занял слишком много времени!-----------')
            self.banking = self.driver.find_element_by_xpath("//li[@data-class='account/index']")
            self.actions_banking_deposit = ActionChains(self.driver)
            self.actions_banking_deposit.move_to_element(self.banking)
            '''try:
                WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.XPATH, "//a[@href='/account/cashin']")))
            except TimeoutException:
                print('-----------Поиск раздела "Пополнить счет" в шапке сайта занял слишком много времени!-----------')'''
            print(' - Навели курсор на "Банкинг";')
            self.deposit = self.driver.find_element_by_xpath("//a[@href='/account/cashin']")
            self.actions_banking_deposit.click(self.deposit)
            self.actions_banking_deposit.perform()
            print(' - Кликнули по "Пополнению счета;"')

            print('1) Проверка пополнеия счета через Mera:')
            try:
                WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "req1")))
            except TimeoutException:
                print('-----------Поиск поля для ввода суммы занял слишком много времени!-----------')
            print(' - Перешли в раздел пополнения счета;')
            self.req1 = self.driver.find_element_by_id("req1")
            self.req1.send_keys(self.sum_req1)
            try:
                WebDriverWait(self.driver, self.delay).until(
                    EC.visibility_of_any_elements_located((By.ID, "buttonPay")))
            except TimeoutException:
                print('-----------Поиск кнопки "Пополнить" занял слишком много времени!-----------')
            print(' - Ввели в поле сумму для пополнения;')
            self.deposit_sum = self.driver.find_element_by_id("buttonPay")
            self.deposit_sum.click()

            try:
                WebDriverWait(self.driver, self.delay).until(
                    EC.visibility_of_any_elements_located((By.ID, "payment-mera")))
            except TimeoutException:
                print('-----------Поиск кнопки "mera" занял слишком много времени!-----------')
            print(' - Появился список платежный систем для пополнения;')
            self.mera = self.driver.find_element_by_id("payment-mera")
            self.mera.click()

            try:
                WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "mera-success")))
            except TimeoutException:
                print('-----------Поиск кнопки "Согласен" занял слишком много времени!-----------')
            print(' - Выбрали в качестве платежной системы "QIWI";')
            self.qiwi_submit = self.driver.find_element_by_id("mera-success")
            self.qiwi_submit.click()
            self.cicle= self.cicle + 1

        time.sleep(5)
        '''
        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "buttonNext1")))
        except TimeoutException:
            print('----------Поиск кнопки "внимательно прочитал, принимаю правила" занял слишком много времени!--------')
        print(' - Отметили галочкой согласие с правилами перевода;')
        self.qiwi_submit_next = self.driver.find_element_by_id("buttonNext1")
        self.qiwi_submit_next.click()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "buttonNext2")))
        except TimeoutException:
            print('-----------Поиск кнопки "Перевод выполнен" занял слишком много времени!-----------')
        print(' - Нажали на кнопку "внимательно прочитал, принимаю правила";')
        self.qiwi_submit_next2 = self.driver.find_element_by_id("buttonNext2")
        self.qiwi_submit_next2.click()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='modalQiwiStep3']/div/div/div/button")))
        except TimeoutException:
            print('-----------Поиск кнопки "Закрыть" занял слишком много времени!-----------')
        print(' - Нажали на кнопку "перефод выполнен";')
        self.qiwi_close = self.driver.find_element_by_xpath("//div[@id='modalQiwiStep3']/div/div/div/button")
        self.qiwi_close.click()
        print(' Прошли все шаги для пополнения счета через QIWI со стороны ЛК.')

        time.sleep(5)'''


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()