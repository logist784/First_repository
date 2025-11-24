from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 60)
wait.until(
    lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#image-container img"))
    == 4
)
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
print(f"Найдено картинок: {len(images)}")
third_img = images[2]
src_value = third_img.get_attribute("src")
print(src_value)

driver.quit()
