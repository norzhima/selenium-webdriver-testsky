import lk_conf
from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestCashInPm(LkCashInLoginRundom):

    def test_cashin_pm(self):
        if self.check_of_ps(lk_conf.ps_perfect_money_id) == True:
            self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_pm_xpath).click()
            self.assertIn(lk_conf.site_perfect_money, self.driver.current_url)
            self.driver.switch_to.window(self.driver.window_handles[0])


