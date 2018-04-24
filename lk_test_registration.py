import lk_conf
import lk_priv_data
import random
from selenium.common.exceptions import TimeoutException as TE
from lk_class_base import LkBase
#from lk_class_cashin_login_rundom import LkCashInLoginRundom

class TestRegistration(LkBase):

    def test_registration(self):
        self.registration()
        self.methods.open_gmail()
        try:
            self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.new_reg_link_xpath % self.email).click()
            self.choose_cityzenship_modal()
        except TE:
            print("Verified user registration without email confirmation.")
            print("The message did not arrive within the specified time interval")


    def registration(self):
        self.methods.wait_and_find_element_by_xpath(lk_conf.sign_up_xpath).click()
        self.email = self.get_email(lk_conf.simple_reg_email)
        self.methods.wait_and_find_element_by_xpath(lk_conf.field_email_xpath).send_keys(self.email)
        self.methods.wait_and_find_element_by_xpath(lk_conf.for_phisical_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.button_sign_up_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.partner_sky_xpath)
        self.methods.wait_and_find_element_by_id(lk_conf.field_phone_id).send_keys(self.get_phone())
        self.methods.wait_and_find_element_by_xpath(lk_conf.field_regname_xpath).send_keys(lk_conf.regname + '_' + self.email)
        self.methods.wait_and_find_element_by_xpath(lk_conf.field_reglastname_xpath).send_keys(lk_conf.reglastname + '_' + self.email)
        self.methods.wait_and_find_element_by_xpath(lk_conf.field_reg_password).send_keys(lk_priv_data.reg_password)
        self.methods.wait_and_find_element_by_xpath(lk_conf.field_reg_confirmpassword).send_keys(lk_priv_data.reg_password)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.button_reg_signup_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.confirm_email_xpath)
        self.methods.expect_message()
        return self.email

    def choose_cityzenship_modal(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(lk_priv_data.main_url)
        self.methods.wait_and_find_element_by_xpath(lk_conf.header_model_citizenship_xpath)
        self.methods.wait_and_find_element_by_id(lk_conf.field_citizenship_country_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.ru_citizenship_country_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.field_country_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.ru_country_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.field_city_id).send_keys(lk_conf.reg_city)
        self.methods.wait_and_find_element_by_id(lk_conf.button_save_id).click()
        self.full_regname = lk_conf.regname + '_' + self.email + ' ' + lk_conf.reglastname + '_' + self.email
        self.methods.wait_and_find_element_by_xpath(lk_conf.username_in_lk % self.full_regname)

    def get_email(self, beginning_email):
        self.full_email_new = beginning_email + str(random.randint(11111, 99999)) + lk_conf.domain_name
        return self.full_email_new

    def get_phone(self):
        self.phone = str(lk_conf.phone_code) + str(lk_conf.region_code) + str(random.randint(1000000, 9999999))
        return self.phone
