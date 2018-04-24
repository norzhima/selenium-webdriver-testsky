import lk_conf
import lk_priv_data
from time import sleep
import autoit
from autoit.autoit import AutoItError as AIE
from lk_class_login_simple import LkLogInSimple

class TestVerification(LkLogInSimple):

    def setUp(self):
        self.assertEqual(lk_conf.short_company_name, self.driver.title)
        self.methods.login_simple(lk_priv_data.login_for_verif, lk_priv_data.passw_for_verif, lk_priv_data.full_name_for_verif)
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def test_verification(self):
        self.checkout_section_personal()
        self.verification_personal_data()
        self.verification_passport_data()
        self.verification_registration_address()
        try:
            self.verification_uploading_of_the_doc()
        except AIE:
            print("Without downloading documents")

    def checkout_section_personal(self):
        sleep(2)
        self.settings_section = self.methods.wait_and_find_element_by_xpath(lk_conf.settings_section_xpath)
        self.settings_section.is_displayed()
        self.settings_section.click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.verification_section_xpath).click()
        self.fill = self.methods.wait_and_find_element_by_xpath(lk_conf.fill_forms_xpath)
        sleep(1)
        self.fill.click()

    def verification_personal_data(self):
        self.methods.wait_and_find_element_by_id(lk_conf.verif_field_ln_ru_id).send_keys(lk_conf.verif_ln_ru)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.verif_field_n_ru_id).send_keys(lk_conf.verif_n_ru)
        self.methods.wait_and_find_element_by_id(lk_conf.verif_field_ln_en_id).send_keys(lk_conf.verif_ln_en)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.verif_field_n_en_id).send_keys(lk_conf.verif_n_en)
        self.methods.wait_and_find_element_by_xpath(lk_conf.checkbox_female_xpath).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_birthday_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_birthday_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.select_birthmonth_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_birthmonth_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.select_birthyear_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_birthyear_count_xpath).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_birthplace_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_birthplace_country_xpath).click()
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.button_next_passport_xpath).click()
        self.select_persondoc = self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_persondoc_id)

    def verification_passport_data(self):
        self.select_persondoc.click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_persondoc_type_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.field_persondoc_num_id).send_keys(lk_conf.persondoc_num)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_persondoc_day_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_persondoc_day_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.select_persondoc_month_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_persondoc_month_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.select_persondoc_year_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_persondoc_year_count_xpath).click()
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.field_persondoc_who_issue_id).send_keys(lk_conf.persondoc_who_issue)
        self.methods.wait_and_find_element_by_xpath_and_move(lk_conf.button_next_address_xpath).click()
        self.selectaddress_region = self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_address_region_id)

    def verification_registration_address(self):
        self.selectaddress_region.click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_address_region_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.select_address_citytype_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_address_citytype_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.field_city_name_id).send_keys(lk_conf.city_name)
        self.methods.wait_and_find_element_by_id_and_move(lk_conf.select_address_streettype_id).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.select_address_streettype_count_xpath).click()
        self.methods.wait_and_find_element_by_id(lk_conf.field_address_street_id).send_keys(lk_conf.address_street_name)
        self.methods.wait_and_find_element_by_id(lk_conf.field_address_house_id).send_keys(lk_conf.house_number)
        self.methods.wait_and_find_element_by_xpath(lk_conf.button_finish_xpath).click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.section_download_xpath)

    def verification_uploading_of_the_doc(self):
        for i in range(2):
            self.download_image()
            i += 1
        self.methods.wait_and_find_element_by_xpath(lk_conf.upload_confirm_xpath).click()
        sleep(2)
        self.button_confirm = self.methods.wait_and_find_element_by_id(lk_conf.button_confirm_id)
        sleep(2)
        self.button_confirm.click()
        self.methods.wait_and_find_element_by_xpath(lk_conf.finish_header_verif_xpath)
        self.assertEqual(self.driver.current_url, lk_conf.personal_list_link)

    def download_image(self):
        self.button_choose = self.methods.wait_and_find_element_by_xpath(lk_conf.button_choose_xpath).click()
        sleep(1)
        autoit.win_wait(lk_conf.autoit_title, lk_conf.autoit_wait)
        autoit.control_focus(lk_conf.autoit_title, lk_conf.autoit_control_edit)
        autoit.control_send(lk_conf.autoit_title, lk_conf.autoit_control_edit, lk_conf.autoit_image_path)
        autoit.control_click(lk_conf.autoit_title, lk_conf.autoit_control_button)
        self.methods.wait_and_find_element_by_xpath(lk_conf.button_download_xpath).click()
        sleep(3)
