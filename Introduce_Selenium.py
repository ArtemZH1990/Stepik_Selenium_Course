import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


#Locators (Same on few pages)
first_name ="//input[@name='first_name']"
last_name = "//input[@name='last_name']"
city = "//input[@class='form-control city']"
country = "//input[@id='country']"
submit_button = "//button[@class='btn btn-default']"
new_submit_button = "//button[@class='btn']"     # XPATH for task_4
pole_loc_for_task_3 = "//input[@type='text']"    #Get use for task_3

#Locators for suninjuly registration form_1 page
first_name_mandatory = "//input[@placeholder='Input your first name']"
last_name_mandatory = "//input[@placeholder='Input your last name']"
email_pole_manadatory = "//input[@placeholder='Input your email']"
congrats_text_XPATH = "//div[@class='container']"
congrats_text = "Congratulations! You have successfully registered!"


class Basic:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def basic_settings(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    # Getters

    def suninjuly_form_url_getter(self):
        return "http://suninjuly.github.io/simple_form_find_task.html"

    def suninjuly_find_link_url_getter(self):
        return "http://suninjuly.github.io/find_link_text"

    def suninjuly_huge_form_url_getter(self):
        return "http://suninjuly.github.io/huge_form.html"

    def suninjuly_find_XPATH_form_url_getter(self):
        return "http://suninjuly.github.io/find_xpath_form"

    def suninjuly_registration_form_url_getter(self):
        return "http://suninjuly.github.io/registration1.html"

    def suninjuly_registration_form_without_login_pole_url_getter(self):
        return "http://suninjuly.github.io/registration2.html"

    # Actions

    def form_sign(self):
        self.driver.find_element(By.XPATH, first_name).send_keys("Art")
        self.driver.find_element(By.XPATH, last_name).send_keys("Zh")
        self.driver.find_element(By.XPATH, city).send_keys("Vtb")
        self.driver.find_element(By.XPATH, country).send_keys("Blr")

    def registration_form_sign(self):
        self.driver.find_element(By.XPATH, first_name_mandatory).send_keys("Art")
        self.driver.find_element(By.XPATH, last_name_mandatory).send_keys("Zh")
        self.driver.find_element(By.XPATH, email_pole_manadatory).send_keys("123")

    def quit(self):
        self.driver.quit()


def task_1():
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_form_url_getter())
    browser.form_sign()
    browser.driver.find_element(By.XPATH, submit_button).click()
    browser.quit()

def task_2():
    need_string = str(math.ceil(math.pow(math.pi, math.e)*10000))
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_find_link_url_getter())
    browser.driver.find_element(By.LINK_TEXT, need_string).click()
    browser.form_sign()
    browser.driver.find_element(By.XPATH, submit_button).click()
    time.sleep(2)
    browser.quit()

def task_3():
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_huge_form_url_getter())
    elements = browser.driver.find_elements(By.XPATH, pole_loc_for_task_3)
    [i.send_keys("123") for i in elements]
    browser.driver.find_element(By.XPATH, submit_button).click()
    browser.quit()

def task_4():
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_find_XPATH_form_url_getter())
    browser.form_sign()
    elements = browser.driver.find_elements(By.XPATH, new_submit_button)
    [i.click() for i in elements]
    browser.quit()

def task_5():
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_registration_form_url_getter())
    browser.registration_form_sign()
    browser.driver.find_element(By.XPATH, submit_button).click()
    success = browser.driver.find_element(By.XPATH, congrats_text_XPATH).text
    assert congrats_text == success

#Check this one task
def task_6():
    browser = Basic()
    browser.basic_settings()
    browser.driver.get(browser.suninjuly_registration_form_without_login_pole_url_getter())
    browser.registration_form_sign()
    browser.driver.find_element(By.XPATH, submit_button).click()
    success = browser.driver.find_element(By.XPATH, congrats_text_XPATH).text
    assert congrats_text == success


task_6()











