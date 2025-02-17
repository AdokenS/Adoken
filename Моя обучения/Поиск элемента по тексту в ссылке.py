from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

x = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element(By.PARTIAL_LINK_TEXT, x)
link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Адок")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Сембаев")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Атырау")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Казахстан")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()

