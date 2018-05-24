import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInMera(LkCashInLoginRundom):

    def test_cashin_mera(self):
        if self.check_of_ps(lk_conf.ps_mera_id, lk_conf.tab_visa_mastercard) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    def test_cashin_mera_qiwi(self):
        if self.check_of_ps(lk_conf.ps_mera_qiwi_id, lk_conf.tab_systems) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

    def test_cashin_mera_euroset(self):
        if self.check_of_ps(lk_conf.ps_mera_euroset_id, lk_conf.tab_cash) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_mera_xpath)
            self.assertIn(lk_conf.site_mera, self.driver.current_url)

