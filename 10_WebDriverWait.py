import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 12)

link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

card = driver.find_element_by_css_selector('.card')
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

button = driver.find_element_by_css_selector('#book')
button.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = driver.find_element_by_id('answer')
answer.send_keys(y)

submit = driver.find_element_by_css_selector('button[type="submit"]')
submit.click()

alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)

time.sleep(30)
driver.quit()

# driver.quit()
