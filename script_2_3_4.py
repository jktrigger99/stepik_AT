from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    
    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла