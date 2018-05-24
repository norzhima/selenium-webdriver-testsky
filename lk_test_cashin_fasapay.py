import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInFasapay(LkCashInLoginRundom):

    def test_cashin_fasapay(self):
        if self.check_of_ps(lk_conf.ps_fasapay_id, lk_conf.tab_systems) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_fasapay_xpath)
            self.assertIn(lk_conf.site_fasapay, self.driver.current_url)


