import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# URL y credenciales correctas
URL = "https://the-internet.herokuapp.com/login"
USER = "tomsmith"
PASS = "SuperSecretPassword!"

def get_driver(headless=False):  # headless=False para ver la ventana
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,800")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

def take_screenshot(driver, name):
    os.makedirs("evidencias", exist_ok=True)
    driver.save_screenshot(os.path.join("evidencias", name))

def test_login_exitoso():
    print("Iniciando prueba: Login exitoso...")
    d = get_driver(headless=False)
    try:
        d.get(URL)

        # Llenar campos
        d.find_element(By.ID, "username").send_keys(USER)
        d.find_element(By.ID, "password").send_keys(PASS)
        d.find_element(By.CSS_SELECTOR, "button.radius").click()

        # Esperar hasta que aparezca el mensaje
        flash = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        print("Mensaje recibido:", flash.text)
        assert "You logged into a secure area!" in flash.text
        take_screenshot(d, "login_exitoso.png")
        print("Prueba exitosa: Login correcto y mensaje validado.")
    finally:
        d.quit()

def test_login_invalido():
    print("Iniciando prueba: Login inválido...")
    d = get_driver(headless=False)
    try:
        d.get(URL)

        # Llenar campos con datos incorrectos
        d.find_element(By.ID, "username").send_keys("wrong")
        d.find_element(By.ID, "password").send_keys("wrong")
        d.find_element(By.CSS_SELECTOR, "button.radius").click()

        # Esperar hasta que aparezca el mensaje
        flash = WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        print("Mensaje recibido:", flash.text)
        assert "Your username is invalid!" in flash.text or "Your password is invalid!" in flash.text
        take_screenshot(d, "login_invalido.png")
        print("Prueba exitosa: Mensaje de error validado.")
    finally:
        d.quit()

if __name__ == "__main__":
    test_login_exitoso()
    test_login_invalido()
