import unittest
from lk_class_base import LkBase
import lk_conf
import lk_priv_data

class TestAuth(LkBase):

    def test_auth(self):
        self.check_login("", "", lk_conf.enter_password, enter_email='yes', )
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

        self.check_login(lk_priv_data.login_auth, "", lk_conf.enter_password)
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

        self.check_login(lk_priv_data.login_auth, "nnn", lk_conf.username_or_password_incorrect)
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

        self.check_login("nnn", "nnn", lk_conf.email_valid)
        self.assertEqual(lk_conf.auth, self.driver.current_url)
        self.login_clear()

    def login_clear(self):
        self.methods.wait_and_find_element_by_xpath(lk_conf.login_field_xpath).clear()
        self.methods.wait_and_find_element_by_xpath(lk_conf.passw_field_xpath).clear()

    def check_login(self, check_login, check_passw, answer, enter_email='no'):
        self.methods.login(check_login, check_passw)
        if enter_email == 'yes':
            self.methods.wait_and_find_element_by_xpath(lk_conf.enter_email_address)
        self.methods.wait_and_find_element_by_xpath(answer)





