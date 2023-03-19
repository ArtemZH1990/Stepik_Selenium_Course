import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Basic locators for all task
x_param = "//span[@id='input_value']"
input_pole = "//input[@id='answer']"


# URL
url_for_task_1 = "https://suninjuly.github.io/math.html"
url_for_task_2 = "http://suninjuly.github.io/get_attribute.html"
url_for_task_3 = "http://suninjuly.github.io/selects1.html"
url_for_task_4 = "https://SunInJuly.github.io/execute_script.html"
url_for_task_5 = "http://suninjuly.github.io/file_input.html"
url_for_task_6 = "http://suninjuly.github.io/alert_accept.html"
url_for_task_7 = "http://suninjuly.github.io/redirect_accept.html"
url_for_task_8 = "http://suninjuly.github.io/explicit_wait2.html"


# Locators for task_5
first_name_pole_task_5 = "//input[@placeholder='Enter first name']"
last_name_pole_task_5 = "//input[@placeholder='Enter last name']"
email_pole_task_5 = "//input[@placeholder='Enter email']"
choose_file_task_5 = "//input[@id='file']"
submit_button_task_5 = "//button[@class='btn btn-primary']"    #Valid for task_6


# Task_8 locators
price = "//h5[@id='price']"
book_button = "//button[@id='book']"
submit_button_task_8 = "//button[@id='solve']"


# Others locators
robot_check_box = "//input[@id='robotCheckbox']"
robot_rule_radio_button = "//input[@id='robotsRule']"
robot_rule_radio_button_ver_2 = "//label[@for='robotsRule']"
submit_button = "//button[@class='btn btn-default']"
submit_button_for_task_4 = "//button[@class='btn btn-primary']"
num_1_task_3 = "//span[@id='num1']"
num_2_task_3 = "//span[@id='num2']"
select_pole_task_3 = "//select[@class='custom-select']"
chest = "//img[@id='treasure']"
submit_button_task_7 = "//button[@class='trollface btn btn-primary']"


def basic_settings():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def task_1():
    driver = basic_settings()
    driver.get(url_for_task_1)
    x = int(driver.find_element(By.XPATH, x_param).text)
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, robot_check_box).click()
    driver.find_element(By.XPATH, robot_rule_radio_button).click()
    driver.find_element(By.XPATH, submit_button).click()
    driver.quit()

def task_2():
    driver = basic_settings()
    driver.get(url_for_task_2)
    x = int(driver.find_element(By.XPATH, chest).get_attribute('valuex'))
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, robot_check_box).click()
    driver.find_element(By.XPATH, robot_rule_radio_button).click()
    driver.find_element(By.XPATH, submit_button).click()
    time.sleep(5)
    driver.quit()

def task_3():
    driver = basic_settings()
    driver.get(url_for_task_3)
    num_1 = int(driver.find_element(By.XPATH, num_1_task_3).text)
    num_2 = int(driver.find_element(By.XPATH, num_2_task_3).text)
    amount = num_1 + num_2

    # driver.find_element(By.XPATH, select_pole_task_3).click()
    # driver.find_element(By.XPATH, f"//option[@value='{amount}']").click()

    # Select help to work with dropdown-box!!!!
    select = Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))
    select.select_by_value(f"{amount}")

    driver.find_element(By.XPATH, submit_button).click()
    driver.quit()

def task_4():
    driver = basic_settings()
    driver.get(url_for_task_4)
    x = int(driver.find_element(By.XPATH, x_param).text)
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, robot_check_box).click()

    action = ActionChains(driver)
    action.scroll_by_amount(0, 200).perform()

    time.sleep(0.1)    #?????? I don't know why it's work like that
    robot_rule_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, robot_rule_radio_button)))
    robot_rule_btn.click()

    driver.find_element(By.XPATH, submit_button_for_task_4).click()

def task_5():
    driver = basic_settings()
    driver.get(url_for_task_5)
    driver.find_element(By.XPATH, first_name_pole_task_5).send_keys('Art')
    driver.find_element(By.XPATH, last_name_pole_task_5).send_keys('Zh')
    driver.find_element(By.XPATH, email_pole_task_5).send_keys('123')

    #current_dir = os.path.abspath(os.path.dirname(__file__))
    #file_path = os.path.join(current_dir, r"C:\Users\ART\Desktop\se.txt")
    # print(os.path.abspath(os.path.dirname(__file__)))
    # print(os.path.abspath(__file__))

    driver.find_element(By.XPATH, choose_file_task_5).send_keys(r"C:\Users\ART\Desktop\se.txt")
    driver.find_element(By.XPATH, submit_button_task_5).click()
    driver.quit()

def task_6():
    driver = basic_settings()
    driver.get(url_for_task_6)
    driver.find_element(By.XPATH, submit_button_task_5).click()
    confirm = driver.switch_to.alert
    confirm.accept()
    x = int(driver.find_element(By.XPATH, x_param).text)
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, submit_button_task_5).click()
    driver.quit()

def task_7():
    driver = basic_settings()
    driver.get(url_for_task_7)
    driver.find_element(By.XPATH, submit_button_task_7).click()
    window_data = driver.window_handles
    driver.switch_to.window(window_data[1])
    x = int(driver.find_element(By.XPATH, x_param).text)
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, submit_button_task_5).click()
    driver.quit()

def task_8():
    driver = basic_settings()
    driver.get(url_for_task_8)
    wait = WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.XPATH, price), "$100"))
    driver.find_element(By.XPATH, book_button).click()
    x = int(driver.find_element(By.XPATH, x_param).text)
    driver.find_element(By.XPATH, input_pole).send_keys(calc(x))
    driver.find_element(By.XPATH, submit_button_task_8).click()
    driver.quit()




