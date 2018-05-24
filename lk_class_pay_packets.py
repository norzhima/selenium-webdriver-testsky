import lk_conf
from lk_class_login_rundom import LogInRundom
from time import sleep
from selenium.common.exceptions import TimeoutException as TE

class PayPackets(LogInRundom):

    def pay(self, packet_inst, payment_method, price_packet):
        self.choice_of_payment_method(packet_inst, payment_method, price_packet)
        self.methods.wait_and_find_element_by_xpath(lk_conf.checkout_button_xpath).click()
        return self.sum

    def choice_of_payment_method(self, packet_inst, payment_method, price_packet):
        if payment_method['type'] in ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']:
            self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.pay_w_acc).click()
            self.sum = self.required_values(payment_method, price_packet)
            self.methods.wait_and_find_element_by_id(lk_conf.input_a_id).send_keys(self.sum[0])
            self.methods.wait_and_find_element_by_id(lk_conf.input_b_id).send_keys(self.sum[1])
            if packet_inst != True:
                #and packet['innotrans']
                self.methods.wait_and_find_element_by_id(lk_conf.input_c_id).send_keys(self.sum[2])
            return self.sum
        else:
            self.selected_method = self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.pay_w_ps).click()
            if payment_method['type'] == "ameria":
                self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.pay_ameria_xpath).click()
                self.methods.wait_and_find_element_by_xpath_and_move("//div[@data-ps-id='56']/div/input").click()



    def required_values(self, payment_method, price_packet):
        if payment_method['type'] in ["a", 'ab', 'ac', 'abc']:
            self.a = price_packet - payment_method['pay_from_b'] - payment_method['pay_from_c']
            self.b = payment_method['pay_from_b']
            self.c = payment_method['pay_from_c']
            return [self.a, self.b, self.c]
        elif payment_method['type'] in ["b", 'bc']:
            self.a = payment_method['pay_from_a']
            self.b = price_packet - payment_method['pay_from_a'] - payment_method['pay_from_c']
            self.c = payment_method['pay_from_c']
            return [self.a, self.b, self.c]
        elif payment_method['type'] in ["c"]:
            self.a = payment_method['pay_from_a']
            self.b = payment_method['pay_from_b']
            self.c = price_packet - payment_method['pay_from_a'] - payment_method['pay_from_b']
            return [self.a, self.b, self.c]


    def w_ps_ameria(self):
        pass


    def check_packet(self, packet, payment_method):
        if packet['instalment'] == True:
            if packet['packet_id'] in lk_conf.exp_without_plus:
                self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.first_payment_25_xpath).click()
            if packet['packet_id'] in lk_conf.exp_with_plus:
                self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.first_payment_50_xpath).click()
            self.sum_list = self.packet_choose(packet['choose_packet_xpath'], lk_conf.url_checkout_inst % packet['packet_id'],
                               packet['price'], packet['count_shares'], payment_method, packet['instalment'])
            self.packet_instalment_payment(lk_conf.month_pay_instalment_xpath % packet['count_month'], payment_method)
            self.packet_sign_a_claim(self.sum_list, packet['price_all'], packet['instalment'], payment_method['type'], packet['price'])
        else:
            self.sum_list = self.packet_choose(packet['choose_packet_xpath'], lk_conf.url_checkout_simple % packet['packet_id'],
                               packet['price_all'], packet['count_shares'], payment_method, packet['instalment'])
            self.packet_sign_a_claim(self.sum_list, packet['price_all'], packet['instalment'], payment_method['type'])


    def packet_choose(self, packet_name, url_checkout, price_packet, count_shares, payment_method, packet_inst):
        self.main_balance_before_int = self.get_all_balance()
        self.methods.wait_and_find_element_by_xpath_and_move(packet_name).click()
        self.total_price = int(self.methods.wait_and_find_element_by_id(lk_conf.total_price_id).text.replace(' ', ''))
        self.assertEqual(url_checkout, self.driver.current_url)
        self.assertEqual(self.total_price, price_packet)
        self.sum_internal = self.pay(packet_inst, payment_method, price_packet)
        self.methods.wait_and_find_element_by_id(lk_conf.progress_start_id).click()
        self.methods.wait_and_find_element_by_xpath(count_shares)
        self.assertEqual(lk_conf.url_acceptance_page, self.driver.current_url)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.checkbox_icon_xpath).click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.button_buy_xpath).click()
        return self.sum_internal

    def packet_instalment_payment(self, count_month, payment_method):
        href_my_instalment = self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.href_my_instalment_xpath)
        self.assertEqual(lk_conf.url_pay_instalment, self.driver.current_url)
        href_my_instalment.click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.tab_myinstalment).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.checkout_myinstalment_xpath)
        self.assertEqual(lk_conf.section_myinstalment, self.driver.current_url)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.select_pay_instalment_xpath).click()
        self.methods.wait_and_find_element_by_xpath(count_month).click()
        self.id_instalment = self.methods.wait_and_find_element_by_xpath(lk_conf.last_instalment_xpath).get_attribute(
            lk_conf.name_attr_instalment_id)
        if payment_method['type'] == "b":
            self.methods.wait_and_find_element_by_xpath(lk_conf.select_a_or_b % self.id_instalment).click()
            self.methods.wait_and_find_element_by_xpath(lk_conf.select_b % self.id_instalment).click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.button_for_pay_instalment_xpath % self.id_instalment).click()

    def packet_sign_a_claim(self, sum, full_price_packet, packet_inst, payment_method, first_pay_price = 0):
        try:
            self.methods.wait_and_find_element_by_xpath(lk_conf.username_verif_data_xpath)
            self.methods.wait_and_find_element_by_xpath(lk_conf.requirement_xpath)
            sleep(3)  # временное решение
            self.sign = self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.sign_xpath)
            self.sign.click()
        except TE:
            pass
        self.methods.wait_and_find_element_by_xpath(lk_conf.section_my_certificates_xpath)
        self.assertTrue(self.driver.page_source.__contains__(lk_conf.section_my_certificates))
        self.assertEqual(lk_conf.url_my_certificates, self.driver.current_url)
        self.actual_result = self.get_all_balance()
        self.exp_result = self.expected_result(sum, full_price_packet, packet_inst, payment_method, first_pay_price)
        self.assertEqual(self.exp_result, self.actual_result)

    def get_all_balance(self):
        self.balance_a_int = self.get_balance(lk_conf.balance_a_xpath)
        self.balance_b_int = self.get_balance(lk_conf.balance_b_xpath)
        self.balance_c_int = self.get_balance(lk_conf.balance_c_xpath)
        return [self.balance_a_int, self.balance_b_int, self.balance_c_int]

    def get_balance(self, name_account):
        self.account =  self.methods.wait_and_find_element_by_xpath(name_account).text.replace(' ', '')
        self.account_balance = int(self.account[:-4])
        return self.account_balance

    def expected_result(self, sum, full_price_packet, packet_inst, payment_method, first_pay_price):
        if packet_inst == True:
            if payment_method == "b":
                sum[1] = sum[1] + (full_price_packet - first_pay_price)
            else:
                sum[0] = sum[0] + (full_price_packet - first_pay_price)
        self.result_a = self.main_balance_before_int[0] - sum[0]
        self.result_b = self.main_balance_before_int[1] - sum[1]
        self.result_c = self.main_balance_before_int[2] - sum[2]
        return [self.result_a, self.result_b, self.result_c]