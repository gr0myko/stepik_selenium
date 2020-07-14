import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link) 

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result) 
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

    