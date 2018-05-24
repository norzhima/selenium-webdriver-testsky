import unittest
import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInTtswift(LkCashInLoginRundom):

    #@unittest.skip("Платежная система payment-tt выключена.")
    def test_cashin_tt_swift(self):
        if self.check_of_ps(lk_conf.ps_tt_swift_id, lk_conf.tab_swift, sum_cashin=200) == True:
            self.payment_swift(select_currency="yes", val=lk_conf.choose_val_eur_xpath)
            self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)