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
from selenium.webdriver.common.action_chains import ActionChains


class LkswcTest(unittest.TestCase):

    def setUp(self):
        if lkswc_config.default_browser is "Chrome":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(chrome_options=self.options)
        else:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        self.driver.get(lkswc_config.main_url)
        self.assertEqual("SkyWay", self.driver.title)
        self.language_search = self.expect_visibility(lkswc_config.language_search_xpath)
        if self.language_search.text == "EN":
            self.language_search.click()
            self.switching_to_ru = self.expect_visibility(lkswc_config.switching_to_ru_xpath).click()
        self.expect_visibility(lkswc_config.enter_the_systeme)
        '''включить после того, как вернут дебаг-панель на тест7
        try:
            #self.expect_visibility(lkswc_config.debug_toolbar_xpath)
            WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.ID, lkswc_config.debug_toolbar_xpath)))
            self.expect_visibility(lkswc_config.debug_minimize_xpath).click()
            #WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.debug_minimize_xpath)))
            #self.debug_minimize = self.driver.find_element_by_xpath(lkswc_config.debug_minimize_xpath)
            #self.debug_minimize.click()
        except TimeoutException:
            pass'''

    def tearDown(self):
        self.driver.quit()

    def test_check_packet_tree(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.packet_tree = self.expect_visibility(lkswc_config.packet_tree_xpath)
        self.expect_visibility(lkswc_config.main_balance_xpath)
        self.main_balance_before = self.driver.find_elements_by_xpath(lkswc_config.main_balance_xpath)
        self.main_balance_before_replace = self.main_balance_before[0].text.replace(' ', '')
        self.main_balance_before_replace_int = int(self.main_balance_before_replace[:-4])
        self.package_header = self.driver.find_elements_by_xpath(lkswc_config.package_header_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", self.package_header[1])
        self.packet_tree.click()
        self.pay_account = self.expect_visibility(lkswc_config.pay_account_xpath)
        self.get_url_450 = self.driver.current_url
        self.assertEqual(lkswc_config.main_url + "/investment/programs?packet=450", self.get_url_450)
        self.go_to_element(lkswc_config.total_price_xpath)
        self.pay_account.click()
        self.expect_visibility(lkswc_config.main_account_xpath)
        self.total_price = self.expect_visibility(lkswc_config.total_price_xpath)
        self.total_price_int = int(self.total_price.text.replace(' ', ''))
        self.input_one = self.expect_visibility(lkswc_config.input_one_xpath)
        self.sum_packet = 5000
        self.assertEqual(self.total_price_int, self.sum_packet)
        self.input_one.send_keys(self.sum_packet)
        self.expect_visibility(lkswc_config.checkout_tree_xpath).click()
        self.expect_visibility(lkswc_config.progress_start).click()
        self.expect_visibility("//span[contains(text(), lkswc_config.you_select_shares)]")
        self.get_url_pay_check = self.driver.current_url
        self.assertEqual(lkswc_config.main_url+"/investment/pay-check", self.get_url_pay_check)
        self.go_to_element(lkswc_config.username_verif_data_xpath)
        self.expect_visibility(lkswc_config.checkbox_icon_xpath).click()
        self.expect_visibility(lkswc_config.button_buy_xpath).click()
        try:
            self.expect_visibility(lkswc_config.username_verif_data_xpath)
            self.expect_visibility(lkswc_config.requirement_xpath)
            self.sign = self.expect_visibility(lkswc_config.sign_xpath)
            time.sleep(3) #временное решение
            self.go_to_element(lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
            self.sign.click()
        except TimeoutException:
            pass
        self.expect_visibility("//h2[contains(text(), lkswc_config.section_my_certificates)]")
        self.assertTrue(self.driver.page_source.__contains__(lkswc_config.section_my_certificates))
        self.get_url_portfolio = self.driver.current_url
        self.assertEqual(lkswc_config.main_url + "/investment/portfolio", self.get_url_portfolio)
        self.main_balance_after = self.expect_visibility(lkswc_config.main_balance_xpath)
        self.main_balance_after_replace = self.main_balance_after.text.replace(' ', '')
        self.main_balance_after_replace_int = int(self.main_balance_after_replace[:-4])
        self.assertEqual(self.main_balance_before_replace_int-self.sum_packet, self.main_balance_after_replace_int)
        return True


    #Здесь в дальнейшем планируется получать список активных платежных систем и на основе этих данных проводить тесты ПС

    def test_cashin_pm(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_perfect_money_xpath)
        self.expect_visibility(lkswc_config.wait_checkout_pm).click()
        self.get_url_perfect_money = self.driver.current_url
        self.assertIn(lkswc_config.site_perfect_money, self.get_url_perfect_money)

    def test_cashin_mera(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_mera_xpath)
        self.expect_visibility(lkswc_config.popup_checkbox_accept_xpath).click()
        self.expect_visibility(lkswc_config.mera_success_xpath).click()
        self.expect_visibility(lkswc_config.wait_checkout_mera)
        self.get_url_mera = self.driver.current_url
        self.assertIn(lkswc_config.site_mera, self.get_url_mera)

    def test_cashin_exmo(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_exmo_xpath)
        self.expect_visibility(lkswc_config.wait_checkout_advcash)
        self.get_url_exmo = self.driver.current_url
        self.assertEqual(lkswc_config.site_advcash, self.get_url_exmo)

    def test_cashin_ecoin(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_ecoin_xpath)
        self.expect_visibility(lkswc_config.wait_checkout_advcash)
        self.get_url_ecoin = self.driver.current_url
        self.assertEqual(lkswc_config.site_advcash, self.get_url_ecoin)

    def test_cashin_impex_mastercard(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_mc_impex_xpath)
        self.checkout_impex_trading(lkswc_config.instruction_mc_impex_xpath, lkswc_config.popup_accept_mc_impex_xpath, lkswc_config.mc_impex_success_xpath)

    def test_cashin_fasapay(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_fasapay_xpath)
        self.expect_visibility(lkswc_config.wait_checkout_fasapay)
        self.get_url_fasa_pay = self.driver.current_url
        self.assertIn(lkswc_config.site_fasapay, self.get_url_fasa_pay)

    def test_cashin_impex_impaya_world(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_impaya_world_xpath)
        self.checkout_impex_trading(lkswc_config.instruction_impaya_world_xpath, lkswc_config.popup_accept_impaya_world_xpath, lkswc_config.impaya_world_success_xpath)

    def test_cashin_impex_visa(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_impexvisa_xpath)
        self.checkout_impex_trading(lkswc_config.instruction_impexvisa_xpath, lkswc_config.popup_accept_impexvisa_xpath, lkswc_config.impexvisa_success_xpath)

    def test_cashin_impex_orange(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_impexorange_xpath)
        self.checkout_impex_trading(lkswc_config.instruction_impexorange_xpath, lkswc_config.popup_accept_impexorange_xpath, lkswc_config.impexorange_success_xpath)

    def test_cashin_impex_epay(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_impexepay_xpath, element=lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.checkout_impex_trading(lkswc_config.instruction_impexepay_xpath, lkswc_config.popup_accept_impexepay_xpath, lkswc_config.impexepay_success_xpath)

    def test_cashin_web_swift_small(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_small, lkswc_config.ps_web_swift_xpath, element=lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.expect_visibility(lkswc_config.popup_web_swift_small_xpath)
        self.assertTrue(self.driver.page_source.__contains__("Банковский перевод"))
        self.assertTrue(self.driver.page_source.__contains__("www.advcash.com"))

    def test_cashin_web_swift_large(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_large, lkswc_config.ps_web_swift_xpath, element=lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.popup_swift_alert()
        self.payment_swift()

    def test_cashin_megapolis(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_large, lkswc_config.ps_megapolis_xpath, element=lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.popup_swift_alert()
        self.payment_swift()

    def test_cashin_tt_swift(self):
        self.autorization(lkswc_private_data.login, lkswc_private_data.password)
        self.deposit_account(lkswc_config.sum_cashin_large, lkswc_config.tt_swift_xpath, element=lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.payment_swift(select_currency="yes")

    def expect_visibility(self, path):
        WebDriverWait(self.driver, lkswc_config.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        return self.driver.find_element_by_xpath(path)

    def autorization(self, login, passw):
        self.expect_visibility(lkswc_config.login_field_xpath).send_keys(login)
        self.expect_visibility(lkswc_config.passw_field_xpath).send_keys(passw)
        self.expect_visibility(lkswc_config.login_button_xpath).click()
        self.expect_visibility(lkswc_config.username_verif_data_xpath)
        self.assertEqual("SkyWay Capital", self.driver.title)
        self.assertTrue(self.driver.page_source.__contains__(lkswc_private_data.username))

    def deposit_account(self, sum_cashin, ps_xpath, element=lkswc_config.deposit_button_xpath, elem_position=lkswc_config.elem_position_top):
        self.expect_visibility(lkswc_config.banking_xpath).click()
        self.expect_visibility(lkswc_config.deposit_account_xpath).click()
        self.get_url_cashin = self.driver.current_url
        self.assertEqual(lkswc_config.check_url_cashin, self.get_url_cashin)
        self.go_to_element(lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.expect_visibility(lkswc_config.field_cashin_xpath).send_keys(sum_cashin)
        self.expect_visibility(lkswc_config.deposit_button_xpath).click()
        self.ps = self.expect_visibility(ps_xpath)
        self.go_to_element(element, elem_position)
        self.ps.click()

    def go_to_element(self, element, elem_position=lkswc_config.elem_position_top):
        self.expect_visibility(element)
        self.go_element = self.expect_visibility(element)
        if elem_position == lkswc_config.elem_position_top:
            self.driver.execute_script("arguments[0].scrollIntoView(true)", self.go_element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.go_element)

    def checkout_impex_trading(self, instruction, popup_accept, success):
        self.expect_visibility(instruction)
        self.assertTrue(self.driver.page_source.__contains__("Инструкция по оплате"))
        self.expect_visibility(popup_accept).click()
        self.expect_visibility(success).click()
        self.expect_visibility(lkswc_config.wait_checkout_trading_impex)
        self.get_url_trading_impex = self.driver.current_url
        self.assertEqual(lkswc_config.site_trading_impex, self.get_url_trading_impex)

    def popup_swift_alert(self):
        self.expect_visibility(lkswc_config.popup_swift_alert_xpath)
        self.assertTrue(self.driver.page_source.__contains__(" Счет действителен в течении 7 дней."))
        self.expect_visibility(lkswc_config.popup_accept_swift_alert_xpath).click()
        self.expect_visibility(lkswc_config.swift_alert_success_xpath).click()

    def payment_swift(self, select_currency="no", val=lkswc_config.choose_val_ru):
        self.expect_visibility(lkswc_config.choose_the_curr_for_payment)
        self.go_to_element(lkswc_config.choose_the_curr_for_payment)
        if select_currency == "yes":
            self.expect_visibility(val).click()
        self.expect_visibility(lkswc_config.download_from_verification_swift_xpath).click()
        self.expect_visibility(lkswc_config.accept_swift_xpath)
        self.accept_swift = self.driver.find_element_by_xpath(lkswc_config.accept_swift_xpath)
        self.go_to_element(lkswc_config.footer_xpath, elem_position=lkswc_config.elem_position_bottom)
        self.accept_swift.click()
        self.expect_visibility(lkswc_config.submit_swift_xpath).click()
        time.sleep(10)
        self.expect_visibility(lkswc_config.wait_checkout_swift_page)
        self.get_url_swift = self.driver.current_url
        self.assertEqual(lkswc_config.main_url + "/swift/", self.get_url_swift)

if __name__ == "__main__":
    unittest.main(verbosity=2)





