import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInAdvcash(LkCashInLoginRundom):

    def test_cashin_advcash_exmo(self):
        if self.check_of_ps(lk_conf.ps_adv_exmo_id) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash_ecoin(self):
        if self.check_of_ps(lk_conf.ps_adv_ecoin_id) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash(self):
        if self.check_of_ps(lk_conf.ps_adv_id) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash_payeer(self):
        if self.check_of_ps(lk_conf.ps_adv_payeer_id) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)

    def test_cashin_advcash_swift(self):
        if self.check_of_ps(lk_conf.ps_adv_swift_id) == True:
            self.checkout_advcash()
            self.assertEqual(lk_conf.site_advcash, self.driver.current_url)


