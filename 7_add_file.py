import time
import os

from selenium import webdriver

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

firstname = driver.find_element_by_name('firstname')
lastname = driver.find_element_by_name('lastname')
email = driver.find_element_by_name('email')
file = driver.find_element_by_id('file')

firstname.send_keys("Иван")
lastname.send_keys("Петров")
email.send_keys("www@pochta.ru")
file.send_keys(os.getcwd() + '/file.txt')

submit = driver.find_element_by_css_selector('button[type="submit"]')
submit.click()

alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)

time.sleep(10)
driver.quit()
