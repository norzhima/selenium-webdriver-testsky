# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as TE
import lk_conf
import lk_priv_data
import lk_method
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import datetime
import inspect
import autoit
import sys
import platform


class LkswcTest(unittest.TestCase):
    def setUp(self):
        if lk_conf.default_browser is "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = False
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        self.find = lk_method.Find(self.driver)
        self.pay = lk_method.Pay(self.driver)
        self.driver.get(lk_priv_data.main_url)
        self.assertEqual(lk_conf.short_company_name, self.driver.title)
        self.change_language()
        self.debug()

    def tearDown(self):
        self.driver.quit()

    def test_cashin_pm(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_perfect_money_id) == True:
            self.find.element_by_xpath(lk_conf.wait_checkout_pm_xpath).click()
            self.assertIn(lk_conf.site_perfect_money, self.driver.current_url)

    def test_cashin_mera(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mera_id) == True:
            self.find.element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    @unittest.skip("Платежная система mera_qiwi работает также как и mera.")
    def test_cashin_mera_qiwi(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mera_qiwi_id) == True:
            self.find.element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    @unittest.skip("Платежная система mera_euroset работает также как и mera.")
    def test_cashin_mera_euroset(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mera_euroset_id) == True:
            self.find.element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    def test_cashin_advcash_exmo(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_exmo_id) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система ecoin работает также как и exmo.")
    def test_cashin_advcash_ecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_ecoin_id) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система advcash работает также как и exmo.")
    def test_cashin_advcash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_id) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система payeer работает также как и exmo.")
    def test_cashin_advcash_payeer(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_payeer_id) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система advcash-swift работает также как и exmo.")
    def test_cashin_advcash_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_swift_id) == True:
            self.checkout_advcash()

    def test_cashin_impex_mastercard(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_mc_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_mc_impex_xpath,
                                        lk_conf.popup_accept_mc_impex_xpath, lk_conf.mc_impex_success_id)

    def test_cashin_fasapay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_fasapay_id) == True:
            self.find.element_by_xpath(lk_conf.wait_checkout_fasapay_xpath)
            self.assertIn(lk_conf.site_fasapay, self.driver.current_url)

    @unittest.skip("Платежная система impaya_world выключена.")
    def test_cashin_impex_impaya_world(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_impaya_world_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_impaya_world_xpath, lk_conf.popup_accept_impaya_world_xpath,
                                        lk_conf.impaya_world_success_id)

    def test_cashin_impex_visa(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_visa_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexvisa_xpath,
                                        lk_conf.popup_accept_impexvisa_xpath, lk_conf.impexvisa_success_id)

    def test_cashin_impex_orange(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_orange_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexorange_xpath,
                                        lk_conf.popup_accept_impexorange_xpath, lk_conf.impexorange_success_id)

    @unittest.skip("Проверка платежной системы impex_payboutique пропущена.")
    def test_cashin_impex_payboutique(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_payboutique_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexpayboutique_xpath,
                                        lk_conf.popup_accept_impexpayboutique_xpath, lk_conf.impexpayboutique_success_id)

    def test_cashin_webmoney(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_webmoney_id) == True:
            self.find.element_by_xpath(lk_conf.popup_webmoney_xpath)

    def test_cashin_bitcoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_bitcoin_id) == True:
            self.find.element_by_xpath(lk_conf.popup_bitcoin_xpath)

    @unittest.skip("Платежная система epay выключена.")
    def test_cashin_impex_epay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impex_epay_id) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexepay_xpath,
                                        lk_conf.popup_accept_impexepay_xpath,
                                        lk_conf.impexepay_success_id)

    #@unittest.skip("Платежная система cryptonator пропущена")
    def test_cashin_cryptonator(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_bitcoin работает также как и cryptonator.")
    def test_cashin_cryptonator_bitcoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoin_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_bitcoincash работает также как и cryptonator.")
    def test_cashin_cryptonator_bitcoincash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoincash_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_dash работает также как и cryptonator.")
    def test_cashin_cryptonator_dash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_dash_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_dogecoin работает также как и cryptonator.")
    def test_cashin_cryptonator_dogecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_dogecoin_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_ethereum работает также как и cryptonator.")
    def test_cashin_cryptonator_etheteum(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_ethereum_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_litecoin работает также как и cryptonator.")
    def test_cashin_cryptonator_litecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_litecoin_crypto_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_monero работает также как и cryptonator.")
    def test_cashin_cryptonator_monero(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_monero_id) == True:
            self.checkout_cripto()


    @unittest.skip("Платежная система cryptonator_ripple работает также как и cryptonator")
    def test_cashin_cryptonator_ripple(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_ripple_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_zcash работает также как и cryptonator.")
    def test_cashin_cryptonator_zcash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_cryptonator_zcash_id) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система swift выключена.")
    def test_cashin_swift_large(self):
        self.autorization()
        self.deposit_account(lk_conf.sum_large)
        if self.check_of_ps(lk_conf.ps_swift_id) == True:
            self.popup_swift_alert()
            self.payment_swift()

    @unittest.skip("Платежная система swift выключена.")
    def test_cashin_swift_small(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_swift_id) == True:
            self.find.element_by_xpath(lk_conf.popup_web_swift_small_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.swift_modal_title))
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.link_in_modal_body))

    def test_cashin_megapolis(self):
        self.login_simple()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_megapolis_id) == True:
            self.popup_swift_alert()
            self.payment_swift()

    unittest.skip("Платежная система test_cashin_megapolis_agree выключена.")
    def test_cashin_megapolis_agree(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_megapolis_agree_id) == True:
            self.find.element_by_xpath(lk_conf.popup_megapolis_xpath)
            self.find.element_by_xpath(lk_conf.button_megapolis_xpath).click()
            self.find.element_by_xpath(lk_conf.enter_to_megapolis_xpath)
            self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)

    def test_cashin_tinkoff(self):
        self.login_simple()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_tinkoff_id) == True:
            self.popup_swift_alert()
            self.payment_swift()

    unittest.skip("Платежная система test_cashin_tinkoff_agree выключена.")
    def test_cashin_tinkoff_agree(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_tinkoff_agree_id) == True:
            self.find.element_by_id(lk_conf.popup_tinkoff_id)
            self.find.element_by_xpath(lk_conf.button_tinkoff_xpath).click()
            self.find.element_by_xpath(lk_conf.enter_to_megapolis_xpath)
            self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)

    def test_cashin_ameria_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_ameria_swift_id) == True:
            self.popup_swift_alert()
            self.payment_swift()

    @unittest.skip("Платежная система tt_swift выключена.")
    def test_cashin_tt_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_tt_swift_id) == True:
            self.payment_swift(select_currency="yes")

    def test_packet_simple_premium_5000_through_account_c(self):
        self.check_packet(lk_conf.packet_premium_5000, lk_conf.pay_account_c)

    def test_packet_instalment_500_through_account_a(self):
        self.check_packet(lk_conf.packet_instalment_500, lk_conf.pay_account_a)

    def test_packet_instalment_start_through_account_ab(self):
        self.check_packet(lk_conf.packet_start, lk_conf.pay_account_ab)

    def test_packet_instalment_start_plus_through_account_b(self):
        self.check_packet(lk_conf.packet_start_plus, lk_conf.pay_account_b)

    def test_auth_login(self):
        self.check_login("", "", lk_conf.enter_password, enter_email='yes',)
        self.check_login(lk_priv_data.login_auth, "", lk_conf.enter_password)
        self.check_login(lk_priv_data.login_auth, "nnn", lk_conf.username_or_password_incorrect)
        self.check_login("nnn", "nnn", lk_conf.email_valid)

    #@unittest.skip("тест registration_and_verification выключен.")
    def test_registration_and_verification(self):
        self.registration()
        self.open_gmail()
        self.last_message = self.find.element_by_xpath(lk_conf.last_message_xpath)
        self.find.element_by_xpath(lk_conf.reg_link_xpath).click()
        self.choose_cityzenship_modal()
        self.verification()

    #@unittest.skip("тест test_transfer_of_money выключен, так как включены в ЛК доп. проверки на наличие гугл аутентификатора и получение кодов через смс")
    def test_transfer_of_money(self):
        self.login_simple()
        self.funds_transfer()
        try:
            self.get_and_insert_code()
        except TE:
            print("Сообщение на почту не пришло за указанное время")

    @unittest.skip("тест test_withdrawal_request выключен, так как включены в ЛК доп. проверки на наличие гугл аутентификатора и получение кодов через смс")
    def test_withdrawal_request(self):
        self.login_simple()
        self.add_requisites()
        self.withdrawal_request()
        self.get_and_insert_code()


    def check_packet(self, packet, payment_method):
        self.autorization()
        if packet['instalment'] == True:
            if packet['packet_id'] in lk_conf.exp_without_plus:
                self.find.element_by_xpath_and_move(lk_conf.first_payment_25_xpath).click()
            if packet['packet_id'] in lk_conf.exp_with_plus:
                self.find.element_by_xpath_and_move(lk_conf.first_payment_50_xpath).click()
            self.sum_list = self.packet_choose(packet['choose_packet_xpath'], lk_conf.url_checkout_inst % packet['packet_id'],
                               packet['price'], packet['count_shares'], payment_method, packet['instalment'])
            self.packet_instalment_payment(lk_conf.month_pay_instalment_xpath % packet['count_month'], payment_method)
            self.packet_sign_a_claim(self.sum_list, packet['price_all'], packet['instalment'], payment_method['type'], packet['price'])
        else:
            self.sum_list = self.packet_choose(packet['choose_packet_xpath'], lk_conf.url_checkout_simple % packet['packet_id'],
                               packet['price_all'], packet['count_shares'], payment_method, packet['instalment'])
            self.packet_sign_a_claim(self.sum_list, packet['price_all'], packet['instalment'], payment_method['type'])

    def packet_choose(self, packet_name, url_checkout, price_packet, count_shares, payment_method, packet_inst):
        self.main_balance_before_int = self.get_all_balance()
        self.find.element_by_xpath_and_move(packet_name).click()
        self.total_price = int(self.find.element_by_id(lk_conf.total_price_id).text.replace(' ', ''))
        self.assertEqual(url_checkout, self.driver.current_url)
        self.assertEqual(self.total_price, price_packet)
        self.sum_internal = self.pay.pay(packet_inst, payment_method, price_packet)
        self.find.element_by_id(lk_conf.progress_start_id).click()
        self.find.element_by_xpath(count_shares)
        self.assertEqual(lk_conf.url_acceptance_page, self.driver.current_url)
        self.find.element_by_xpath_and_move(lk_conf.checkbox_icon_xpath).click()
        self.find.element_by_xpath_and_move(lk_conf.button_buy_xpath).click()
        return self.sum_internal

    def packet_instalment_payment(self, count_month, payment_method):
        href_my_instalment = self.find.element_by_xpath_and_move(lk_conf.href_my_instalment_xpath)
        self.assertEqual(lk_conf.url_pay_instalment, self.driver.current_url)
        href_my_instalment.click()
        self.find.element_by_xpath(lk_conf.checkout_myinstalment_xpath)
        self.assertEqual(lk_conf.section_myinstalment, self.driver.current_url)
        self.find.element_by_xpath_and_move(lk_conf.select_pay_instalment_xpath).click()
        self.find.element_by_xpath(count_month).click()
        self.id_instalment = self.find.element_by_xpath(lk_conf.last_instalment_xpath).get_attribute(
            lk_conf.name_attr_instalment_id)
        if payment_method['type'] == "b":
            self.find.element_by_xpath(lk_conf.select_a_or_b % self.id_instalment).click()
            self.find.element_by_xpath(lk_conf.select_b % self.id_instalment).click()
        self.find.element_by_xpath_and_move(lk_conf.button_for_pay_instalment_xpath % self.id_instalment).click()

    def packet_sign_a_claim(self, sum, full_price_packet, packet_inst, payment_method, first_pay_price = 0):
        try:
            self.find.element_by_xpath(lk_conf.username_verif_data_xpath)
            self.find.element_by_xpath(lk_conf.requirement_xpath)
            sleep(3)  # временное решение
            self.sign = self.find.element_by_xpath_and_move(lk_conf.sign_xpath)
            self.sign.click()
        except TE:
            pass
        self.find.element_by_xpath(lk_conf.section_my_certificates_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.section_my_certificates))
        self.assertEqual(lk_conf.url_my_certificates, self.driver.current_url)
        self.actual_result = self.get_all_balance()
        self.exp_result = self.expected_result(sum, full_price_packet, packet_inst, payment_method, first_pay_price)
        self.assertEqual(self.exp_result, self.actual_result)

    def get_all_balance(self):
        self.balance_a_int = self.get_balance(lk_conf.balance_a_xpath)
        self.balance_b_int = self.get_balance(lk_conf.balance_b_xpath)
        self.balance_c_int = self.get_balance(lk_conf.balance_c_xpath)
        return [self.balance_a_int, self.balance_b_int, self.balance_c_int]

    def get_balance(self, name_account):
        self.account =  self.find.element_by_xpath(name_account).text.replace(' ', '')
        self.account_balance = int(self.account[:-4])
        return self.account_balance

    def expected_result(self, sum, full_price_packet, packet_inst, payment_method, first_pay_price):
        if packet_inst == True:
            if payment_method == "b":
                sum[1] = sum[1] + (full_price_packet - first_pay_price)
            else:
                sum[0] = sum[0] + (full_price_packet - first_pay_price)
        self.result_a = self.main_balance_before_int[0] - sum[0]
        self.result_b = self.main_balance_before_int[1] - sum[1]
        self.result_c = self.main_balance_before_int[2] - sum[2]
        return [self.result_a, self.result_b, self.result_c]

    def get_and_insert_code(self):
        self.open_in_new_window_mail()
        self.open_gmail()
        self.insert_code()

    def withdrawal_request(self):
        sleep(2)
        self.find.element_by_xpath_and_move(lk_conf.banking_section_xpath).click()
        self.find.element_by_xpath(lk_conf.withdrawal_request_xpath).click()
        self.count_request = len(self.find.elements_by_xpath(lk_conf.count_request_xpath))
        if self.count_request == 1:
            pass
        else:
            self.text_del = self.find.element_by_xpath(lk_conf.text_del_xpath).text
            if self.text_del == lk_conf.exp_text_for_del:
                self.find.element_by_xpath(lk_conf.link_for_delete).click()
                Alert(self.driver).accept()
        self.find.element_by_xpath_and_move(lk_conf.data_type_visamaster_xpath).click()
        self.find.element_by_id(lk_conf.input_sum_request_id).send_keys(lk_conf.sum_small)
        self.find.element_by_id(lk_conf.button_request_id).click()

    def add_requisites(self):
        self.banking_section()
        self.find.element_by_xpath(lk_conf.req_section_xpath).click()
        self.find.element_by_xpath(lk_conf.req_title_section_xpath)
        self.find.element_by_id_and_move(lk_conf.req_button_add).click()
        self.find.element_by_xpath(lk_conf.title_requisites_xpath)
        self.all_rows_before = len(self.driver.find_elements_by_xpath(lk_conf.all_rows_table_requisites_xpath))
        self.len_td_table = len(self.find.elements_by_xpath(lk_conf.len_td_table_xpath))
        if int(self.len_td_table) == 1:
            self.all_rows_before_and_one = int(self.all_rows_before)
        else:
            self.all_rows_before_and_one = int(self.all_rows_before) + 1
        self.find.element_by_id(lk_conf.open_mymodal_id)
        self.find.element_by_id(lk_conf.select_req_type_id)
        self.find.element_by_xpath(lk_conf.select_req_visa_xpath).click()
        self.find.element_by_id(lk_conf.input_req_number_visa_id).send_keys(
            lk_priv_data.req_number_visa)
        self.find.element_by_id(lk_conf.input_req_name_owner_id).send_keys(lk_conf.req_name_owner)
        self.find.element_by_id(lk_conf.input_req_expiry_id).send_keys(lk_conf.req_expiry)
        self.find.element_by_id(lk_conf.button_add_requisites_id).click()
        self.find.element_by_xpath(lk_conf.added_rows % self.all_rows_before_and_one)
        self.all_rows_after = int(len(self.find.elements_by_xpath(lk_conf.all_rows_table_requisites_xpath)))
        self.assertEqual(self.all_rows_before_and_one, self.all_rows_after)

    def verification(self):
        self.checkout_section_personal()
        self.verification_personal_data()
        self.verification_passport_data()
        self.verification_registration_address()
        #self.verification_uploading_of_the_doc()

    def checkout_section_personal(self):
        sleep(2)
        self.settings_section = self.find.element_by_xpath(lk_conf.settings_section_xpath)
        self.settings_section.is_displayed()
        self.settings_section.click()
        self.find.element_by_xpath(lk_conf.verification_section_xpath).click()
        self.fill = self.find.element_by_xpath(lk_conf.fill_forms_xpath)
        sleep(1)
        self.fill.click()

    def verification_personal_data(self):
        self.find.element_by_id(lk_conf.verif_field_ln_ru_id).send_keys(lk_conf.verif_ln_ru)
        self.find.element_by_id(lk_conf.verif_field_ln_en_id).send_keys(lk_conf.verif_ln_en)
        self.find.element_by_id_and_move(lk_conf.verif_field_n_ru_id).send_keys(lk_conf.verif_n_ru)
        self.find.element_by_id_and_move(lk_conf.verif_field_n_en_id).send_keys(lk_conf.verif_n_en)
        self.find.element_by_xpath(lk_conf.checkbox_female_xpath).click()
        self.find.element_by_id_and_move(lk_conf.select_birthday_id).click()
        self.find.element_by_xpath(lk_conf.select_birthday_count_xpath).click()
        self.find.element_by_id(lk_conf.select_birthmonth_id).click()
        self.find.element_by_xpath(lk_conf.select_birthmonth_count_xpath).click()
        self.find.element_by_id(lk_conf.select_birthyear_id).click()
        self.find.element_by_xpath(lk_conf.select_birthyear_count_xpath).click()
        self.find.element_by_id_and_move(lk_conf.select_birthplace_id).click()
        self.find.element_by_xpath(lk_conf.select_birthplace_country_xpath).click()
        self.find.element_by_xpath_and_move(lk_conf.button_next_passport_xpath).click()
        self.select_persondoc = self.find.element_by_id_and_move(lk_conf.select_persondoc_id)

    def verification_passport_data(self):
        self.select_persondoc.click()
        self.find.element_by_xpath(lk_conf.select_persondoc_type_xpath).click()
        self.find.element_by_id(lk_conf.field_persondoc_num_id).send_keys(lk_conf.persondoc_num)
        self.find.element_by_id_and_move(lk_conf.select_persondoc_day_id).click()
        self.find.element_by_xpath(lk_conf.select_persondoc_day_count_xpath).click()
        self.find.element_by_id(lk_conf.select_persondoc_month_id).click()
        self.find.element_by_xpath(lk_conf.select_persondoc_month_count_xpath).click()
        self.find.element_by_id(lk_conf.select_persondoc_year_id).click()
        self.find.element_by_xpath(lk_conf.select_persondoc_year_count_xpath).click()
        self.find.element_by_id_and_move(lk_conf.field_persondoc_who_issue_id).send_keys(lk_conf.persondoc_who_issue)
        self.find.element_by_xpath_and_move(lk_conf.button_next_address_xpath).click()
        self.selectaddress_region = self.find.element_by_id_and_move(lk_conf.select_address_region_id)

    def verification_registration_address(self):
        self.selectaddress_region.click()
        self.find.element_by_xpath(lk_conf.select_address_region_count_xpath).click()
        self.find.element_by_id(lk_conf.select_address_citytype_id).click()
        self.find.element_by_xpath(lk_conf.select_address_citytype_count_xpath).click()
        self.find.element_by_id(lk_conf.field_city_name_id).send_keys(lk_conf.city_name)
        self.find.element_by_id_and_move(lk_conf.select_address_streettype_id).click()
        self.find.element_by_xpath(lk_conf.select_address_streettype_count_xpath).click()
        self.find.element_by_id(lk_conf.field_address_street_id).send_keys(lk_conf.address_street_name)
        self.find.element_by_id(lk_conf.field_address_house_id).send_keys(lk_conf.house_number)
        self.find.element_by_xpath(lk_conf.button_finish_xpath).click()
        self.find.element_by_xpath(lk_conf.section_download_xpath)

    def verification_uploading_of_the_doc(self):
        for i in range(2):
            self.download_image()
            i += 1
        self.find.element_by_xpath(lk_conf.upload_confirm_xpath).click()
        sleep(2)
        self.button_confirm = self.find.element_by_id(lk_conf.button_confirm_id)
        sleep(2)
        self.button_confirm.click()
        self.find.element_by_xpath(lk_conf.finish_header_verif_xpath)
        self.assertEqual(self.driver.current_url, lk_conf.personal_list_link)

    def download_image(self):
        self.button_choose = self.find.element_by_xpath(lk_conf.button_choose_xpath).click()
        sleep(1)
        autoit.win_wait(lk_conf.autoit_title, lk_conf.autoit_wait)
        autoit.control_focus(lk_conf.autoit_title, lk_conf.autoit_control_edit)
        autoit.control_send(lk_conf.autoit_title, lk_conf.autoit_control_edit, lk_conf.autoit_image_path)
        autoit.control_click(lk_conf.autoit_title, lk_conf.autoit_control_button)
        self.find.element_by_xpath(lk_conf.button_download_xpath).click()
        sleep(3)

    def save_src_png(self, name_def):
        self.now = datetime.datetime.now()
        self.scr = str(self.now.year) + '_' + str(self.now.month) + '_' + str(self.now.day) + '_' + str(
            self.now.hour) + str(self.now.minute) + '_' + name_def + '.png'
        self.driver.save_screenshot(self.scr)
    def get_funcname(self):
        return inspect.stack()[1][3]

    def registration(self):
        self.find.element_by_xpath(lk_conf.sign_up_xpath).click()
        self.email = self.get_email(lk_conf.simple_reg_email)
        self.find.element_by_xpath(lk_conf.field_email_xpath).send_keys(self.email)
        self.find.element_by_xpath(lk_conf.for_phisical_xpath).click()
        self.find.element_by_xpath(lk_conf.button_sign_up_xpath).click()
        self.find.element_by_xpath(lk_conf.partner_sky_xpath)
        self.find.element_by_id(lk_conf.field_phone_id).send_keys(self.get_phone())
        self.find.element_by_xpath(lk_conf.field_regname_xpath).send_keys(lk_conf.regname + '_' + self.email)
        self.find.element_by_xpath(lk_conf.field_reglastname_xpath).send_keys(lk_conf.reglastname + '_' + self.email)
        self.find.element_by_xpath(lk_conf.field_reg_password).send_keys(lk_priv_data.reg_password)
        self.find.element_by_xpath(lk_conf.field_reg_confirmpassword).send_keys(lk_priv_data.reg_password)
        self.find.element_by_xpath_and_move(lk_conf.button_reg_signup_xpath).click()
        self.find.element_by_xpath(lk_conf.confirm_email_xpath)
        self.expect_message()
        return self.email

    def open_gmail(self):
        self.driver.get(lk_priv_data.mail_url)
        self.find.element_by_id(lk_conf.login_for_gmail_id).send_keys(lk_priv_data.login_for_gmail)
        self.find.element_by_xpath(lk_conf.confirm_auth_button_xpath).click()
        self.find.element_by_xpath(lk_conf.password_for_gmail_xpath).send_keys(lk_priv_data.password_for_gmail)
        self.find.element_by_xpath(lk_conf.confirm_auth_button_xpath).click()
        self.find.element_by_xpath(lk_conf.check_new_email_xpath).click()
        self.last_message = self.find.element_by_xpath_and_move(lk_conf.last_message_xpath)

    def choose_cityzenship_modal(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(lk_priv_data.main_url)
        self.find.element_by_xpath(lk_conf.header_model_citizenship_xpath)
        self.find.element_by_id(lk_conf.field_citizenship_country_id).click()
        self.find.element_by_xpath(lk_conf.ru_citizenship_country_xpath).click()
        self.find.element_by_id(lk_conf.field_country_id).click()
        self.find.element_by_xpath(lk_conf.ru_country_xpath).click()
        self.find.element_by_id(lk_conf.field_city_id).send_keys(lk_conf.reg_city)
        self.find.element_by_id(lk_conf.button_save_id).click()
        self.full_regname = lk_conf.regname + '_' + self.email + ' ' + lk_conf.reglastname + '_' + self.email
        self.find.element_by_xpath(lk_conf.username_in_lk % self.full_regname)
        return True

    def login(self, log_in, passw):
        self.find.element_by_xpath(lk_conf.login_field_xpath).send_keys(log_in)
        self.find.element_by_xpath(lk_conf.passw_field_xpath).send_keys(passw)
        self.find.element_by_xpath(lk_conf.login_button_xpath).click()

    def login_clear(self):
        self.find.element_by_xpath(lk_conf.login_field_xpath).clear()
        self.find.element_by_xpath(lk_conf.passw_field_xpath).clear()

    def check_login(self, check_login, check_passw, answer, enter_email='no'):
        self.login(check_login, check_passw)
        if enter_email == 'yes':
            self.find.element_by_xpath(lk_conf.enter_email_address)
        self.find.element_by_xpath(answer)
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

    def login_simple(self, login_simple=lk_priv_data.login_for_test, pasw_simple=lk_priv_data.passw_for_test, name_sample=lk_priv_data.full_name_for_test):
        self.login(login_simple, pasw_simple)
        self.find.element_by_xpath(lk_conf.username_in_lk % name_sample)
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def checkout_cripto(self):
        self.find.element_by_xpath(lk_conf.wait_checkout_cryptonator)
        self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def checkout_advcash(self):
        self.find.element_by_xpath(lk_conf.wait_checkout_advcash)
        self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def autorization(self):
        user = lk_priv_data.get_user()
        self.login(user['login'], user['password'])
        self.find.element_by_xpath(lk_conf.username_in_lk % user['full_name'])
        #print(self.user['login'])
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def banking_section(self):
        self.find.element_by_xpath(lk_conf.banking_section_xpath).click()

    def deposit_account(self, sum_cashin=lk_conf.sum_small):
        self.banking_section()
        self.find.element_by_xpath(lk_conf.deposit_account_section_xpath).click()
        self.find.element_by_xpath(lk_conf.dep_acc_title_xpath)
        self.assertEqual(lk_conf.check_url_cashin, self.driver.current_url)
        self.find.element_by_id_and_move(lk_conf.field_cashin_id).send_keys(sum_cashin)
        self.find.element_by_id(lk_conf.deposit_button_id).click()

    def search_all_ps(self):
        #Получаем спикок всех включенных платежных систем в виде значений атрибута 'id'.
        all_ps = self.find.elements_by_xpath(lk_conf.all_ps_xpath)
        list_ps_attribute = []
        for i in all_ps:
            list_ps_attribute.append(str(i.get_attribute(lk_conf.name_attribute)))
        return list_ps_attribute

    def check_of_ps(self, ps_id):
        list_ps = self.search_all_ps()
        # print(self.list_ps)
        if ps_id in list_ps:
            self.find.element_by_id_and_move(ps_id).click()
            return True
        else:
            print("Платежная система", ps_id, "выключена.")
            return False

    def checkout_impex_trading(self, instruction, popup_accept, success):
        self.find.element_by_xpath(instruction)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
        self.find.element_by_xpath_and_move(popup_accept).click()
        self.find.element_by_id_and_move(success).click()
        self.find.element_by_id(lk_conf.wait_checkout_trading_impex_id)
        self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def popup_swift_alert(self):
        self.find.element_by_xpath(lk_conf.popup_swift_alert_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_body_text))
        self.find.element_by_xpath(lk_conf.popup_accept_swift_alert_xpath).click()
        self.find.element_by_id(lk_conf.swift_alert_success_id).click()

    def payment_swift(self, select_currency="no", val=lk_conf.choose_val_gbp_xpath):
        self.find.element_by_xpath(lk_conf.choose_the_curr_for_payment_xpath)
        if select_currency == "yes":
            self.find.element_by_xpath_and_move(val).click()
        self.find.element_by_id_and_move(lk_conf.download_from_verification_swift_id).click()
        self.find.element_by_xpath_and_move(lk_conf.accept_swift_xpath).click()
        self.find.element_by_xpath_and_move(lk_conf.submit_swift_xpath).click()
        self.find.element_by_xpath(lk_conf.wait_checkout_swift_page_xapth)
        self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)

    def change_language(self):
        language_search = self.find.element_by_xpath(lk_conf.language_search_xpath)
        if language_search.text == "EN":
            language_search.click()
            self.find.element_by_xpath(lk_conf.switching_to_ru_xpath).click()
        self.find.element_by_xpath(lk_conf.enter_the_systeme_xpath)

    def debug(self):
        try:
            self.find.element_by_id(lk_conf.debug_toolbar_id)
            self.find.element_by_xpath(lk_conf.debug_minimize_xpath).click()
        except TE:
            pass

    def get_email(self, beginning_email):
        self.full_email_new = beginning_email + str(random.randint(11111, 99999)) + lk_conf.domain_name
        return self.full_email_new

    def get_phone(self):
        self.phone = str(lk_conf.phone_code) + str(lk_conf.region_code) + str(random.randint(1000000, 9999999))
        return self.phone

    def funds_transfer(self):
        self.banking_section()
        self.find.element_by_xpath(lk_conf.funds_transfer_section_xpath).click()
        self.find.element_by_id_and_move(lk_conf.enter_the_sum_main_id).send_keys(lk_conf.sum_small)
        self.find.element_by_id_and_move(lk_conf.enter_the_sum_bonus_id).send_keys(lk_conf.sum_small)
        self.find.element_by_id_and_move(lk_conf.enter_email_recipient_id).send_keys(lk_priv_data.email_recipient)
        self.find.element_by_id(lk_conf.input_submit_id).click()
        self.find.element_by_id_and_move(lk_conf.recipient_fio_id)
        self.assertTrue(self.driver.page_source.__contains__(lk_priv_data.full_recipient))
        self.find.element_by_xpath(lk_conf.confirmation_email_xpath).click()
        self.find.element_by_id_and_move(lk_conf.pay1button_id).click()
        self.find.element_by_id(lk_conf.input_sms_code_id)

    def open_in_new_window_mail(self):
        self.expect_message()
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def insert_code(self):
        self.last_message = self.find.element_by_xpath_and_move(lk_conf.element_with_code_xpath)
        self.confirmation_code = self.last_message.text[-5:]
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.find.element_by_id(lk_conf.input_sms_code_id).send_keys(self.confirmation_code)
        self.find.element_by_id(lk_conf.button_sms_code_id).click()
        self.find.element_by_id(lk_conf.transfer_success_id)

    def expect_message(self):
        sleep(120) #Ожидание поступления письма на почту

if __name__ == "__main__":
    unittest.main()





