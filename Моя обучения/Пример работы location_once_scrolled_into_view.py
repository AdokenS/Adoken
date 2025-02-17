from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(y))

checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
checkbox.click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radiobutton.location_once_scrolled_into_view
radiobutton.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.location_once_scrolled_into_view
button.click()

time.sleep(10)
browser.quit()