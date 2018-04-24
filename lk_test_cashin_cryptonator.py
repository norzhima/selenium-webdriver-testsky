import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInCryptonator(LkCashInLoginRundom):

    def test_cashin_cryptonator(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_bitcoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoin_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_bitcoincash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_bitcoincash_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_dash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_dash_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_dogecoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_dogecoin_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_etheteum(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_ethereum_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_litecoin(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_litecoin_crypto_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_monero(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_monero_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_ripple(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_ripple_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)

    def test_cashin_cryptonator_zcash(self):
        if self.check_of_ps(lk_conf.ps_cryptonator_zcash_id) == True:
            self.checkout_cripto()
            self.assertIn(lk_conf.site_cryptonator, self.driver.current_url)




