from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Kasutame tavalist standardset Seleniumi
driver = webdriver.Chrome()
driver.maximize_window()

print("--- ÜLESANNE 1: Otsing DuckDuckGo-s (Õpetaja lubatud alternatiiv) ---")
try:
    # 1. Ava leht
    driver.get("https://duckduckgo.com")
    time.sleep(2)

    # 2. Leia otsingukast ja sisesta oma nimi
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Roven")
    
    # 3. Esita otsing
    search_box.submit()
    print("Otsing nimega 'Roven' käivitatud.")
    time.sleep(3)
    
    # 4. Tee screenshot tulemustest
    driver.save_screenshot("minu_otsing.png")
    print("Ülesanne 1 tehtud! Screenshot salvestatud kausta nimega 'minu_otsing.png'.")

except Exception as e:
    print("Viga Ülesandes 1:", e)


print("\n--- ÜLESANNE 2: Tsitaatide kraapimine ---")
try:
    driver.get("https://quotes.toscrape.com")
    time.sleep(1)
    
    quotes = driver.find_elements(By.CLASS_NAME, "text")
    authors = driver.find_elements(By.CLASS_NAME, "author")
    
    print("\nLeitud tsitaadid terminalis:")
    for i in range(len(quotes)):
        print(f'"{quotes[i].text}" - {authors[i].text}')
    print("Ülesanne 2 tehtud!")

except Exception as e:
    print("Viga Ülesandes 2:", e)


print("\n--- ÜLESANNE 3: Elementide lisamine ja kustutamine ---")
try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)
    
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for i in range(5):
        add_button.click()
        time.sleep(0.1)
    print("Lisatud 5 elementi.")
        
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    for button in delete_buttons:
        button.click()
        time.sleep(0.1)
    print("Kõik 5 elementi uuesti kustutatud. Ülesanne 3 tehtud!")

except Exception as e:
    print("Viga Ülesandes 3:", e)


print("\n--- ÜLESANNE 4: Sisselogimise vorm ---")
try:
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)
    
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    
    success_text = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in success_text:
        print("TEST ÕNNESTUS: Edukalt sisse logitud! Ülesanne 4 tehtud!")
    else:
        print("TEST EBAÕNNESTUS: Sisselogimise teadet ei leitud.")

except Exception as e:
    print("Viga Ülesandes 4:", e)


print("\n--- ÜLESANNE 5: Navigatsioon ja Checkboxid ---")
try:
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(1)
    
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    time.sleep(1)
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")
    for box in checkboxes:
        if not box.is_selected():
            box.click()
    print("Mõlemad kastid märgitud.")
    time.sleep(1)
    
    driver.back()
    print("Navigeeritud tagasi pealehele. Ülesanne 5 tehtud!")

except Exception as e:
    print("Viga Ülesandes 5:", e)

print("\n--- KÕIK SELENIUMI ÜLESANDED ON LÕPETATUD! ---")
driver.quit()