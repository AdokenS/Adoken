from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(y))

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(10)
browser.quit()

