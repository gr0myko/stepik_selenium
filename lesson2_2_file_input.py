from selenium import webdriver
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link) 
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Popov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ivanpopov@gmail.com")
    file_input = browser.find_element_by_id("file")
    file_input.send_keys(file_path)
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
