import lk_conf
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Find:
    def __init__(self, driver):
        self.driver = driver
        self.id = By.ID
        self.xpath = By.XPATH

    #Ожидает появления элемента и возвращает его
    # Поиск по id
    def element_by_id(self, path):
        self.wait(path, self.id)
        return self.driver.find_element_by_id(path)

    #Ожидает появления элемента, скроллит страницу и возвращает его
    # Поиск по id
    def element_by_id_and_move(self, path):
        self.wait(path, self.id)
        self.elem = self.driver.find_element_by_id(path)
        self.move(self.elem)
        return self.driver.find_element_by_id(path)

    #Ожидает появления списка элементов и возвращает его
    # Поиск по id
    def elements_by_id(self, path):
        self.wait(path, self.id)
        return self.driver.find_elements_by_id(path)

    #Ожидает появления списка элементов, скроллит страницу и возвращает его
    # Поиск по id
    def elements_by_id_and_move(self, path):
        self.wait(path, self.id)
        self.elem = self.driver.find_elements_by_id(path)
        self.move(self.elem)
        return self.driver.find_elements_by_id(path)


    #Ожидает появления элемента и возвращает его
    # Поиск по xpath
    def element_by_xpath(self, path):
        self.wait(path, self.xpath)
        return self.driver.find_element_by_xpath(path)

    #Ожидает появления элемента, скроллит страницу и возвращает его
    # Поиск по xpath
    def element_by_xpath_and_move(self, path):
        self.wait(path, self.xpath)
        self.elem = self.driver.find_element_by_xpath(path)
        self.move(self.elem)
        return self.driver.find_element_by_xpath(path)

    #Ожидает появления списка элементов и возвращает его
    # Поиск по xpath
    def elements_by_xpath(self, path):
        self.wait(path, self.xpath)
        return self.driver.find_elements_by_xpath(path)

    #Ожидает появления списка элементов, скроллит страницу и возвращает его
    # Поиск по xpath
    def elements_by_xpath_and_move(self, path):
        self.wait(path, self.xpath)
        self.elem = self.driver.find_elements_by_xpath(path)
        self.move(self.elem)
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


class Pay:
    def pay_account_a(self):
        pass

    def pay_account_b(self):
        pass

    def pay_account_c(self):
        pass

    def pay_account_ab(self):
        pass

    def pay_account_ac(self):
        pass

    def pay_account_bc(self):
        pass

    def pay_account_abc(self):
        pass

    def pay_w_ps_megapolis(self):
        pass

    def pay_w_ps_megapolis_apree(self):
        pass

    def pay_w_ps_tinkoff(self):
        pass

    def pay_w_ps_tinkoff_agree(self):
        pass

    def pay_w_ps_ameria(self):
        pass













