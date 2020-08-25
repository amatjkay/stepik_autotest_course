import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.fixture(scope="function")
def answer():
	answer = math.log(int(time.time()))
	yield answer


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_func(browser, link, answer):
	link = f"https://stepik.org/lesson/{link}/step/1"
	browser.implicitly_wait(20)
	browser.get(link)
	text_area = browser.find_element_by_tag_name('textarea')
	text_area.send_keys(f'{answer}')
	button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
	button.click()
	optional_feedback = browser.find_element_by_css_selector('.smart-hints__hint')
	optional_feedback_text = optional_feedback.text
	assert "Correct!" in optional_feedback_text
