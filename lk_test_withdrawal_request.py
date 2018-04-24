import unittest
from selenium import webdriver
import lk_conf
import lk_priv_data
#import lk_find
#import lk_methods
from time import sleep
from selenium.webdriver.common.alert import Alert
from lk_class_login_simple import LkLogInSimple

class TestWithdrawalRequest(LkLogInSimple):

    def test_withdrawal_request(self):
        self.add_requisites()
        self.withdrawal_request()
        self.methods.get_and_insert_code()


    def add_requisites(self):
        self.methods.banking_section()
        self.methods.wait_and_find_element_by_xpath(lk_conf.req_section_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.req_title_section_xpath)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.req_button_add).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.title_requisites_xpath)
        self.all_rows_before = len(self.methods.wait_and_find_elements_by_xpath(lk_conf.all_rows_table_requisites_xpath))
        self.len_td_table = len(self.methods.wait_and_find_elements_by_xpath(lk_conf.len_td_table_xpath))
        if int(self.len_td_table) == 1:
            self.all_rows_before_and_one = int(self.all_rows_before)
        else:
            self.all_rows_before_and_one = int(self.all_rows_before) + 1
        self.methods.wait_and_find_element_by_id(lk_conf.open_mymodal_id)
        self.methods.wait_and_find_element_by_id(lk_conf.select_req_type_id)
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_req_visa_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.input_req_number_visa_id).send_keys(
            lk_priv_data.req_number_visa)
        self.methods.wait_and_find_element_by_id(lk_conf.input_req_name_owner_id).send_keys(lk_conf.req_name_owner)
        self.methods.wait_and_find_element_by_id(lk_conf.input_req_expiry_id).send_keys(lk_conf.req_expiry)
        self.methods.wait_and_find_element_by_id(lk_conf.button_add_requisites_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.added_rows % self.all_rows_before_and_one)
        self.all_rows_after = int(len(self.methods.wait_and_find_elements_by_xpath(lk_conf.all_rows_table_requisites_xpath)))
        self.assertEqual(self.all_rows_before_and_one, self.all_rows_after)

    def withdrawal_request(self):
        sleep(2)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.banking_section_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.withdrawal_request_xpath).click()
        self.count_request = len(self.methods.wait_and_find_elements_by_xpath(lk_conf.count_request_xpath))
        if self.count_request == 1:
            pass
        else:
            self.text_del = self.methods.wait_and_find_element_by_xpath(lk_conf.text_del_xpath).text
            if self.text_del == lk_conf.exp_text_for_del:
                self.methods.wait_and_find_element_by_xpath(lk_conf.link_for_delete).click()
                Alert(self.driver).accept()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.data_type_visamaster_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.input_sum_request_id).send_keys(lk_conf.sum_small)
        self.methods.wait_and_find_element_by_id(lk_conf.button_request_id).click()

