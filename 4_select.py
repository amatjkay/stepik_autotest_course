from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id('num1')
num2 = browser.find_element_by_id('num2')

num1_text = num1.text
num2_text = num2.text

sum = (int(num1_text) + int(num2_text))
print(sum)

select = Select(browser.find_element_by_id('dropdown'))
time.sleep(1)
select.select_by_value(f'{sum}')

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

time.sleep(10)
browser.quit()