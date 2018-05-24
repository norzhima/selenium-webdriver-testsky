import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInAdvcash(LkCashInLoginRundom):

    def test_cashin_advcash_exmo(self):
        if self.check_of_ps(lk_conf.ps_adv_exmo_id, lk_conf.tab_aggregators) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash_ecoin(self):
        if self.check_of_ps(lk_conf.ps_adv_ecoin_id, lk_conf.tab_cryptonator) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash(self):
        if self.check_of_ps(lk_conf.ps_adv_id, lk_conf.tab_aggregators) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash_payeer(self):
        if self.check_of_ps(lk_conf.ps_adv_payeer_id, lk_conf.tab_aggregators) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    #На бою выключено
    def test_cashin_advcash_swift(self):
        if self.check_of_ps(lk_conf.ps_adv_swift_id, lk_conf.tab_aggregators) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)


