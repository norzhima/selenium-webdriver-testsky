import unittest
import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInTtswift(LkCashInLoginRundom):

    #@unittest.skip("Платежная система payment-tt выключена.")
    def test_cashin_tt_swift(self):
        if self.check_of_ps(lk_conf.ps_tt_swift_id) == True:
            self.payment_swift(select_currency="yes")
            self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)