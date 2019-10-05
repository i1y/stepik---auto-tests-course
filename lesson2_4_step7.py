from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
'''
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. 
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
'''
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    check = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value").text
    number = calc(x)
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element_by_id("answer").send_keys(number)
    button.click()






finally:
    time.sleep(15)
    browser.quit()

