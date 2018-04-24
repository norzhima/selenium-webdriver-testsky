import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInMegapolisAgree(LkCashInLoginRundom):

    def test_cashin_megapolis_agree(self):
        if self.check_of_ps(lk_conf.ps_megapolis_agree_id) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.popup_megapolis_xpath)
            self.methods.wait_and_find_element_by_xpath(lk_conf.button_megapolis_xpath).click()
            self.methods.wait_and_find_element_by_xpath(lk_conf.enter_to_megapolis_xpath)
            self.assertEqual(lk_conf.site_megapolis, self.driver.current_url)
