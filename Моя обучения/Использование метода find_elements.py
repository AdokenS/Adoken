from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

browser = webdriver.Chrome()
browser.get(link)

elements = browser.find_elements(By.TAG_NAME, "input")

for element in elements:
    element.send_keys("Стану тестировщиком")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()
