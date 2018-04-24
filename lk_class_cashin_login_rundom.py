from lk_class_login_rundom import LogInRundom
import lk_conf
import lk_priv_data
from lk_class_ps_methods import LkPsMethods


class LkCashInLoginRundom(LkPsMethods, LogInRundom):
    def setUp(self):
        super().setUp()
        self.deposit_account()
        self.assertEqual(lk_conf.check_url_cashin, self.driver.current_url)

    def tearDown(self):
        self.driver.get(lk_priv_data.main_url)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.logout).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.login_button_xpath)


