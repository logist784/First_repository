from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(2)
    success_message = driver.find_element(By.CLASS_NAME, "success")
    print("Текст с зеленой плашки:", success_message.text)
    time.sleep(2)

finally:
    driver.quit()
