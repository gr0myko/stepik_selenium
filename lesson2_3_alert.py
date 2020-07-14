import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector(".btn")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(result)
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
    


