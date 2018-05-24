from lk_class_base import LkBase
import lk_conf


class LkPsMethods(LkBase):

    def popup_swift_alert(self):
        self.methods.wait_and_find_element_by_xpath(lk_conf.popup_accept_swift_alert_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.swift_alert_success_id).click()

    def payment_swift(self, select_currency="no", val=lk_conf.choose_val_gbp_xpath):
        self.methods.wait_and_find_element_by_xpath(lk_conf.choose_the_curr_for_payment_xpath)
        if select_currency == "yes":
            self.methods.wait_and_find_element_by_xpath_and_move(val).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.download_from_verification_swift_id).click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.accept_swift_xpath).click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.submit_swift_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_swift_page_xapth)

    def deposit_account(self):
        self.methods.banking_section()
        self.methods.wait_and_find_element_by_xpath(lk_conf.deposit_account_section_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.dep_acc_title_xpath)

    def check_of_ps(self,  ps_id, tab, sum_cashin=lk_conf.sum_small):
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.field_cashin_id).send_keys(sum_cashin)
        self.methods.wait_and_find_element_by_id(lk_conf.deposit_button_id).click()
        self.methods.wait_and_find_element_by_xpath_and_move(tab).click()
        list_ps = self.search_all_ps()
        if ps_id in list_ps:
            self.methods.wait_and_find_element_by_id_and_move(ps_id).click()
            self.methods.wait_and_find_element_by_id_and_move(lk_conf.pay_invoice_id).click()
            return True
        else:
            print("PS", ps_id, "disabled")
            return False

    def search_all_ps(self):
        #Получаем спикок всех включенных платежных систем в виде значений атрибута 'id'.
        all_ps = self.methods.wait_and_find_elements_by_xpath(lk_conf.all_ps_xpath)
        list_ps_attribute = []
        for i in all_ps:
            list_ps_attribute.append(str(i.get_attribute(lk_conf.name_attribute)))
        return list_ps_attribute

    def checkout_advcash(self):
        self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_advcash)

    def checkout_cripto(self):
        self.methods.wait_and_find_element_by_xpath(lk_conf.wait_checkout_cryptonator)

    def checkout_impex_trading(self, popup_accept, success):
        self.methods.wait_and_find_element_by_xpath_and_move(popup_accept).click()
        self.methods.wait_and_find_element_by_id_and_move(success).click()
        self.methods.wait_and_find_element_by_id(lk_conf.wait_checkout_trading_impex_id)

