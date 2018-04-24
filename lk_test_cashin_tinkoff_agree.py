import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInTinkoffAgree(LkCashInLoginRundom):

    def test_cashin_tinkoff_agree(self):
        if self.check_of_ps(lk_conf.ps_tinkoff_agree_id) == True:
            self.methods.wait_and_find_element_by_id(lk_conf.popup_tinkoff_id)
            self.methods.wait_and_find_element_by_xpath(lk_conf.button_tinkoff_xpath).click()
            self.methods.wait_and_find_element_by_xpath(lk_conf.enter_to_megapolis_xpath)
            self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)