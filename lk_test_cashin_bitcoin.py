import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInBitcoin(LkCashInLoginRundom):

    def test_cashin_bitcoin(self):
        if self.check_of_ps(lk_conf.ps_bitcoin_id) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_bitcoin_xpath)


