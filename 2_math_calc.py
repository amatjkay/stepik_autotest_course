from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
print(y)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()

robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

time.sleep(30)
browser.quit()



