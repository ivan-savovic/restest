from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Putanja do slike
image_file = "IMG_1474.JPEG"
image_path = os.path.abspath(image_file)

if not os.path.exists(image_path):
    print(f"❌ Slika nije pronađena: {image_file}")
    exit()

# Pokretanje Chrome browsera
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Otvori direktno Yandex Image Search upload stranicu
print("🔍 Otvaram Yandex Images upload...")
driver.get("https://yandex.com/images/search?rpt=imageview")
time.sleep(2)

# Pronađi polje za upload slike i pošalji je
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys(image_path)

print("✅ Slika poslata na Yandex.")
print("📂 Otvori browser za rezultate.")

# Ostavimo browser da ostane otvoren 20 sekundi
time.sleep(20)