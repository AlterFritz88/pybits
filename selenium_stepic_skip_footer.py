from selenium import webdriver
import math

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Firefox()
browser.get(link)


x = int(browser.find_element_by_id('input_value').text)
result = str(math.log(abs(12*math.sin(x))))

input_1 = browser.find_element_by_id('answer')
input_1.send_keys(result)

check_box = browser.find_element_by_id('robotCheckbox')
check_box.click()


browser.execute_script("window.scrollBy(0, 100);")
option1 = browser.find_element_by_id("robotsRule")
option1.click()


button = browser.find_element_by_css_selector('body > div > form > button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)




button.click()