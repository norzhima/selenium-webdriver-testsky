from lk_class_base import LkBase
import lk_conf

class LogInRundom(LkBase):

    def setUp(self):
        super().setUp()
        self.methods.autorization()
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def tearDown(self):
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.logout).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.login_button_xpath)


