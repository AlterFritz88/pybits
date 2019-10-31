from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Firefox()
browser.get(link)

try:
    input1 = browser.find_element_by_css_selector("input[class='form-control first']:required")
    input1.send_keys("ololo")
    input2 = browser.find_element_by_css_selector("input[class='form-control second']:required")
    input2.send_keys("ololo")
    input3 = browser.find_element_by_css_selector("input[class='form-control third']:required")
    input3.send_keys("ololo")
finally:
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


'''
inputs = browser.find_elements_by_css_selector("input[required]")
#inputs = browser.find_elements_by_tag_name('input')

for i in inputs:
    print(i)
    i.send_keys('ololo')
'''







'''
input1 = browser.find_element_by_tag_name('input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name('last_name')
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name('form-control.city')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
'''

