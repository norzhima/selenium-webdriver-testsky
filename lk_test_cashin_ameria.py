import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInAmeria(LkCashInLoginRundom):

    def test_cashin_ameria_swift(self):
        if self.check_of_ps(lk_conf.ps_ameria_swift_id, lk_conf.tab_swift) == True:
            self.popup_swift_alert()
            self.payment_swift()
            self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)


