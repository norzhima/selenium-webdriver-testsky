import unittest
import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInSwift(LkCashInLoginRundom):

    #@unittest.skip("Платежная система payment-swift выключена.")
    def test_cashin_swift_large(self):
        if self.check_of_ps(lk_conf.ps_swift_id) == True:
            self.popup_swift_alert()
            self.payment_swift()
            self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)

    #@unittest.skip("Платежная система payment-swift выключена.")
    def test_cashin_swift_small(self):
        if self.check_of_ps(lk_conf.ps_swift_id) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_web_swift_small_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.swift_modal_title))
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.link_in_modal_body))
