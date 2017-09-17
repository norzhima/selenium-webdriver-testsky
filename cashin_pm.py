import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class tree_testing(unittest.TestCase):

    print('     ПРОВЕРКА ПРИОБРЕТЕНИЯ ПАКЕТА "ИМЕННОЕ ДЕРЕВО 5000" в браузере Chrome.')
    print()

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
            self.section_my_certificates = "My certificates"

        else:
            print("Сайт SkyWay Capital открыт на ", self.search_leng.text)
            self.main_accounts = "Основной: "
            self.you_select_shares = "Вы собираетесь приобрести следующее количество акций: "
            self.section_my_certificates = "Мои сертификаты"
        try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "yii-debug-toolbar")))
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='yii-debug-toolbar-toggler']")))
            self.debug_minimize = self.driver.find_element_by_xpath("//span[@class='yii-debug-toolbar-toggler']")
            self.debug_minimize.click()
        except TimeoutException:
            print("На тестовом стенде нет дебаг-панели.")

    def autorization(self, login, passw):
        self.login_field = self.driver.find_element_by_name("LoginForm[email]")
        self.passw_field = self.driver.find_element_by_name("LoginForm[password]")
        self.login_button = self.driver.find_element_by_name("button")
        self.login_field.send_keys(login)
        print("1) Ввели логин.")
        self.passw_field.send_keys(passw)
        print("2) Ввели пароль")
        self.login_button.click()

    def login(self):
        print('АВТОРИЗАЦИЯ В ЛИЧНОМ КАБИНЕТЕ:')
        print('Вводим логин и пароль:')
        self.autorization("n.chagdurova@skyway.capital", "Xfulehjdf!1")
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
            (By.XPATH, "//h3[@class='personal-card__name personal-card__name_verified']")))
        self.current_url = self.driver.current_url
        try:
            self.assertTrue("SkyWay Capital", self.driver.title)
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

    def check_packet_tree(self):
        self.check_packet = '"Именное дерево 5 000"'
        print('ПОКУПКА ПАКЕТА', self.check_packet, 'ЧЕРЕЗ ОСНОВНОЙ СЧЕТ:')
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/investment/programs?packet=384']")))
        self.invest_programs = self.driver.find_element_by_xpath("//h3[@class='cabinet__title']")
        self.tree_one = self.driver.find_element_by_xpath("//a[@href='/investment/programs?packet=384']")
        #self.driver.execute_script("return arguments[0].scrollIntoView();", self.invest_programs)
        self.tree_one.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='pay-w-acc']")))
        self.get_url_384 = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/programs?packet=384", self.get_url_384)
        print(" - Перешли на страницу", self.get_url_384, 'для выбора способа оплаты пакета', self.check_packet)
        self.pay_acc = self.driver.find_element_by_xpath("//label[@for='pay-w-acc']")
        self.total = self.driver.find_element_by_xpath("//h3[@class='paying__title']")
        #self.driver.execute_script("return arguments[0].scrollIntoView();", self.total)
        self.pay_acc.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.main_accounts)]")))
        self.assertTrue(self.driver.page_source.__contains__(self.main_accounts))
        print(" - Выбрали оплату с внутренних кошельков")
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.ID, "input1")))
        self.input1 = self.driver.find_element_by_id("input1")
        self.sum_packet = 5000
        self.input1.send_keys(self.sum_packet)
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='paying__panel-acc-btn']/input")))
        print(" - Ввели сумму", self.sum_packet,"в поле для основного счета")
        self.checkout_tree = self.driver.find_element_by_xpath("//div[@class='paying__panel-acc-btn']/input")
        #time.sleep(10)
        self.checkout_tree.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='progressStart']")))
        self.progress_start = self.driver.find_element_by_xpath("//button[@id='progressStart']")
        self.progress_start.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), self.you_select_shares)]")))
        print(" - Подтвердили инвестицию во всплывающем окне")
        self.get_url_pay_check = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/pay-check", self.get_url_pay_check)
        print(' - и перешли на страницу', self.get_url_pay_check)
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='swc-elements_checkbox-icon']")))
        self.agree = self.driver.find_element_by_xpath("//span[@class='swc-elements_checkbox-icon']")
        self.agree.click()
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "buy-btn")))
        print(' - Нажали галочку для принятия условий договора конвертируемого займа;')
        self.buy_btn = self.driver.find_element_by_id("buy-btn")
        self.buy_btn.click()
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, "swc-canvas")))
        print(' - После этого нажали на появившуюся кнопку "Инвестировать";')
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='personal-card__name personal-card__name_verified']")))
            self.verif_data = self.driver.find_element_by_xpath(
                "//h3[@class='personal-card__name personal-card__name_verified']")
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.NAME, "sign")))
            self.sign = self.driver.find_element_by_name("sign")
            self.sign.click()
            print(' - Нажали кнопку "Подписать" в открывшемся требовании')
        except TimeoutException:
            print("Пользователь не верифицирован")
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), self.section_my_certificates)]")))
        self.assertTrue(self.driver.page_source.__contains__(self.section_my_certificates))
        self.get_url_portfolio = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/portfolio", self.get_url_portfolio)
        print(' - После покупки пакета "" перешли на страницу', self.get_url_portfolio, 'в раздел "Мои сертификаты".')
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='heading-logo-link']")))
        self.checkout_main_section = self.driver.find_element_by_xpath("//a[@class='heading-logo-link']")
        self.checkout_main_section.click()
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='back-to-news']")))
        self.get_url_main_section = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/", self.get_url_main_section)
        print(' - После проверки покупки пакета', self.check_packet, 'c основного счета перешли на главную страницу сайта')
        print('++++++++++Покупка пакета', self.check_packet, ' с основного счета прошла успешно!+++++++++++++++')

    def test_tree(self):
        self.login()
        #Ниже будет проводиться проверка наличия баннеров на сайте
        print()
        self.check_packet_tree()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
