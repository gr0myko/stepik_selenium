import math 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #wait until the price will be 100$
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element_by_id("book")
    book.click()

    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    submit = browser.find_element_by_id("solve")
    submit.click()
   
finally:
    time.sleep(10)
    browser.quit()
    