from selenium import webdriver
import time
link="http://suninjuly.github.io/registration2.html"
browser=webdriver.Firefox()
browser.get(link)

input1=browser.find_element_by_xpath("//input[@placeholder='Ââåäèòå èìÿ']")
input1.send_keys("Dasha")

input2=browser.find_element_by_xpath("//input[@placeholder='Ââåäèòå ôàìèëèþ']")
input2.send_keys("Byk")

input3=browser.find_element_by_xpath("//input[@placeholder='Ââåäèòå Email']")
input3.send_keys("123@email.com")

button=browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)
welcome_text_elt=browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Ïîçäðàâëÿåì! Âû óñïåøíî çàðåãèñòèðîâàëèñü!" == welcome_text