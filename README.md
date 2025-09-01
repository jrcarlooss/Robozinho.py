# 🤖 Automação de Preenchimento de Formulário Web

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-orange)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.54-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Um script em **Python** que automatiza o login e o preenchimento de formulários em um site específico. Ele utiliza **Selenium** para interagir com elementos da página e **PyAutoGUI** para manipulações de teclado e mouse.

---

## ⚡ Funcionalidades

- 🔹 Acessa o site e realiza login automático.
- 🔹 Preenche campos de **CNPJ**, **CPF**, **senha** e outros dados de formulário.
- 🔹 Interage com botões, caixas de texto e navegação de página.
- 🔹 Permite executar múltiplas vezes para automação repetitiva.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Selenium** – automação de navegadores.
- **PyAutoGUI** – manipulação de teclado, mouse e GUI.
- **ChromeDriver** – necessário para controlar o navegador Chrome.

---

## ⚙️ Como usar

1. Instale as bibliotecas necessárias:

```bash
pip install selenium pyautogui

campo_cnpj.send_keys("")          # Digitar CNPJ
campo_cpf.send_keys("")           # Digitar CPF
campo_senha.send_keys("")         # Digitar senha
campo_responsavel.send_keys("")   # Digitar nome do responsável
campo_cargo.send_keys("")         # Digitar função/cargo

python main.py                    #Executar 

