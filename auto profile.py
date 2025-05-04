from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

# Set up Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

user_id = 54144011

print("Press 'Q' to go to the next Roblox inventory page.")
print("Press 'ESC' to quit.")

# Load initial page
driver.get(f"https://www.roblox.com/users/{user_id}/inventory/#!/accessories")

while True:
    if keyboard.is_pressed('q'):
        user_id += 1
        url = f"https://www.roblox.com/users/{user_id}/inventory/#!/accessories"
        print(f"Redirecting to: {url}")
        driver.get(url)
        time.sleep(0.3)  # Prevent accidental multiple triggers

    elif keyboard.is_pressed('esc'):
        print("Exiting.")
        break
