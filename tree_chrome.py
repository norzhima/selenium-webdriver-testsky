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
    print('     ПРОВЕРКА ПРИОБРЕТЕНИЯ ПАКЕТА "ИМЕННОЕ ДЕРЕВО 5000" в браузере Chrome(Руский ЛК).')
    print()
    print('Тестирование авторизации в ЛК')
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
            self.main_accounts = "Main: "
            self.you_select_shares = " You are going to select the following number of shares : "

        else:
            print("Сайт SkyWay Capital открыт на ", self.search_leng.text)
            self.main_accounts = "Основной: "
            self.you_select_shares = "Вы собираетесь приобрести следующее количество акций: "

    def autorization(self, login, passw):
        #WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='LoginForm[email]']")))
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
        self.current_url = self.driver.current_url
        try:
            self.assertEqual("SkyWay Capital", self.driver.title)
            print("Зашли в Личный кабинет:", self.driver.title)
            #self.assertTrue(self.driver.page_source.__contains__("Norzhima Чагдурова"))
            self.username = self.driver.find_element_by_xpath("//h3[@class='personal-card__name personal-card__name_verified']")
            if self.username.text == "Norzhima Чагдурова":
                print("пользователя: ", self.username.text)
            else:
                pass
            print("- Авторизация на сайте", self.current_url, "прошла успешно.")
        except TimeoutException:
            print("Попытка авторизации провалилась")

    def test_tree(self):
        self.login()
        #Ниже будет проводиться проверка наличия баннеров на сайте

        print()
        print("1) Покупка через основной счет:")
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/investment/programs?packet=384']")))
        self.tree_one = self.driver.find_element_by_xpath("//a[@href='/investment/programs?packet=384']")
        self.tree_one.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='pay-w-acc']")))
        self.get_url_384 = self.driver.current_url
        self.assertIn("https://cab-test7.skyway.capital/investment/programs?packet=384", self.get_url_384)
        self.pay_acc = self.driver.find_element_by_xpath("//label[@for='pay-w-acc']")
        print(" - Перешли на страницу", self.get_url_384, 'для выбора способа оплаты пакета "Именное дерево 5000"')
        
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.pay_acc)
        self.actions.click(self.pay_acc)
        self.actions.perform()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.main_accounts)]")))
        self.assertTrue(self.driver.page_source.__contains__(self.main_accounts))
        print(" - Выбрали оплату с внутренних кошельков")
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "input1")))
        self.input1 = self.driver.find_element_by_id("input1")
        self.sum_packet = 5000
        self.input1.send_keys(self.sum_packet)
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//input[@class='swc-btn do-pay-button']")))
        print(" - Ввели сумму", self.sum_packet,"в поле для основного счета")
        self.checkout_innotrans = self.driver.find_element_by_xpath("//input[@class='swc-btn do-pay-button']")
        self.checkout_innotrans.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='progressStart']")))
        self.progress_start = self.driver.find_element_by_xpath("//button[@id='progressStart']")
        self.progress_start.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.you_select_shares)]")))
        print(" - Подтвердили инвестицию во всплывающем окне")
        self.get_url_pay_check = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/pay-check", self.get_url_pay_check)
        print('и перешли на страницу', self.get_url_pay_check)
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "agree")))
        self.agree = self.driver.find_element_by_id("agree")
        self.agree.click()
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "buy-btn")))
        print(' - Нажали галочку для принятия условий договора конвертируемого займа;')
        self.buy_btn = self.driver.find_element_by_id("buy-btn")
        self.buy_btn.click()
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "swc-canvas")))
        print(' - После этого нажали на появившуюся кнопку "Инвестировать";')

        self.verif_data = self.driver.find_element_by_xpath("//a[@href='/personal']")

        if self.verif_data == "верифицирован":
            try:
                WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, "sign")))
            except TimeoutException:
                print(
                    '-----------Поиск кнопки "Подписать" для подтверждения инвестиции занял слишком много времени!-----------')
            self.sign = self.driver.find_element_by_name("sign")
            self.sign.click()
            print(' - Нажали кнопку "Подписать" в открывшемся требовании')

        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='col-xs-12']")))
        except TimeoutException:
            print('-----------Поиск надписи "Мои сертификаты" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("Мои сертификаты"))
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
            print('-----------Поиск кнопки "Все инвестиционнае предложения" занял слишком много времени!-----------')
        self.assertTrue(self.driver.page_source.__contains__("Все инвестиционные предложения"))
        print(" - После проверки покупки пакета innotrans c основного счета перешли на главную страницу сайта")
        print('++++++++++Покупка пакета "INNOTRANS" с основного счета прошла успешно!+++++++++++++++')



        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
