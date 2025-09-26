from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CALC = "https://testsheepnz.github.io/BasicCalculator.html"

def get_driver():
    o = Options(); o.add_argument("--headless=new"); o.add_argument("--window-size=1280,800")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)

def calcular(a, b, operacion="Add"):
    d = get_driver()
    try:
        d.get(CALC)
        d.find_element(By.ID, "number1Field").send_keys(str(a))
        d.find_element(By.ID, "number2Field").send_keys(str(b))
        select = d.find_element(By.ID, "selectOperationDropdown")
        for option in select.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == operacion:
                option.click(); break
        d.find_element(By.ID, "calculateButton").click()
        return d.find_element(By.ID, "numberAnswerField").get_attribute("value")
    finally:
        d.quit()

if __name__ == "__main__":
    print("5 + 7 =", calcular(5,7,"Add"))
    print("8 / 0 =", calcular(8,0,"Divide"))
