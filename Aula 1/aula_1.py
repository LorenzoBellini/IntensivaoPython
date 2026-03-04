"""
Passo a passo:
    1 - Entrar no site;
    2 - Fazer login (email e senha);
    3 - Cadastrar produto:
        3.1 - Abrir planilha para consulta;
        3.2 - Preencher os campos no site;
        3.3 - Repetir o processo para cada produto.
"""
# Importando as bibliotecas necessárias e definindo as variáveis

import pyautogui
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1 - Comandos para abrir o navegador e acessar o site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.sleep(2)
pyautogui.press("enter")
pyautogui.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.sleep(2)

# 2 - Fazer login e entrar no sistema

pyautogui.click(x=756, y=375)
pyautogui.write("email@exemplo.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")
pyautogui.sleep(2)
pyautogui.scroll(400)
pyautogui.click(x=837, y=255)

# 3 - Cadastrar produto
tabela = pd.read_csv("produtos.csv")
print(tabela)
# Por algum motivo eu preciso rodar o arquivo no integral interativo pra ele ler a pasta
# Quando clico em rodar ele roda o arquivo python na pasta Intensivao, e não na Aula 1
for linha in tabela.index:
    pyautogui.scroll(400)
    pyautogui.click(x=837, y=255)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if str(obs) != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(400)
    pyautogui.click(x=837, y=255)
