from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

chest = browser.find_element(By.ID, "treasure")
chest_x = chest.get_attribute("valuex")

xx = calc(chest_x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(xx))

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()
radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()