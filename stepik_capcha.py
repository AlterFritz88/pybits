from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Firefox()
browser.get(link)

x = int(browser.find_element_by_id('treasure').get_attribute('valuex'))
result = str(math.log(abs(12*math.sin(x))))

input_1 = browser.find_element_by_id('answer')
input_1.send_keys(result)

check_1 = browser.find_element_by_id('robotCheckbox')
check_1.click()

option1 = browser.find_element_by_id("robotsRule")
option1.click()

button = browser.find_element_by_css_selector('body > div > form > div > div > button')

button.click()