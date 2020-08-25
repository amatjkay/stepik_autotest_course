import time
import unittest
import colorama
from colorama import Fore, Back, Style
colorama.init()

from selenium import webdriver


class TestAbs(unittest.TestCase):

	def test_abs1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		first_name = browser.find_element_by_css_selector('.first_block .form-group > .first[required]')
		first_name.send_keys('FirstName')
		last_name = browser.find_element_by_css_selector('.first_block .form-group > .second[required]')
		last_name.send_keys('LastName')
		email = browser.find_element_by_css_selector('.first_block .form-group > .third[required]')
		email.send_keys('email@example.com')
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

	def test_abs2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		first_name = browser.find_element_by_css_selector('.first_block .form-group > .first[required]')
		first_name.send_keys('FirstName')
		last_name = browser.find_element_by_css_selector('.first_block .form-group > .second[required]')
		last_name.send_keys('LastName')
		email = browser.find_element_by_css_selector('.first_block .form-group > .third[required]')
		email.send_keys('email@example.com')
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
	unittest.main()


