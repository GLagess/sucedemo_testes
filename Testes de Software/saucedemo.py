from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    print("🔄 Acessando o site...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    print("👤 Preenchendo usuário...")
    driver.find_element(By.ID, "user-name").send_keys("visual_user")
    time.sleep(1.5)

    print("🔒 Preenchendo senha...")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1.5)

    print("➡️ Fazendo login...")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    print("🛒 Adicionando produto ao carrinho...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    if cart_count == '1':
        print("✅ Produto adicionado com sucesso!")

        # Acessa o carrinho
        print("🧺 Acessando o carrinho...")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        print("🧾 Carrinho exibido! Você pode verificar no navegador.")
    else:
        print("❌ Erro ao adicionar o produto.")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")
