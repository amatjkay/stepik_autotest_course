import time
import math

from selenium import webdriver

'''
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
time.sleep(2)
input_value = browser.find_element_by_xpath('//*[@id="input_value"]')
x = input_value.text
print('Текст значения:', x)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

print('Результат расчета', calc(x))

input_answer = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)

input_answer.send_keys(calc(x))

robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()
robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()
submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

time.sleep(10)
browser.quit()
