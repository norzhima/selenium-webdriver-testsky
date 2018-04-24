import lk_conf
import lk_priv_data
from selenium.common.exceptions import TimeoutException as TE
from lk_class_login_simple import LkLogInSimple

class TestTransferOfMoney(LkLogInSimple):

    def tearDown(self):
        self.driver.get(lk_priv_data.main_url)
        super().tearDown()


    def test_transfer_of_money(self):
        self.funds_transfer()
        try:
            self.methods.get_and_insert_code()
        except TE:
            print("Message to the mail did not come for Wednesday time")


    def funds_transfer(self):
        self.methods.banking_section()
        self.methods.wait_and_find_element_by_xpath(lk_conf.funds_transfer_section_xpath).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.enter_the_sum_main_id).send_keys(lk_conf.sum_small)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.enter_the_sum_bonus_id).send_keys(lk_conf.sum_small)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.enter_email_recipient_id).send_keys(lk_priv_data.email_recipient)
        self.methods.wait_and_find_element_by_id(lk_conf.input_submit_id).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.recipient_fio_id)
        self.assertTrue(self.driver.page_source.__contains__(lk_priv_data.full_recipient))
        self.methods.wait_and_find_element_by_xpath(lk_conf.confirmation_email_xpath).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.pay1button_id).click()
        self.methods.wait_and_find_element_by_id(lk_conf.input_sms_code_id)

