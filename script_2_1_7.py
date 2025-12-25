from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_box = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure_box.get_attribute("valuex")
    y = calc(x)
    
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    
    time.sleep(1)
    
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox1.click()
    
    time.sleep(1)
    
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton1.click()
    
    time.sleep(1)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
