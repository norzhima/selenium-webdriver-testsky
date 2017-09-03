import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


class all_testing(unittest.TestCase):
    print("     ПРОВЕРКА ОСНОВНОГО ФУНКЦИОНАЛА САЙТА new.skyway.capital В БРАУЗЕРЕ CHROME(РУССКИЙ ЛК)")
    print()

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=self.options)

        self.driver.get("https://cab-test4.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли окно авторизации:")
        self.delay = 10
        self.login_key = "n.chagdurova@skyway.capital"
        self.password_key = "Xfulehjdf!1"
        self.sum_req1 = 50

    def test_all_main(self):
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
                EC.presence_of_element_located((By.XPATH, "//h3[@class='username pull-left']"))))
        except TimeoutException:
            print("-----------Загрузка страницы после авторизации занимает слмшком много времени!------------")
        self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
        print("Успешно авторизовались в ЛК Norzhima Чагдурова;")

        print()
        print('1) Проверка покупки пакета "INNOTRANS" через основной счет:')
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//a[@class='innotrans-buy']")))
        except TimeoutException:
            print('-----------Поиск кнопки "Выбрать" у пакета innotrans занял слишком много времени!-----------')
        self.innotrans = self.driver.find_element_by_xpath("//a[@class='innotrans-buy']")
        self.innotrans.click()

        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.XPATH, "//label[@for='pay-w-acc']")))
        except TimeoutException:
            print(
                '-----------Поиск элемента "Оплатить с внутренних кошельков" поля "Основной" занял слишком много времени!-----------')
        self.pay_acc = self.driver.find_element_by_xpath("//label[@for='pay-w-acc']")
        print(" - Выбрали пакет innotrans")
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.pay_acc)
        self.actions.click(self.pay_acc)
        self.actions.perform()
        print(" - Выбрали оплату с внутренних кошельков")

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "input5")))
        except TimeoutException:
            print('-----------Поиск поля "Основной" занял слишком много времени!-----------')
        self.input5 = self.driver.find_element_by_id("input5")
        self.input5.send_keys("1000")
        print(" - Ввели сумму 1000$ в поле для основного счета")

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.XPATH, "//input[@class='btn pay-btn do-pay-button col-xs-12")))
        except TimeoutException:
            print('-----------Поиск кнопки "Оформить" занял слишком много времени!-----------')
        self.checkout_innotrans = self.driver.find_element_by_xpath("//input[@class='btn pay-btn do-pay-button col-xs-12']")
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
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "agree")))
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
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//span[@class='pull-right']")))
            self.rec_sign = self.driver.find_element_by_xpath("//span[@class='pull-right']")
            try:
                WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, "sign")))
            except TimeoutException:
                print(
                    '-----------Поиск кнопки "Подписать" для подтверждения инвестиции занял слишком много времени!-----------')
            self.sign = self.driver.find_element_by_name("sign")
            self.sign.click()
            print(' - Нажали кнопку "Подписать" в открывшемся требовании')
        except:
            print("Не верифицирован. Требование не подписываем")

        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, "//h2[@class='col-xs-12']")))
        except TimeoutException:
            print('-----------Поиск надписи "Мои сертификаты" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("Мои сертификаты"))
        print(' - Убедились, что после покупки пакета "INNOTRANS" перешли на страницу "Мои сертификаты".')

        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@class='navbar-brand']")))
        except TimeoutException:
            print(
                '-----------Поиск логотипа компании для перехода на главную страницу ЛК занял слишком много времени!-----------')
        self.skyway_capital = self.driver.find_element_by_xpath("//a[@class='navbar-brand']")
        self.skyway_capital.click()
        time.sleep(10)

        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@class='back-to-news']")))
        except TimeoutException:
            print('-----------Поиск кнопки "Все инвестиционнае предложения" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("Все инвестиционные предложения"))
        print(" - После проверки покупки пакета innotrans c основного счета перешли на главную страницу сайта")
        print('++++++++++Покупка пакета "INNOTRANS" с основного счета прошла успешно!+++++++++++++++')

        print()
        print('Переход в раздел "ТРАНЗАКЦИИ/ПОПОЛНЕНИЕ СЧЕТА":')

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

        print('2) Проверка пополнеия счета через QIWI:')
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
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "payment-qiwi")))
        except TimeoutException:
            print('-----------Поиск кнопки "QIWI" занял слишком много времени!-----------')
        print(' - Появился список платежный систем для пополнения;')
        self.deposit_qiwi = self.driver.find_element_by_id("payment-qiwi")
        self.deposit_qiwi.click()

        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "buttonSubmit201610201534")))
        except TimeoutException:
            print('-----------Поиск кнопки "Согласен" занял слишком много времени!-----------')
        print(' - Выбрали в качестве платежной системы "QIWI";')
        self.qiwi_submit = self.driver.find_element_by_id("buttonSubmit201610201534")
        self.qiwi_submit.click()

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
        print('++++++++++Прошли все шаги для пополнения счета через QIWI со стороны ЛК.+++++++++++++++')



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
