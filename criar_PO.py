import pyautogui as pag
import pyscreeze
import time

def main_criar_PO():
    abrir_nova_PO()
    preencher_dados_fornecedor("404325440001")
    preencher_site_deposito("SP", "RICH")

    pag.moveTo(1752, 949, duration=1)
    pag.click()

def abrir_nova_PO():
    #clicando no botão de atualizar a página para os botões voltarem ao padrão
    pag.moveTo(1770, 205, duration=1)
    pag.click()

    #tempo de carregar a página
    time.sleep(4)


    posicaoBotaoNovo = pag.locateOnScreen("BotaoNovo.png")
    pag.moveTo(posicaoBotaoNovo, duration=1)
    pag.click()

def preencher_dados_fornecedor(cpf):
    pag.PAUSE = 1

    #clicar em "Conta do Fornecedor"
    pag.moveTo(1363, 424, duration=2)
    pag.click(clicks=2)

    #clicar no CPF
    pag.moveTo(396, 452, duration=1)
    pag.click(clicks=2)
    #escrever o cpf
    time.sleep(1.5)
    pag.write(cpf)
    #clicar em "aplicar"
    pag.moveTo(297, 717, duration=0.5)
    pag.click()
    #clicar no cpf
    pag.moveTo(343, 497 ,duration=1)
    pag.click(clicks=2)

def preencher_site_deposito(site, deposito=''):
    pag.PAUSE = 1

    #mover a tela para baixo, até dar para ve os campos de site e deposito
    pag.moveTo(1661,445, duration=1)
    pag.scroll(-300)

    #clicar em "Site"
    pag.moveTo(1690, 665, duration=1)
    pag.click(clicks=2)
    #escrever o site correspondente
    pag.write(site)
    pag.press("enter")

    if deposito != '':
        #ir para o campo de depósito
        pag.press("tab")
        time.sleep(1)
        #selecionar o depósito correspondente
        pag.write(deposito)
        pag.press("enter")
        time.sleep(1)