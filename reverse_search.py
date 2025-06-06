from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ⇨ Ime tvoje slike
image_name = "IMG_1474.JPEG"
image_path = os.path.abspath(image_name)

if not os.path.exists(image_path):
    print(f"❌ Slika '{image_name}' nije pronađena.")
    exit()

# 🔧 Pokretanje browsera
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

### --- GOOGLE IMAGES REVERSE SEARCH --- ###
print("🔍 Otvaram Google Images...")
driver.get("https://images.google.com/")
time.sleep(2)

# Klik na ikonicu za pretragu po slici
search_by_image_icon = driver.find_element(By.XPATH, "//a[@aria-label='Search by image']")
search_by_image_icon.click()
time.sleep(2)

# Klik na "Upload a file"
upload_tab = driver.find_element(By.XPATH, "//input[@type='file']")
upload_tab.send_keys(image_path)

print("✅ Slika je poslata na Google Images.")
time.sleep(5)

### --- YANDEX IMAGES REVERSE SEARCH --- ###
print("🔍 Otvaram Yandex Images...")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://yandex.com/images/")
time.sleep(3)

camera_icon = driver.find_element(By.CLASS_NAME, "input__camera")
camera_icon.click()
time.sleep(2)

upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys(image_path)

print("✅ Slika je poslata na Yandex Images.")
print("🎯 Rezultati su otvoreni u browseru.")