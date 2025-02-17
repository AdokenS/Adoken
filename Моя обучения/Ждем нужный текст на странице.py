import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/explicit_wait2.html"

browser.get(link)

button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button3 = browser.find_element(By.ID, "book")
button3.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value").text
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(str(y))

button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(10)
browser.quit()


