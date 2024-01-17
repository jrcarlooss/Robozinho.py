from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

# Configurando opções do Chrome
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Função para executar o código
def executar_codigo():
    # Inicialize o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://200.20.53.11/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "rdCpf"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "rdCnpj"))).click()

        # Insira o CNPJ
        campo_cnpj = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCnpj")))
        campo_cnpj.send_keys("") #digitar CNPJ

        # Pressione "Tab" para mudar o foco
        pyautogui.press('tab')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtCpfUsuario"))).click()
        # Insira o CPF
        campo_cpf = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCpfUsuario")))
        campo_cpf.send_keys("") #digitar CPF

        # Pressione "Tab" novamente para mudar o foco
        pyautogui.press('tab')

        # Insira a senha
        campo_senha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtSenha")))
        campo_senha.send_keys("") #digitar senha

        pyautogui.press('tab')
        # Pressione "Enter" para enviar o formulário
        pyautogui.press('enter')
        pyautogui.sleep(5)
        driver.get("http://200.20.53.11/ControllerServlet?acao=cadastroModeloMtr")

        pyautogui.sleep(3)
        pyautogui.click(117, 454)  # coordenadas para click
        pyautogui.sleep(3)
        pyautogui.click(131, 459)
        pyautogui.sleep(3)
        pyautogui.click(613, 598)
        pyautogui.sleep(3)
        #pyautogui.hotkey('tab')
        pyautogui.typewrite("200")
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.sleep(2)

        campo_responsavel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtGeradorRespExpedicao")))
        campo_responsavel.send_keys("") #digitar Nome
        pyautogui.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.sleep(3)
        campo_cargo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtGeradorRespCargo")))
        campo_cargo.send_keys("") #digitar Função

        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnGravar")))
        button.click()
        pyautogui.sleep(3)

        botao_fechar = driver.find_element(By.XPATH, '/html/body/div[13]/div[1]/button')
        botao_fechar.click()

    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")
        raise

    finally:
        driver.quit()


for _ in range(1 ): # Executar o código 1 vezes
    executar_codigo()
