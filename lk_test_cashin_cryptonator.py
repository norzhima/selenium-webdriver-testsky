import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInCryptonator(LkCashInLoginRundom):

    def test_cashin_cryptonator(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_id, lk_conf.tab_aggregators) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_bitcoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoin_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_bitcoincash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoincash_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_dash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_dash_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_dogecoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_dogecoin_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_etheteum(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_ethereum_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_litecoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_litecoin_crypto_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_monero(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_monero_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_ripple(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_ripple_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_zcash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_zcash_id, lk_conf.tab_cryptonator) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)




