from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Firefox()
browser.get(link)

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)
sum = str(num1 + num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum)

button = browser.find_element_by_css_selector('body > div > form > button')
button.click()