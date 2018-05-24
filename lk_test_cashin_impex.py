import unittest
import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInImpex(LkCashInLoginRundom):

    def test_cashin_impex_mastercard(self):
        if self.check_of_ps(lk_conf.ps_impex_mc_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.instruction_mc_impex_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
            self.checkout_impex_trading(lk_conf.popup_accept_mc_impex_xpath, lk_conf.mc_impex_success_id)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def test_cashin_impex_visa(self):
        if self.check_of_ps(lk_conf.ps_impex_visa_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.instruction_impexvisa_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
            self.checkout_impex_trading(lk_conf.popup_accept_impexvisa_xpath, lk_conf.impexvisa_success_id)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def test_cashin_impex_orange(self):
        if self.check_of_ps(lk_conf.ps_impex_orange_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.instruction_impexorange_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
            self.checkout_impex_trading(lk_conf.popup_accept_impexorange_xpath,
                                                lk_conf.impexorange_success_id)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    def test_cashin_impex_payboutique(self):
        if self.check_of_ps(lk_conf.ps_impex_payboutique_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.instruction_impexpayboutique_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
            self.checkout_impex_trading(lk_conf.popup_accept_impexpayboutique_xpath,
                                        lk_conf.impexpayboutique_success_id)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

    @unittest.skip("PS impex_epay desabled")
    def test_cashin_impex_epay(self):
        if self.check_of_ps(lk_conf.ps_impex_epay_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.instruction_impexepay_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_subtitle))
            self.checkout_impex_trading(lk_conf.popup_accept_impexepay_xpath,
                                        lk_conf.impexepay_success_id)
            self.assertEqual(lk_conf.site_trading_impex, self.driver.current_url)

