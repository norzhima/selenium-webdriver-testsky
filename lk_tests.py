# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as TE
import lk_conf
import lk_priv_data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class LkswcTest(unittest.TestCase):
    def setUp(self):
        if lk_conf.default_browser is "Chrome":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(chrome_options=self.options)
        else:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        self.driver.get(lk_priv_data.main_url)
        self.assertEqual(lk_conf.short_company_name, self.driver.title)
        self.change_language()
        #self.debug()

    def tearDown(self):
        self.driver.quit()

    def test_cashin_bitcoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.bitcoin_xpath, lk_conf.name_bitcoin,
                            element=lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom) == True:
            self.expect_visibility(lk_conf.popup_bitcoin)

    def test_cashin_cryptonator(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_xpath, lk_conf.name_cryptonator,
                            element=lk_conf.footer_xpath,
                            elem_position=lk_conf.elem_position_bottom) == True:
            self.expect_visibility(lk_conf.wait_checkout_cryptonator)
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)
    '''
    def test_cashin_ecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_ecoin_xpath, lk_conf.name_ecoin) == True:
            self.expect_visibility(lk_conf.wait_checkout_advcash)
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)
    #'''
    def test_cashin_exmo(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_exmo_xpath, lk_conf.name_exmo) == True:
            self.expect_visibility(lk_conf.wait_checkout_advcash)
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_fasapay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_fasapay_xpath, lk_conf.name_fasa) == True:
            self.expect_visibility(lk_conf.wait_checkout_fasapay)
            self.assertIn(lk_conf.site_fasapay, self.driver.current_url)
    '''
    def test_cashin_impex_epay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexepay_xpath, lk_conf.name_epay,
                            element=lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexepay_xpath,
                                        lk_conf.popup_accept_impexepay_xpath,
                                        lk_conf.impexepay_success_xpath)
    #''''''
    def test_cashin_impex_impaya_world(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impaya_world_xpath, lk_conf.name_impaya) == True:
            self.checkout_impex_trading(lk_conf.instruction_impaya_world_xpath, lk_conf.popup_accept_impaya_world_xpath,
                                        lk_conf.impaya_world_success_xpath)
    #'''
    def test_cashin_impex_mastercard(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mc_impex_xpath, lk_conf.name_mc) == True:
            self.checkout_impex_trading(lk_conf.instruction_mc_impex_xpath,
                                        lk_conf.popup_accept_mc_impex_xpath, lk_conf.mc_impex_success_xpath)

    def test_cashin_impex_orange(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexorange_xpath, lk_conf.name_orange) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexorange_xpath,
                                        lk_conf.popup_accept_impexorange_xpath, lk_conf.impexorange_success_xpath)

    def test_cashin_impex_visa(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexvisa_xpath, lk_conf.name_visa) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexvisa_xpath,
                                        lk_conf.popup_accept_impexvisa_xpath, lk_conf.impexvisa_success_xpath)

    def test_cashin_megapolis(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_megapolis_xpath, lk_conf.name_megapolis,
                            element=lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom) == True:
            try:
                self.expect_visibility(lk_conf.popup_megapolis)
                self.expect_visibility(lk_conf.button_megapolis).click()
                self.expect_visibility(lk_conf.enter_to_megapolis)
                self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)
            except TE:
                self.popup_swift_alert()
                self.payment_swift()

    def test_cashin_mera(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mera_xpath, lk_conf.name_mera) == True:
            self.expect_visibility(lk_conf.popup_checkbox_accept_xpath).click()
            self.expect_visibility(lk_conf.mera_success_xpath).click()
            self.expect_visibility(lk_conf.wait_checkout_mera)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    def test_cashin_pm(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_perfect_money_xpath, lk_conf.name_pm) == True:
            self.expect_visibility(lk_conf.wait_checkout_pm).click()
            self.assertIn(lk_conf.site_perfect_money, self.driver.current_url)
    '''
    def test_cashin_swift_large(self):
        self.autorization()
        self.deposit_account(lk_conf.sum_cashin_large)
        if self.check_of_ps(lk_conf.ps_web_swift_xpath, lk_conf.name_swift,
                            element=lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom) == True:
            self.popup_swift_alert()
            self.payment_swift()

    def test_cashin_swift_small(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_web_swift_xpath, lk_conf.name_swift,
                            element=lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom) == True:
            self.expect_visibility(lk_conf.popup_web_swift_small_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.swift_modal_title))
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.link_in_modal_body))
    #'''
    def test_cashin_tt_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.tt_swift_xpath, lk_conf.name_ttswift, element=lk_conf.footer_xpath,
                            elem_position=lk_conf.elem_position_bottom) == True:
            self.payment_swift(select_currency="yes")

    def test_cashin_webmoney(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.webmoney_xpath, lk_conf.name_webmoney,
                            element=lk_conf.select_payment_system) == True:
            self.expect_visibility(lk_conf.popup_webmoney)

    def test_check_packet_tree(self):
        self.autorization()
        self.packet_choose(lk_conf.packet_tree_xpath, 1, lk_conf.url_checkout_tree,
                           lk_conf.price_tree, lk_conf.count_shares_tree_xpath)
        self.packet_sign_a_claim(lk_conf.price_tree)

    def test_check_packet_instalment_500(self):
        self.autorization()
        self.packet_choose(lk_conf.packet_instalment_500_xpath, 7, lk_conf.url_checkout_instalment_500,
                           lk_conf.price_instalment_500, lk_conf.count_shares_instalment_500_xpath)
        self.packet_installment_payment(lk_conf.month_pay_instalment_xpath)
        self.packet_sign_a_claim(lk_conf.price_instalment_500_all)


    def expect_visibility(self, path):
        #print(path)
        WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        return self.driver.find_element_by_xpath(path)

    def go_to_element(self, element, elem_position=lk_conf.elem_position_top):
        self.go_element = self.expect_visibility(element)
        if elem_position == lk_conf.elem_position_top:
            self.driver.execute_script("arguments[0].scrollIntoView(true)", self.go_element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.go_element)

    def autorization(self):
        self.user = lk_priv_data.get_user()
        self.expect_visibility(lk_conf.login_field_xpath).send_keys(self.user['login'])
        self.expect_visibility(lk_conf.passw_field_xpath).send_keys(self.user['password'])
        self.expect_visibility(lk_conf.login_button_xpath).click()
        self.expect_visibility("//h3[contains(text(), '%s')]" % self.user['full_name'])
        self.assertEqual(lk_conf.full_company_name, self.driver.title)
        self.assertTrue(self.driver.page_source.__contains__(self.user['full_name']))

    def deposit_account(self, sum_cashin=lk_conf.sum_cashin_small):
        self.expect_visibility(lk_conf.banking_xpath).click()
        self.expect_visibility(lk_conf.deposit_account_xpath).click()
        self.assertEqual(lk_conf.check_url_cashin, self.driver.current_url)
        self.go_to_element(lk_conf.dep_acc_title_xpath)
        self.expect_visibility(lk_conf.field_cashin_xpath).send_keys(sum_cashin)
        self.expect_visibility(lk_conf.deposit_button_xpath).click()

    def search_all_ps(self):
        WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, lk_conf.last_ps_xpath)))
        self.last_elem = self.driver.find_element_by_xpath(lk_conf.last_ps_xpath)
        self.all_ps = self.driver.find_elements_by_xpath(lk_conf.all_ps_xpath)
        self.list_ps_attribute = []
        for i in self.all_ps:
            self.list_ps_attribute.append(str(i.get_attribute(lk_conf.name_attribute)))
        return self.list_ps_attribute

    def check_of_ps(self, ps_xpath, data, element=lk_conf.deposit_button_xpath,
                    elem_position=lk_conf.elem_position_top):
        self.list_ps = self.search_all_ps()
        if data in self.list_ps:
            self.ps = self.expect_visibility(ps_xpath)
            self.go_to_element(element, elem_position)
            # time.sleep(10)
            self.ps.click()
            return True
        else:
            print("Платежная система", data, "выключена.")
            return False

    def checkout_impex_trading(self, instruction, popup_accept, success):
        self.expect_visibility(instruction)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
        self.expect_visibility(popup_accept).click()
        self.expect_visibility(success).click()
        self.expect_visibility(lk_conf.wait_checkout_trading_impex)
        self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def popup_swift_alert(self):
        self.expect_visibility(lk_conf.popup_swift_alert_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_body_text))
        self.expect_visibility(lk_conf.popup_accept_swift_alert_xpath).click()
        self.expect_visibility(lk_conf.swift_alert_success_xpath).click()

    def payment_swift(self, select_currency="no", val=lk_conf.choose_val_ru):
        self.expect_visibility(lk_conf.choose_the_curr_for_payment)
        #self.go_to_element(lk_conf.choose_the_curr_for_payment)
        if select_currency == "yes":
            self.val_tt = self.expect_visibility(val)
            self.go_to_element(lk_conf.header_page)
            #time.sleep(5)
            self.val_tt.click()
        self.go_to_element(lk_conf.choose_the_curr_for_payment)
        self.expect_visibility(lk_conf.download_from_verification_swift_xpath).click()
        self.expect_visibility(lk_conf.accept_swift_xpath)
        self.accept_swift = self.driver.find_element_by_xpath(lk_conf.accept_swift_xpath)
        self.go_to_element(lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom)
        #time.sleep(10)
        self.accept_swift.click()
        self.expect_visibility(lk_conf.submit_swift_xpath).click()
        self.expect_visibility(lk_conf.wait_checkout_swift_page)
        self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)

    def packet_choose(self, packet_name, count_pack, url_checkout, price_packet, count_shares):
        self.packet = self.expect_visibility(packet_name)
        self.expect_visibility(lk_conf.main_balance_xpath)
        self.main_balance_before = self.driver.find_elements_by_xpath(lk_conf.main_balance_xpath)
        self.main_balance_before_replace = self.main_balance_before[0].text.replace(' ', '')
        self.main_balance_before_replace_int = int(self.main_balance_before_replace[:-4])
        self.package_header = self.driver.find_elements_by_xpath(lk_conf.package_header_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", self.package_header[count_pack])
        self.packet.click()
        self.pay_account = self.expect_visibility(lk_conf.pay_account_xpath)
        self.assertEqual(url_checkout, self.driver.current_url)
        self.expect_visibility(lk_conf.total_price_xpath)
        time.sleep(2)
        self.go_to_element(lk_conf.total_price_xpath)
        self.pay_account.click()
        self.expect_visibility(lk_conf.main_account_xpath)
        self.total_price = self.expect_visibility(lk_conf.total_price_xpath)
        self.total_price_int = int(self.total_price.text.replace(' ', ''))
        self.input_one = self.expect_visibility(lk_conf.input_one_xpath)
        self.assertEqual(self.total_price_int, price_packet)
        self.input_one.send_keys(price_packet)
        self.expect_visibility(lk_conf.checkout_tree_xpath).click()
        self.expect_visibility(lk_conf.progress_start_xpath).click()
        self.expect_visibility(count_shares)
        self.assertEqual(lk_conf.url_acceptance_page, self.driver.current_url)
        self.go_to_element(lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom)
        self.expect_visibility(lk_conf.checkbox_icon_xpath).click()
        self.expect_visibility(lk_conf.button_buy_xpath).click()

    def packet_installment_payment(self, count_month):
        self.expect_visibility(lk_conf.main_balance_xpath)
        self.assertEqual(lk_conf.url_pay_instalment, self.driver.current_url)
        self.checkout_my_instalment = self.expect_visibility(lk_conf.href_my_installment_xpath)
        self.go_to_element(lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom)
        #time.sleep(10)
        self.checkout_my_instalment.click()
        self.expect_visibility(lk_conf.checkout_myinstalment_xpath)
        self.assertEqual(lk_conf.section_myinstalment, self.driver.current_url)
        self.select_pay_instalment = self.expect_visibility(lk_conf.select_pay_instalment_xpath)
        self.go_to_element(lk_conf.schedule_payment_xpath)
        self.select_pay_instalment.click()
        self.expect_visibility(count_month).click()
        self.id_instalment = self.expect_visibility(lk_conf.last_instalment_xpath).get_attribute(
            lk_conf.name_attr_instalment_id)
        self.expect_visibility("//button[@data-id='%s']" % self.id_instalment).click()

    def packet_sign_a_claim(self, full_price_packet):
        try:
            self.expect_visibility(lk_conf.username_verif_data_xpath)
            self.expect_visibility(lk_conf.requirement_xpath)
            self.sign = self.expect_visibility(lk_conf.sign_xpath)
            time.sleep(3)  # временное решение
            self.go_to_element(lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom)
            self.sign.click()
        except TE:
            pass
        self.expect_visibility(lk_conf.section_my_certificates_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.section_my_certificates))
        self.assertEqual(lk_conf.url_my_certificates, self.driver.current_url)
        self.main_balance_after = self.expect_visibility(lk_conf.main_balance_xpath)
        self.main_balance_after_replace = self.main_balance_after.text.replace(' ', '')
        self.main_balance_after_replace_int = int(self.main_balance_after_replace[:-4])
        self.assertEqual(self.main_balance_before_replace_int - full_price_packet, self.main_balance_after_replace_int)

    def change_language(self):
        self.language_search = self.expect_visibility(lk_conf.language_search_xpath)
        if self.language_search.text == "EN":
            self.language_search.click()
            self.switching_to_ru = self.expect_visibility(lk_conf.switching_to_ru_xpath).click()
        self.expect_visibility(lk_conf.enter_the_systeme_xpath)

    def debug(self):
        try:
            #self.expect_visibility(lkswc_config.debug_toolbar_xpath)
            WebDriverWait(self.driver, lk_conf.delay).until(EC.visibility_of_element_located((By.ID, lk_conf.debug_toolbar_id)))
            self.expect_visibility(lk_conf.debug_minimize_xpath).click()
            #WebDriverWait(self.driver, lkswc_config.delay).until(EC.visibility_of_element_located((By.XPATH, lkswc_config.debug_minimize_xpath)))
            #self.debug_minimize = self.driver.find_element_by_xpath(lkswc_config.debug_minimize_xpath)
            #self.debug_minimize.click()
        except TE:
            pass

    def packet_choose_old(self, packet_name, count_pack, url_checkout, price_packet, count_shares):
        self.packet = self.expect_visibility(packet_name)
        self.expect_visibility(lk_conf.main_balance_xpath)
        self.main_balance_before = self.driver.find_elements_by_xpath(lk_conf.main_balance_xpath)
        self.main_balance_before_replace = self.main_balance_before[0].text.replace(' ', '')
        self.main_balance_before_replace_int = int(self.main_balance_before_replace[:-4])
        self.package_header = self.driver.find_elements_by_xpath(lk_conf.package_header_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", self.package_header[count_pack])
        self.packet.click()
        self.assertEqual(url_checkout, self.driver.current_url)
        self.expect_visibility(lk_conf.main_account_xpath)
        self.input_one = self.expect_visibility(lk_conf.input_one_xpath)
        self.input_one.send_keys(price_packet)
        self.expect_visibility(lk_conf.checkout_tree_xpath).click()
        self.expect_visibility(lk_conf.progress_start_xpath).click()
        self.expect_visibility(lk_conf.you_select_shares_xpath)
        self.expect_visibility(count_shares)
        self.assertEqual(lk_conf.url_acceptance_page, self.driver.current_url)
        self.go_to_element(lk_conf.footer_xpath, elem_position=lk_conf.elem_position_bottom)
        self.expect_visibility(lk_conf.checkbox_icon_xpath).click()
        self.expect_visibility(lk_conf.button_buy_xpath).click()

if __name__ == "__main__":
    unittest.main()
