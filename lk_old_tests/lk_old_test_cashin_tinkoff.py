import lk_conf
from lk_class_cashin_login_simple import LkCashInLogInSimple
from time import sleep

class TestCashInTinkoff(LkCashInLogInSimple):

    def test_cashin_tinkoff(self):
        if self.check_of_ps(lk_conf.ps_tinkoff_id, lk_conf.tab_swift) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_swift_alert_xpath)
            self.assertTrue(self.driver.page_source.__contains__(lk_conf.impex_modal_body_text))
            self.popup_swift_alert()
            self.payment_swift()
            self.assertEqual(lk_conf.url_swift_invoices, self.driver.current_url)


