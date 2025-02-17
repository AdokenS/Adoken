import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
first_name.send_keys("Adok")
last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
last_name.send_keys("Sembaev")
email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
email.send_keys("adok.salam@gmail.com")

filetxt = browser.find_element(By.ID, "file")
filetxt.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()