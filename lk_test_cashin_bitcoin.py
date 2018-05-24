import lk_conf
from lk_class_cashin_login_yield import LkCashInLoginRundom

class TestCashInBitcoin(LkCashInLoginRundom):

    def test_cashin_bitcoin(self):
        if self.check_of_ps(lk_conf.ps_bitcoin_id, lk_conf.tab_cryptonator) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_bitcoin_xpath)


