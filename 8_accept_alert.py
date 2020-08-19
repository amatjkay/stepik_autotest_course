import math
import time

from selenium import webdriver

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

submit = driver.find_element_by_css_selector('button[type="submit"]')
submit.click()

confirm = driver.switch_to.alert
confirm.accept()

element = driver.find_element_by_css_selector('#input_value')
element_value = element.text
x = element_value

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

print('Результат расчета', calc(x))

input_answer = driver.find_element_by_css_selector('#answer')
input_answer.send_keys(calc(x))

submit = driver.find_element_by_css_selector('button[type="submit"]')
submit.click()

alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)

time.sleep(10)
driver.quit()
