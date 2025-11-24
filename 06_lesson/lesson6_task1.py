from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    success_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    text = success_element.text
    print(text)

finally:
    driver.quit()
