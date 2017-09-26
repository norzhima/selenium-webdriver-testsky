# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import lkswc_config
import lkswc_private_data

class LkswcTest(unittest.TestCase):

    def setUp(self):

        if lkswc_config.default_browser is "Chrome":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(chrome_options=self.options)
        else:
            self.driver = webdriver.Firefox()
        self.driver.get(lkswc_config.main_url)
        self.assertIn("SkyWay", self.driver.title)
        WebDriverWait(self.driver, lkswc_config.delay).until(
            EC.presence_of_all_elements_located((By.XPATH, lkswc_config.language_search_xpath)))
        self.language_search = self.driver.find_element_by_xpath(lkswc_config.language_search_xpath)
        if self.language_search.text == "EN":
            self.language_search.click()
            WebDriverWait(self.driver, lkswc_config.delay).until(
                EC.visibility_of_element_located((By.XPATH, lkswc_config.switching_to_ru_xpath)))
            self.switching_to_ru = self.driver.find_element_by_xpath(lkswc_config.switching_to_ru_xpath).click()
        self.assertTrue(self.driver.page_source.__contains__("Вход в систему"))
        try:
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.ID, lkswc_config.debug_toolbar_xpath)))
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.debug_minimize_xpath)))
            self.debug_minimize = self.driver.find_element_by_xpath(lkswc_config.debug_minimize_xpath)
            self.debug_minimize.click()
        except TimeoutException:
            pass

    def tearDown(self):
        self.driver.quit()

    def test_authorization(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)

    def check_packet_tree(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.packet_tree_xpath)))
        #self.invest_programs = self.driver.find_element_by_xpath("//h3[@class='cabinet__title']")
        self.packet_tree = self.driver.find_element_by_xpath(lkswc_config.packet_tree_xpath)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.main_balance_xpath)))
        self.main_balance_before = self.driver.find_element_by_xpath(lkswc_config.main_balance_xpath)
        self.main_balance_before_replace = self.main_balance_before.text.replace(' ', '')
        self.main_balance_before_replace_int = int(self.main_balance_before_replace[:-4])
        self.packet_tree.click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.pay_account_xpath)))
        self.get_url_450 = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/programs?packet=450", self.get_url_450)
        self.pay_account = self.driver.find_element_by_xpath(lkswc_config.pay_account_xpath)
        self.pay_account.click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.main_account_xpath)))
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.total_price_xpath)))
        self.total_price = self.driver.find_element_by_xpath(lkswc_config.total_price_xpath)
        self.total_price_int = int(self.total_price.text.replace(' ', ''))
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.input_one_xpath)))
        self.input_one = self.driver.find_element_by_xpath(lkswc_config.input_one_xpath)
        self.sum_packet = 5000
        self.assertTrue(self.total_price_int, self.sum_packet)
        self.input_one.send_keys(self.sum_packet)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.checkout_tree_xpath))).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.progress_start))).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), lkswc_config.you_select_shares)]")))
        self.get_url_pay_check = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/pay-check", self.get_url_pay_check)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.checkbox_icon_xpath))).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located((By.XPATH, lkswc_config.button_buy_xpath))).click()
        try:
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located((By.XPATH, lkswc_config.verif_data_xpath)))
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located((By.XPATH, lkswc_config.requirement_xpath)))
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located((By.XPATH, lkswc_config.sign_xpath))).click()
        except TimeoutException:
            pass
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), lkswc_config.section_my_certificates)]")))
        self.assertTrue(self.driver.page_source.__contains__(lkswc_config.section_my_certificates))
        self.get_url_portfolio = self.driver.current_url
        self.assertTrue("https://cab-test7.skyway.capital/investment/portfolio", self.get_url_portfolio)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.main_balance_xpath)))
        self.main_balance_after = self.driver.find_element_by_xpath(lkswc_config.main_balance_xpath)
        self.main_balance_after_replace = self.main_balance_after.text.replace(' ', '')
        self.main_balance_after_replace_int = int(self.main_balance_after_replace[:-4])
        self.assertTrue(self.main_balance_before_replace_int-self.sum_packet, self.main_balance_after_replace_int)
        return True

    def test_cashin_pm(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.banking_xpath))).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.deposit_account))).click()
        self.get_url_cashin = self.driver.current_url
        self.assertTrue(lkswc_config.check_url_cashin, self.get_url_cashin)
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.field_cashin_xpath)))
        self.req1 = self.driver.find_element_by_xpath(lkswc_config.field_cashin_xpath)
        self.req1.send_keys(lkswc_config.sum_cashin)
        time.sleep(5)

        '''try:
            WebDriverWait(self.driver, self.delay).until(EC.visibility_of_any_elements_located((By.ID, "buttonPay")))
        except TimeoutException:
            print('-----------Поиск кнопки "Пополнить" занял слишком много времени!-----------')
        print(' - Ввели в поле сумму для пополнения;')
        self.deposit_sum = self.driver.find_element_by_id("buttonPay")
        self.deposit_sum.click()'''

    def autorization(self, login, passw):
        self.login_field = self.driver.find_element_by_xpath(lkswc_config.login_field_xpath).send_keys(login)
        self.passw_field = self.driver.find_element_by_xpath(lkswc_config.passw_field_xpath).send_keys(passw)
        self.login_button = self.driver.find_element_by_xpath(lkswc_config.login_button_xpath).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located(
            (By.XPATH, lkswc_config.username_xpath)))
        self.assertEqual("SkyWay Capital", self.driver.title)
        self.assertTrue(self.driver.page_source.__contains__(lkswc_private_data.username))
        return True

if __name__ == "__main__":
    unittest.main(verbosity=2)