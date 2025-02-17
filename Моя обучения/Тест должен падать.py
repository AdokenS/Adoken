from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name.send_keys("Adok")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name.send_keys("Sembaev")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys("adok.salam@gmail.com")
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    phone.send_keys("87758322048")
    address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
    address.send_keys("Atyrau")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()