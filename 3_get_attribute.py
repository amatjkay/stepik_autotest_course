from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

element_img = browser.find_element_by_id('treasure')
element_img_value = element_img.get_attribute('valuex')
x = element_img_value
print('Значение:', x)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

print('Результат расчета', calc(x))

input_answer = browser.find_element_by_css_selector('#answer')
input_answer.send_keys(calc(x))
robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()
robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()
submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()


time.sleep(30)
browser.quit()