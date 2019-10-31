from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Firefox()
browser.get(link)

input_1 = browser.find_element_by_name('firstname')
input_1.send_keys('Sashko')
input_2 = browser.find_element_by_name('lastname')
input_2.send_keys('Bu')
input_3 = browser.find_element_by_name('email')
input_3.send_keys('alpl@ss.ru')

import os

element = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'data.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)

button = browser.find_element_by_css_selector('body > div > form > button')
button.click()

