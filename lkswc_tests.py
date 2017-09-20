# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import lkswc_config

class LkswcTest(unittest.TestCase):

    def setUp(self):

        if lkswc_config.default_browser is "Chrome":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(chrome_options=self.options)
        else:
            self.driver = webdriver.Firefox()
        self.driver.get(lkswc_config.main_url)
        self.assertIn("SkyWay", self.driver.title)
        WebDriverWait(self.driver, lkswc_config.delay).until(
            EC.presence_of_all_elements_located((By.XPATH, lkswc_config.language_search_xpath)))
        self.language_search = self.driver.find_element_by_xpath(lkswc_config.language_search_xpath)
        if self.language_search.text == "EN":
            self.language_search.click()
            WebDriverWait(self.driver, lkswc_config.delay).until(
                EC.visibility_of_element_located((By.XPATH, lkswc_config.switching_to_ru_xpath)))
            self.switching_to_ru = self.driver.find_element_by_xpath(lkswc_config.switching_to_ru_xpath).click()
        self.assertTrue(self.driver.page_source.__contains__("Вход в систему"))

    def tearDown(self):
        self.driver.quit()

    def test_authorization(self):
        self.autorization(lkswc_config.login, lkswc_config.password)

    def autorization(self, login, passw):
        self.login_field = self.driver.find_element_by_xpath(lkswc_config.login_field_xpath).send_keys(lkswc_config.login)
        self.passw_field = self.driver.find_element_by_xpath(lkswc_config.passw_field_xpath).send_keys(lkswc_config.password)
        self.login_button = self.driver.find_element_by_xpath(lkswc_config.login_button_xpath).click()
        WebDriverWait(self.driver, lkswc_config.delay).until(EC.presence_of_element_located(
            (By.XPATH, lkswc_config.username_xpath)))
        self.assertEqual("SkyWay Capital", self.driver.title)
        self.assertTrue(self.driver.page_source.__contains__(lkswc_config.username))
        return True




if __name__ == "__main__":
    unittest.main(verbosity=2)