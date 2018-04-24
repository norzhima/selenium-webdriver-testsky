import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInWebmoney(LkCashInLoginRundom):

    def test_cashin_webmoney(self):
        if self.check_of_ps(lk_conf.ps_webmoney_id) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_webmoney_xpath)



