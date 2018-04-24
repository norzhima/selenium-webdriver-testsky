import lk_conf
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import lk_priv_data
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import StaleElementReferenceException as SERE
import datetime
import inspect


class MethodsFroCls:
    def __init__(self, driver):
        self.driver = driver

    def change_language(self):
        language_search = self.wait_and_find_element_by_xpath(lk_conf.language_search_xpath)
        if language_search.text == "EN":
            language_search.click()
            self.wait_and_find_element_by_xpath(lk_conf.switching_to_ru_xpath).click()
            self.wait_and_find_element_by_xpath(lk_conf.enter_the_systeme_xpath)

    def debug_panel(self):
        try:
            self.wait_and_find_element_by_id(lk_conf.debug_toolbar_id)
            self.wait_and_find_element_by_xpath(lk_conf.debug_minimize_xpath).click()
        except TE:
            pass

    #Ожидает появления элемента и возвращает его
    # Поиск по id
    def wait_and_find_element_by_id(self, path):
        self.wait(path, By.ID)
        return self.driver.find_element_by_id(path)

    #Ожидает появления элемента, скроллит страницу и возвращает его
    # Поиск по id
    def wait_and_find_element_by_id_and_move(self, path):
        self.wait(path, By.ID)
        elem = self.driver.find_element_by_id(path)
        self.move(elem)
        return self.driver.find_element_by_id(path)

    #Ожидает появления списка элементов и возвращает его
    # Поиск по id
    def wait_and_find_elements_by_id(self, path):
        self.wait(path, By.ID)
        return self.driver.find_elements_by_id(path)

    #Ожидает появления списка элементов, скроллит страницу и возвращает его
    # Поиск по id
    def wait_and_find_elements_by_id_and_move(self, path):
        self.wait(path, By.ID)
        elem = self.driver.find_elements_by_id(path)
        self.move(elem)
        return self.driver.find_elements_by_id(path)


    #Ожидает появления элемента и возвращает его
    # Поиск по xpath
    def wait_and_find_element_by_xpath(self, path):
        self.wait(path, By.XPATH)
        return self.driver.find_element_by_xpath(path)

    #Ожидает появления элемента, скроллит страницу и возвращает его
    # Поиск по xpath
    def wait_and_find_element_by_xpath_and_move(self, path):
        self.wait(path, By.XPATH)
        elem = self.driver.find_element_by_xpath(path)
        self.move(elem)
        return self.driver.find_element_by_xpath(path)

    #Ожидает появления списка элементов и возвращает его
    # Поиск по xpath
    def wait_and_find_elements_by_xpath(self, path):
        self.wait(path, By.XPATH)
        return self.driver.find_elements_by_xpath(path)

    #Ожидает появления списка элементов, скроллит страницу и возвращает его
    # Поиск по xpath
    def wait_and_find_elements_by_xpath_and_move(self, path):
        self.wait(path, By.XPATH)
        elem = self.driver.find_elements_by_xpath(path)
        self.move(elem)
        return self.driver.find_elements_by_xpath(path)

    def wait(self, path, method):
        WebDriverWait(self.driver, lk_conf.delay).until(
            EC.visibility_of_element_located((method, path)))

    def move(self, elem):
        self.element_top = self.driver.execute_script("return arguments[0].getBoundingClientRect()",
                                                      elem).get("top")
        self.page_off_set = self.driver.execute_script("return window.pageYOffset")
        self.inner = self.driver.execute_script("return window.innerHeight")
        self.top_and_off_set = self.element_top + self.page_off_set
        self.element_middle = self.top_and_off_set - (self.inner / 2)
        self.driver.execute_script("window.scrollTo(0, arguments[0])", self.element_middle)
        sleep(0.5)
        elem.is_displayed()

    def autorization(self):
        user = lk_priv_data.get_user()
        self.login(user['login'], user['password'])
        self.wait_and_find_element_by_xpath(lk_conf.username_in_lk % user['full_name'])
        #print(self.user['login'])

    def login_simple(self, login_simple=lk_priv_data.login_for_test, pasw_simple=lk_priv_data.passw_for_test, name_sample=lk_priv_data.full_name_for_test):
        self.login(login_simple, pasw_simple)
        self.wait_and_find_element_by_xpath(lk_conf.username_in_lk % name_sample)

    def login(self, log_in, passw):
        self.wait_and_find_element_by_xpath(lk_conf.login_field_xpath).send_keys(log_in)
        self.wait_and_find_element_by_xpath(lk_conf.passw_field_xpath).send_keys(passw)
        self.wait_and_find_element_by_xpath(lk_conf.login_button_xpath).click()

    def open_gmail(self):
        self.driver.get(lk_priv_data.mail_url)
        self.wait_and_find_element_by_id(lk_conf.login_for_gmail_id).send_keys(lk_priv_data.login_for_gmail)
        self.wait_and_find_element_by_xpath(lk_conf.confirm_auth_button_xpath).click()
        self.wait_and_find_element_by_xpath(lk_conf.password_for_gmail_xpath).send_keys(lk_priv_data.password_for_gmail)
        self.wait_and_find_element_by_xpath(lk_conf.confirm_auth_button_xpath).click()
        try:
            self.wait_and_find_element_by_xpath(lk_conf.check_new_email_xpath).click()
        except TE:
            print("No new messages")

    def expect_message(self):
        sleep(180) #Ожидание поступления письма на почту

    def save_src_png(self, name_def):
        self.now = datetime.datetime.now()
        self.scr = str(self.now.year) + '_' + str(self.now.month) + '_' + str(self.now.day) + '_' + str(
            self.now.hour) + str(self.now.minute) + '_' + name_def + '.png'
        self.driver.save_screenshot(self.scr)
    def get_funcname(self):
        return inspect.stack()[1][3]

    def open_in_new_window_mail(self):
        self.expect_message()
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_and_insert_code(self):
        try:
            self.open_in_new_window_mail()
            self.open_gmail()
            self.insert_code()
        except SERE:
            print("Wrong email selected")

    def insert_code(self):
        self.last_message = self.wait_and_find_element_by_xpath_and_move(lk_conf.element_with_code_xpath)
        self.confirmation_code = self.last_message.text[-5:]
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.wait_and_find_element_by_id(lk_conf.input_sms_code_id).send_keys(self.confirmation_code)
        self.wait_and_find_element_by_id(lk_conf.button_sms_code_id).click()
        self.wait_and_find_element_by_id(lk_conf.transfer_success_id)

    def banking_section(self):
        self.wait_and_find_element_by_xpath(lk_conf.banking_section_xpath).click()





