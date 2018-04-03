# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as TE
import lk_conf
import lk_priv_data
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import datetime
import inspect
import autoit
import sys
import platform


class LkswcTest(unittest.TestCase):
    PLATFORM = 'LINUX'
    BROWSER = 'chrome'
    #SAUCE_USERNAME ='norzhima_chagdurova'
    #SUACE_KEY = 'abba511b-d8f8-440b-9a01-f9729c6fff25'

    def setUp(self):
        ip_address = 'ondemand.saucelabs.com:80'
        #hub = 'http://' + ip_address + '/wd/hub'
        hub = 'http://10.133.8.249:4444/wd/hub'
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER
        desired_caps['maxInstances'] = 4
        desired_caps['maxSession'] = 6
        desired_caps['version'] = "any"


        #sauce_string = self.SAUCE_USERNAME + ':' + self.SUACE_KEY

        self.driver = webdriver.Remote(hub, desired_caps)#http://192.168.1.76:4444 #http://10.0.3.1:4444
        self.driver.set_window_size(1350, 700)
        self.driver.get(lk_priv_data.main_url)
        self.assertEqual(lk_conf.short_company_name, self.driver.title)
        self.change_language()

    def tearDown(self):
        self.driver.quit()

    def test_cashin_pm(self):
        self.autorization()
        self.deposit_account()
        if self.check_of_ps(lk_conf.ps_perfect_money_xpath, lk_conf.name_pm) == True:
            self.expect_visibility(lk_conf.wait_checkout_pm).click()
            self.assertIn(lk_conf.site_perfect_money, self.driver.current_url)



    def autorization(self):
        self.user = lk_priv_data.get_user()
        self.login(self.user['login'], self.user['password'])
        self.expect_visibility("//h3[contains(text(), '%s')]" % self.user['full_name'])
        self.assertEqual(lk_conf.full_company_name, self.driver.title)

    def login(self, lig_in, passw):
        self.expect_visibility(lk_conf.login_field_xpath).send_keys(lig_in)
        self.expect_visibility(lk_conf.passw_field_xpath).send_keys(passw)
        self.expect_visibility(lk_conf.login_button_xpath).click()

    def expect_visibility(self, path):
        #print(path)
        self.found_element = WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        return self.driver.find_element_by_xpath(path)

    def change_language(self):
        self.language_search = self.expect_visibility(lk_conf.language_search_xpath)
        if self.language_search.text == "EN":
            self.language_search.click()
            self.switching_to_ru = self.expect_visibility(lk_conf.switching_to_ru_xpath).click()
        self.expect_visibility(lk_conf.enter_the_systeme_xpath)

    def deposit_account(self, sum_cashin=lk_conf.sum_cashin_small):
        self.expect_visibility(lk_conf.banking_section_xpath).click()
        self.expect_visibility(lk_conf.deposit_account_section_xpath).click()
        self.expect_visibility(lk_conf.dep_acc_title_xpath)
        self.assertEqual(lk_conf.check_url_cashin, self.driver.current_url)
        self.expect_visibility_and_move(lk_conf.field_cashin_xpath).send_keys(sum_cashin)
        self.expect_visibility(lk_conf.deposit_button_xpath).click()

    def check_of_ps(self, ps_xpath, data):
        self.list_ps = self.search_all_ps()
        #print(self.list_ps)
        if data in self.list_ps:
            self.expect_visibility_and_move(ps_xpath).click()
            return True
        else:
            print("Платежная система", data, "выключена.")
            return False

    def expect_visibility_and_move(self, path):
        #print(path)
        self.found_element = WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((By.XPATH, path)))
        self.found_element = self.driver.find_element_by_xpath(path)
        self.element_top = self.driver.execute_script("return arguments[0].getBoundingClientRect()", self.found_element).get("top")
        self.page_off_set = self.driver.execute_script("return window.pageYOffset")
        self.inner = self.driver.execute_script("return window.innerHeight")
        self.top_and_off_set = self.element_top + self.page_off_set
        self.element_middle = self.top_and_off_set - (self.inner / 2)
        self.driver.execute_script("window.scrollTo(0, arguments[0])", self.element_middle)
        sleep(0.2)
        self.found_element.is_displayed()
        return self.driver.find_element_by_xpath(path)

    def search_all_ps(self):
        #Получаем спикок всех включенных платежных систем в виде значений атрибута 'data-code'.
        WebDriverWait(self.driver, lk_conf.delay).until(EC.visibility_of_element_located((By.XPATH, lk_conf.last_ps_xpath)))
        self.expect_visibility(lk_conf.you_were_billed_xpath)
        self.last_elem = self.expect_visibility(lk_conf.last_ps_xpath)
        self.all_ps = self.driver.find_elements_by_xpath(lk_conf.all_ps_xpath)
        self.list_ps_attribute = []
        for i in self.all_ps:
            self.list_ps_attribute.append(str(i.get_attribute(lk_conf.name_attribute)))
        return self.list_ps_attribute


if __name__ == "__main__":
    if len(sys.argv) > 1:
        LkswcTest.BROWSER = sys.argv.pop()
        LkswcTest.PLATFORM = sys.argv.pop()
    unittest.main()
