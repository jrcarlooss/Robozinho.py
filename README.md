# Robozinho.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# Inicialize o driver do Chrome
driver = webdriver.Chrome()

try:
    driver.get("http://200.20.53.11/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "rdCpf"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "rdCnpj"))).click()
    

    # Insira o CNPJ
    campo_cnpj = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCnpj")))
    campo_cnpj.send_keys("")

    # Pressione "Tab" para mudar o foco
    pyautogui.press('tab')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtCpfUsuario"))).click()
    # Insira o CPF
    campo_cpf = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCpfUsuario")))
    campo_cpf.send_keys("")

    # Pressione "Tab" novamente para mudar o foco
    pyautogui.press('tab')

    # Insira a senha
    campo_senha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtSenha")))
    campo_senha.send_keys("")


    pyautogui.press('tab')
    # Pressione "Enter" para enviar o formulário
    pyautogui.press('enter')
    driver.get("http://200.20.53.11/ControllerServlet?acao=cadastroModeloMtr")

    pyautogui.click(117, 454)#coordenadas para click
    pyautogui.click(131, 459)
    pyautogui.click(613, 598)
    pyautogui.hotkey('tab')
    pyautogui.sleep(1)
    pyautogui.typewrite("200")

    campo_responsavel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtGeradorRespExpedicao")))
    campo_responsavel.send_keys("")

    campo_cargo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtGeradorRespCargo")))
    campo_cargo.send_keys("")

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnGravar")))
    button.click()
    pyautogui.sleep(3)
    pyautogui.click(645, 360)
    pyautogui.sleep(3)

    
    # Espere o usuário posicionar o cursor na tela
    #input("Posicione o cursor onde você deseja identificar as coordenadas e pressione Enter...")

# Obtenha as coordenadas atuais do cursor
    #oordenadas = pyautogui.position()
    
    #print(f"Coordenadas X: {coordenadas[0]}, Coordenadas Y: {coordenadas[1]}")


    
    # Aguarde a entrada do usuário
    input("Pressione Enter para encerrar o teste...")

except Exception as e:
    print(f"Ocorreu uma exceção: {e}")

finally:
    driver.quit()

