# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as TE
import lk_conf
import lk_priv_data
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
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--start-maximized")
            #self.options.arguments
            self.driver = webdriver.Chrome(chrome_options=self.options)
        else:
            self.profile = webdriver.FirefoxProfile()
            self.profile.native_events_enabled = False
            self.driver = webdriver.Firefox()
            #profile.setEnableNativeEvents(false)
            self.driver.maximize_window()
        self.driver.get(lk_priv_data.main_url)
        self.assertEqual(lk_conf.short_company_name, self.driver.title)
        self.change_language()
        #self.debug()

    def tearDown(self):
        self.driver.quit()

    def test_cashin_pm(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_perfect_money_xpath, lk_conf.name_pm) == True:
            self.expect_visibility(lk_conf.wait_checkout_pm).click()
            self.assertIn(lk_conf.site_perfect_money, self.driver.current_url)

    def test_cashin_mera(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mera_xpath, lk_conf.name_mera) == True:
            self.expect_visibility(lk_conf.wait_checkout_mera)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    def test_cashin_advcash_exmo(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_exmo_xpath, lk_conf.name_advcash) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система ecoin работает также как и exmo")
    def test_cashin_advcash_ecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_ecoin_xpath, lk_conf.name_advcash) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система advcash работает также как и exmo")
    def test_cashin_advcash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_advcash_xpath, lk_conf.name_advcash) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система payeer работает также как и exmo")
    def test_cashin_payeer(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_adv_payeer_xpath, lk_conf.name_advcash) == True:
            self.checkout_advcash()

    @unittest.skip("Платежная система advcash-swift работает также как и exmo")
    def test_cashin_advcash_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_advcash_swift_xpath, lk_conf.name_advcash) == True:
            self.checkout_advcash()

    def test_cashin_impex_mastercard(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_mc_impex_xpath, lk_conf.name_mc) == True:
            self.checkout_impex_trading(lk_conf.instruction_mc_impex_xpath,
                                        lk_conf.popup_accept_mc_impex_xpath, lk_conf.mc_impex_success_xpath)

    def test_cashin_fasapay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_fasapay_xpath, lk_conf.name_fasa) == True:
            self.expect_visibility(lk_conf.wait_checkout_fasapay)
            self.assertIn(lk_conf.site_fasapay, self.driver.current_url)

    @unittest.skip("Платежная система impaya_world выключена.")
    def test_cashin_impex_impaya_world(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impaya_world_xpath, lk_conf.name_impaya) == True:
            self.checkout_impex_trading(lk_conf.instruction_impaya_world_xpath, lk_conf.popup_accept_impaya_world_xpath,
                                        lk_conf.impaya_world_success_xpath)

    def test_cashin_impex_visa(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexvisa_xpath, lk_conf.name_visa) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexvisa_xpath,
                                        lk_conf.popup_accept_impexvisa_xpath, lk_conf.impexvisa_success_xpath)

    def test_cashin_impex_orange(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexorange_xpath, lk_conf.name_orange) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexorange_xpath,
                                        lk_conf.popup_accept_impexorange_xpath, lk_conf.impexorange_success_xpath)

    def test_cashin_impex_payboutique(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexpayboutique_xpath, lk_conf.name_payboutique) == True:
            self.expect_visibility(lk_conf.wait_checkout_trading_impex)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)
            # self.checkout_impex_trading(lk_conf.instruction_impexpayboutique_xpath,
            #                             lk_conf.popup_accept_impexpayboutique_xpath, lk_conf.impexpayboutique_success_xpath)

    def test_cashin_webmoney(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.webmoney_xpath, lk_conf.name_webmoney) == True:
            self.expect_visibility(lk_conf.popup_webmoney)

    def test_cashin_bitcoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.bitcoin_xpath, lk_conf.name_bitcoin) == True:
            self.expect_visibility(lk_conf.popup_bitcoin)

    @unittest.skip("Платежная система epay выключена.")
    def test_cashin_impex_epay(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_impexepay_xpath, lk_conf.name_epay) == True:
            self.checkout_impex_trading(lk_conf.instruction_impexepay_xpath,
                                        lk_conf.popup_accept_impexepay_xpath,
                                        lk_conf.impexepay_success_xpath)

    def test_cashin_cryptonator(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_bitcoin работает также как и cryptonator")
    def test_cashin_cryptonator_bitcoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_bitcoin_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_bitcoincash работает также как и cryptonator")
    def test_cashin_cryptonator_bitcoincash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_bitcoincash_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_dash работает также как и cryptonator")
    def test_cashin_cryptonator_dash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_dash_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_dogecoin работает также как и cryptonator")
    def test_cashin_cryptonator_dogecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_dogecoin_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_ethereum работает также как и cryptonator")
    def test_cashin_cryptonator_etheteum(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_ethereum_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_litecoin работает также как и cryptonator")
    def test_cashin_cryptonator_litecoin(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_litecoin_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_monero работает также как и cryptonator")
    def test_cashin_cryptonator_monero(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_monero_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()


    @unittest.skip("Платежная система cryptonator_ripple работает также как и cryptonator")
    def test_cashin_cryptonator_ripple(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_ripple_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система cryptonator_zcash работает также как и cryptonator")
    def test_cashin_cryptonator_zcash(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.cryptonator_zcash_xpath, lk_conf.name_cryptonator) == True:
            self.checkout_cripto()

    @unittest.skip("Платежная система swift выключена.")
    def test_cashin_swift_large(self):
        self.autorization()
        self.deposit_account(lk_conf.sum_cashin_large)
        if self.check_of_ps(lk_conf.ps_web_swift_xpath, lk_conf.name_swift) == True:
            self.popup_swift_alert()
            self.payment_swift()

    @unittest.skip("Платежная система swift выключена.")
    def test_cashin_swift_small(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_web_swift_xpath, lk_conf.name_swift) == True:
            self.expect_visibility(lk_conf.popup_web_swift_small_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.swift_modal_title))
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.link_in_modal_body))

    def test_cashin_megapolis(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_megapolis_xpath, lk_conf.name_megapolis) == True:
            try:
                self.expect_visibility(lk_conf.popup_megapolis)
                self.expect_visibility(lk_conf.button_megapolis).click()
                self.expect_visibility(lk_conf.enter_to_megapolis)
                self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)
            except TE:
                self.popup_swift_alert()
                self.payment_swift()

    def test_cashin_tinkoff(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_tinkoff_xpath, lk_conf.name_megapolis) == True:
            try:
                self.expect_visibility(lk_conf.popup_tinkoff)
                self.expect_visibility(lk_conf.button_tinkoff).click()
                self.expect_visibility(lk_conf.enter_to_megapolis)
                self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)
            except TE:
                self.popup_swift_alert()
                self.payment_swift()

    def test_cashin_ameria_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_ameria_swift_xpath, lk_conf.name_ameria) == True:
            self.payment_swift()

    @unittest.skip("Платежная система tt_swift выключена.")
    def test_cashin_tt_swift(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_tt_swift_xpath, lk_conf.name_ttswift) == True:
            self.payment_swift(select_currency="yes")

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

    def test_auth_login(self):
        self.check_login("", "", lk_conf.enter_password, enter_email='yes',)
        self.check_login(lk_priv_data.login_auth, "", lk_conf.enter_password)
        self.check_login(lk_priv_data.login_auth, "nnn", lk_conf.username_or_password_incorrect)
        self.check_login("nnn", "nnn", lk_conf.email_valid)

    def test_transfer_of_money(self):
        self.autorization()
        self.funds_transfer()
        self.checkout_gmail()
        self.insert_code()

    #@unittest.skip("тест registration_and_verification выключен.")
    def test_registration_and_verification(self):
        self.registration()
        self.checkout_gmail()
        self.expect_visibility(lk_conf.reg_link_xpath).click()
        self.choose_cityzenship_modal()
        self.verification()


    def verification(self):
        #self.login_simple(lk_priv_data.login_for_verif, lk_priv_data.passw_for_verif, lk_priv_data.full_name_for_verif)
        self.checkout_section_personal()
        self.verification_personal_data()
        self.verification_passport_data()
        self.verification_registration_address()
        self.verification_uploading_of_the_doc()

    def checkout_section_personal(self):
        sleep(2)
        self.settings_section = self.expect_visibility(lk_conf.settings_section_xpath)
        self.settings_section.is_displayed()
        self.settings_section.click()
        self.expect_visibility(lk_conf.verification_section_xpath).click()
        self.fill = self.expect_visibility_and_move(lk_conf.fill_forms_xpath)
        sleep(1)
        self.fill.click()

    def verification_personal_data(self):
        self.expect_visibility(lk_conf.verif_field_ln_ru_xpath).send_keys(lk_conf.verif_ln_ru)
        self.expect_visibility(lk_conf.verif_field_ln_en_xpath).send_keys(lk_conf.verif_ln_en)
        self.expect_visibility_and_move(lk_conf.verif_field_n_ru_xpath).send_keys(lk_conf.verif_n_ru)
        self.expect_visibility_and_move(lk_conf.verif_field_n_en_xpath).send_keys(lk_conf.verif_n_en)
        self.expect_visibility_and_move(lk_conf.checkbox_female_xpath).click()
        self.expect_visibility_and_move(lk_conf.select_birthday_xpath).click()
        self.expect_visibility(lk_conf.select_birthday_count_xpath).click()
        self.expect_visibility(lk_conf.select_birthmonth_xpath).click()
        self.expect_visibility(lk_conf.select_birthmonth_count_xpath).click()
        self.expect_visibility(lk_conf.select_birthyear_xpath).click()
        self.expect_visibility(lk_conf.select_birthyear_count_xpath).click()
        self.expect_visibility_and_move(lk_conf.select_birthplace_xpath).click()
        self.expect_visibility(lk_conf.select_birthplace_country_xpath).click()
        self.expect_visibility_and_move(lk_conf.button_next_passport_xpath).click()
        self.select_persondoc = self.expect_visibility_and_move(lk_conf.select_persondoc_xpath)

    def verification_passport_data(self):
        self.select_persondoc.click()
        self.expect_visibility(lk_conf.select_persondoc_type_xpath).click()
        self.expect_visibility(lk_conf.field_persondoc_num_xpath).send_keys(lk_conf.persondoc_num)
        self.expect_visibility_and_move(lk_conf.select_persondoc_day_xpath).click()
        self.expect_visibility(lk_conf.select_persondoc_day_count_xpath).click()
        self.expect_visibility(lk_conf.select_persondoc_month_xpath).click()
        self.expect_visibility(lk_conf.select_persondoc_month_count_xpath).click()
        self.expect_visibility(lk_conf.select_persondoc_year_xpath).click()
        self.expect_visibility(lk_conf.select_persondoc_year_count_xpath).click()
        self.expect_visibility_and_move(lk_conf.field_persondoc_who_issue_xpath).send_keys(lk_conf.persondoc_who_issue)
        self.expect_visibility_and_move(lk_conf.button_next_address_xpath).click()
        self.selectaddress_region = self.expect_visibility_and_move(lk_conf.select_address_region_xpath)

    def verification_registration_address(self):
        self.selectaddress_region.click()
        self.expect_visibility(lk_conf.select_address_region_count_xpath).click()
        self.expect_visibility(lk_conf.select_address_citytype_xpath).click()
        self.expect_visibility(lk_conf.select_address_citytype_count_xpath).click()
        self.expect_visibility_and_move(lk_conf.field_city_name_xpath).send_keys(lk_conf.city_name)
        self.expect_visibility_and_move(lk_conf.select_address_streettype_xpath).click()
        self.expect_visibility(lk_conf.select_address_streettype_count_xpath).click()
        self.expect_visibility_and_move(lk_conf.field_address_street_xpath).send_keys(lk_conf.address_street_name)
        self.expect_visibility_and_move(lk_conf.field_address_house_xpath).send_keys(lk_conf.house_number)
        self.expect_visibility_and_move(lk_conf.button_finish_xpath).click()
        self.expect_visibility(lk_conf.section_download_xpath)

    def verification_uploading_of_the_doc(self):
        for i in range(2):
            self.download_image()
            i += 1
        self.expect_visibility_and_move(lk_conf.upload_confirm_xpath).click()
        self.button_confirm = self.expect_visibility_and_move(lk_conf.button_confirm_xpath)
        sleep(2)
        self.button_confirm.click()
        self.expect_visibility(lk_conf.finish_header_verif_xpath)
        self.assertEqual(self.driver.current_url, lk_conf.personal_list_link)

    def download_image(self):
        self.button_choose = self.expect_visibility_and_move(lk_conf.button_choose_xpath).click()
        sleep(1)
        autoit.win_wait(lk_conf.autoit_title, lk_conf.autoit_wait)
        autoit.control_focus(lk_conf.autoit_title, lk_conf.autoit_control_edit)
        autoit.control_send(lk_conf.autoit_title, lk_conf.autoit_control_edit, lk_conf.autoit_image_path)
        autoit.control_click(lk_conf.autoit_title, lk_conf.autoit_control_button)
        self.expect_visibility(lk_conf.button_download_xpath).click()
        sleep(3)

    def save_src_png(self, name_def):
        self.now = datetime.datetime.now()
        self.scr = str(self.now.year) + '_' + str(self.now.month) + '_' + str(self.now.day) + '_' + str(
            self.now.hour) + str(self.now.minute) + '_' + name_def + '.png'
        self.driver.save_screenshot(self.scr)
    def get_funcname(self):
        return inspect.stack()[1][3]

    def registration(self):
        self.expect_visibility(lk_conf.sign_up_xpath).click()
        self.email = self.get_email(lk_conf.simple_reg_email)
        self.expect_visibility(lk_conf.field_email_xpath).send_keys(self.email)
        self.expect_visibility(lk_conf.for_phisical_xpath).click()
        self.expect_visibility(lk_conf.button_sign_up_xpath).click()
        self.expect_visibility(lk_conf.partner_sky_xpath)
        self.expect_visibility(lk_conf.field_phone_xpath).send_keys(self.get_phone())
        self.expect_visibility(lk_conf.field_regname_xpath).send_keys(lk_conf.regname + '_' + self.email)
        self.expect_visibility(lk_conf.field_reglastname_xpath).send_keys(lk_conf.reglastname + '_' + self.email)
        self.expect_visibility(lk_conf.field_reg_password).send_keys(lk_priv_data.reg_password)
        self.expect_visibility(lk_conf.field_reg_confirmpassword).send_keys(lk_priv_data.reg_password)
        self.expect_visibility_and_move(lk_conf.button_reg_signup_xpath).click()
        self.expect_visibility(lk_conf.confirm_email_xpath)
        sleep(25) #Ожидание поступления письма на почту
        return self.email

    def checkout_gmail(self):
        self.driver.get(lk_priv_data.mail_url)
        self.expect_visibility(lk_conf.login_for_gmail_xpath).send_keys(lk_priv_data.login_for_gmail)
        self.expect_visibility(lk_conf.confirm_auth_button_xpath).click()
        self.expect_visibility(lk_conf.password_for_gmail_xpath).send_keys(lk_priv_data.password_for_gmail)
        self.expect_visibility(lk_conf.confirm_auth_button_xpath).click()
        self.expect_visibility(lk_conf.check_new_email_xpath).click()
        #window_before = self.driver.window_handles[0]
        #sleep(15)

    def choose_cityzenship_modal(self):
        #window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(self.driver.window_handles[1])
        #self.driver.switch_to.window(window_after)
        self.driver.get(lk_priv_data.main_url)
        self.expect_visibility(lk_conf.header_model_citizenship_xpath)
        self.expect_visibility(lk_conf.field_citizenship_country_xpath).click()
        self.expect_visibility(lk_conf.ru_citizenship_country_xpath).click()
        self.expect_visibility(lk_conf.field_country_xpath).click()
        self.expect_visibility(lk_conf.ru_country_xpath).click()
        self.expect_visibility(lk_conf.field_city_xpath).send_keys(lk_conf.reg_city)
        self.expect_visibility(lk_conf.button_save_xpath).click()
        self.full_regname = lk_conf.regname + '_' + self.email + ' ' + lk_conf.reglastname + '_' + self.email
        #print(self.full_regname)
        self.expect_visibility("//h3[contains(text(), '%s')]" % self.full_regname)
        #print(self.full_regname)
        return True

    def expect_visibility(self, path):
        #print(path)
        self.found_element = WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        return self.driver.find_element_by_xpath(path)

    def expect_visibility_and_move(self, path):
        #print(path)
        self.found_element = WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        self.found_element = self.driver.find_element_by_xpath(path)
        self.element_top = self.driver.execute_script("return arguments[0].getBoundingClientRect()", self.found_element).get("top")
        self.page_off_set = self.driver.execute_script("return window.pageYOffset")
        self.inner = self.driver.execute_script("return window.innerHeight")
        self.top_and_off_set = self.element_top + self.page_off_set
        self.element_middle = self.top_and_off_set - (self.inner / 2)
        self.driver.execute_script("window.scrollTo(0, arguments[0])", self.element_middle)
        sleep(0.2)
        self.found_element.is_displayed()
        return self.driver.find_element_by_xpath(path)

    def go_to_element(self, element, elem_position=lk_conf.elem_position_top):
        self.go_element = self.expect_visibility(element)
        if elem_position == lk_conf.elem_position_top:
            self.driver.execute_script("arguments[0].scrollIntoView(true)", self.go_element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(false)", self.go_element)

    def login(self, lig_in, passw):
        self.expect_visibility(lk_conf.login_field_xpath).send_keys(lig_in)
        self.expect_visibility(lk_conf.passw_field_xpath).send_keys(passw)
        self.expect_visibility(lk_conf.login_button_xpath).click()

    def login_clear(self):
        self.expect_visibility(lk_conf.login_field_xpath).clear()
        self.expect_visibility(lk_conf.passw_field_xpath).clear()

    def check_login(self, check_login, check_passw, answer, enter_email='no'):
        self.login(check_login, check_passw)
        if enter_email == 'yes':
            self.expect_visibility(lk_conf.enter_email_address)
        self.expect_visibility(answer)
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

    def login_simple(self, login_simple, pasw_simple, name_sample):
        self.login(login_simple, pasw_simple)
        self.expect_visibility("//h3[contains(text(), '%s')]" % name_sample)
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def checkout_cripto(self):
        self.expect_visibility(lk_conf.wait_checkout_cryptonator)
        self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def checkout_advcash(self):
        self.expect_visibility(lk_conf.wait_checkout_advcash)
        self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def autorization(self):
        self.user = lk_priv_data.get_user()
        self.login(self.user['login'], self.user['password'])
        self.expect_visibility("//h3[contains(text(), '%s')]" % self.user['full_name'])
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def deposit_account(self, sum_cashin=lk_conf.sum_cashin_small):
        self.expect_visibility(lk_conf.banking_section_xpath).click()
        self.expect_visibility(lk_conf.deposit_account_section_xpath).click()
        self.expect_visibility_and_move(lk_conf.dep_acc_title_xpath)
        self.assertEqual(lk_conf.check_url_cashin, self.driver.current_url)
        self.expect_visibility_and_move(lk_conf.field_cashin_xpath).send_keys(sum_cashin)
        self.expect_visibility(lk_conf.deposit_button_xpath).click()

    def search_all_ps(self):
        #Получаем спикок всех включенных платежных систем в виде значений атрибута 'data-code'.
        WebDriverWait(self.driver, lk_conf.delay).until(EC.visibility_of_element_located((By.XPATH, lk_conf.last_ps_xpath)))
        self.expect_visibility(lk_conf.you_were_billed_xpath)
        self.last_elem = self.expect_visibility(lk_conf.last_ps_xpath)
        self.all_ps = self.driver.find_elements_by_xpath(lk_conf.all_ps_xpath)
        self.list_ps_attribute = []
        for i in self.all_ps:
            self.list_ps_attribute.append(str(i.get_attribute(lk_conf.name_attribute)))
        return self.list_ps_attribute

    def check_of_ps(self, ps_xpath, data):
        self.list_ps = self.search_all_ps()
        #print(self.list_ps)
        if data in self.list_ps:
            self.expect_visibility_and_move(ps_xpath).click()
            return True
        else:
            print("Платежная система", data, "выключена.")
            return False

    def checkout_impex_trading(self, instruction, popup_accept, success):
        self.expect_visibility(instruction)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
        self.expect_visibility_and_move(popup_accept).click()
        self.expect_visibility_and_move(success).click()
        self.expect_visibility(lk_conf.wait_checkout_trading_impex)
        self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def popup_swift_alert(self):
        self.expect_visibility(lk_conf.popup_swift_alert_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_body_text))
        self.expect_visibility(lk_conf.popup_accept_swift_alert_xpath).click()
        self.expect_visibility(lk_conf.swift_alert_success_xpath).click()

    def payment_swift(self, select_currency="no", val=lk_conf.choose_val_gbp_xpath):
        self.expect_visibility(lk_conf.choose_the_curr_for_payment)
        if select_currency == "yes":
            self.expect_visibility_and_move(val).click()
        self.expect_visibility_and_move(lk_conf.download_from_verification_swift_xpath).click()
        self.expect_visibility_and_move(lk_conf.accept_swift_xpath).click()
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
        self.pay_account = self.expect_visibility_and_move(lk_conf.pay_account_xpath)
        self.assertEqual(url_checkout, self.driver.current_url)
        self.expect_visibility(lk_conf.total_price_xpath)
        sleep(2)
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
        self.expect_visibility_and_move(lk_conf.checkbox_icon_xpath).click()
        #ActionChains(self.driver).move_to_element(self.expect_visibility(lk_conf.checkbox_icon_xpath)).click().perform()
        # sleep(10)
        self.expect_visibility_and_move(lk_conf.button_buy_xpath).click()

    def packet_installment_payment(self, count_month):
        self.expect_visibility(lk_conf.main_balance_xpath)
        self.assertEqual(lk_conf.url_pay_instalment, self.driver.current_url)
        self.expect_visibility_and_move(lk_conf.href_my_installment_xpath).click()
        self.expect_visibility(lk_conf.checkout_myinstalment_xpath)
        self.assertEqual(lk_conf.section_myinstalment, self.driver.current_url)
        self.expect_visibility_and_move(lk_conf.select_pay_instalment_xpath).click()
        self.expect_visibility(count_month).click()
        self.id_instalment = self.expect_visibility(lk_conf.last_instalment_xpath).get_attribute(
            lk_conf.name_attr_instalment_id)
        self.expect_visibility_and_move("//button[@data-id='%s']" % self.id_instalment).click()

    def packet_sign_a_claim(self, full_price_packet):
        try:
            self.expect_visibility(lk_conf.username_verif_data_xpath)
            self.expect_visibility(lk_conf.requirement_xpath)
            self.expect_visibility(lk_conf.sign_xpath)
            sleep(3)  # временное решение
            self.sign = self.expect_visibility_and_move(lk_conf.sign_xpath)
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
            WebDriverWait(self.driver, lk_conf.delay).until(
                EC.visibility_of_element_located((By.ID, lk_conf.debug_toolbar_id)))
            self.expect_visibility(lk_conf.debug_minimize_xpath).click()
        except TE:
            pass

    def get_email(self, beginning_email):
        self.full_email_new = beginning_email + str(random.randint(1111, 9999)) + lk_conf.domain_name
        return self.full_email_new

    def get_phone(self):
        self.phone = str(lk_conf.phone_code) + str(lk_conf.region_code) + str(random.randint(1000000, 9999999))
        return self.phone

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
        self.expect_visibility_and_move(lk_conf.checkbox_icon_xpath).click()
        self.expect_visibility(lk_conf.button_buy_xpath).click()

    def funds_transfer(self):
        self.expect_visibility(lk_conf.banking_section_xpath).click()
        self.expect_visibility(lk_conf.funds_transfer_section_xpath).click()
        self.expect_visibility_and_move(lk_conf.enter_the_sum_main_xpath).send_keys(lk_conf.sum_cashin_small)
        self.expect_visibility_and_move(lk_conf.enter_the_sum_bonus_xpath).send_keys(lk_conf.sum_cashin_small)
        self.expect_visibility_and_move(lk_conf.enter_email_recipient_xpath).send_keys(lk_priv_data.email_recipient)
        self.expect_visibility(lk_conf.input_submit_xpath).click()
        self.expect_visibility_and_move(lk_conf.recipient_fio_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_priv_data.full_recipient))
        self.expect_visibility_and_move(lk_conf.pay1button_xpath).click()
        sleep(25)        #Ожидание поступления письма на почту
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def insert_code(self):
        self.element_with_code = self.expect_visibility(lk_conf.funds_code_xpath)
        self.code_for_transfer = self.element_with_code.text[-5:]
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.expect_visibility(lk_conf.input_sms_code_xpath).send_keys(self.code_for_transfer)
        self.expect_visibility(lk_conf.button_sms_code_xpath).click()
        self.expect_visibility(lk_conf.transfer_success_xpath)



if __name__ == "__main__":
    unittest.main()
