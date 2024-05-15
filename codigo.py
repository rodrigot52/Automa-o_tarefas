# Passo a passo do projeto

# 1. Abrir o sistema da emrpesa
    # https://dlp.hashtagtreinamentos.com/python/intesivao/login

# para instalar: pip istall pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5
# Abrir o navegador (Chrome)
pyautogui.press("win")
time.sleep(5)
pyautogui.write("chrome")
time.sleep(5)
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=499, y=431)
time.sleep(10)
# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")
# esperar o site carregar
time.sleep(20)

# 2. Fazer Login no site

pyautogui.click(x=513, y=376)
pyautogui.write("rodrigosantos@google.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(10)

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4. Cadastrar um produto
# str = string = texto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do codigo do produto
    pyautogui.click(x=461, y=280)
    # preencher o codigo
    pyautogui.write(codigo)
    # passar pro proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha , "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passar pro proximo campo
    pyautogui.press("tab")
    # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)