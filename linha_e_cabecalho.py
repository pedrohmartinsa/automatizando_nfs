import pyautogui as pag
import time

def main_linha_e_cabecalho():
    apagar_linha()
    preencher_dados_cabecalho("TI", "TELEC-COM")

def apagar_linha():
    pag.PAUSE = 1

    time.sleep(2)
    #garantir que a página esteja no padrão
    pag.moveTo(775, 710, duration=1)
    pag.scroll(1000)
    pag.scroll(-500)
    #mover para a linha e selecionar ela
    pag.moveTo(143,790, duration=1)
    pag.click()
    # #mover para a lixeira e excluir linha
    pag.moveTo(635, 696, duration=1)
    pag.click()

def preencher_dados_cabecalho(centroDeCustos, tipoDeOperacao):
    pag.PAUSE = 1
    #mover para abrir o cabeçalho
    pag.moveTo(232, 582, duration=1)
    pag.click()

    # #scrollar até o centro de custos e operação
    time.sleep(1)
    pag.moveTo(704, 687, duration=1)
    pag.scroll(-1800)

    # #preencher o centro de custos
    pag.moveTo(331, 647, duration=1)
    pag.click()
    pag.write(centroDeCustos)
    time.sleep(2)
    pag.press("enter")

    #preencher o tipo de operação
    pag.scroll(-300)
    pag.moveTo(274, 914, duration=2)
    pag.click()
    time.sleep(2)
    pag.write(tipoDeOperacao)
    pag.press("enter")

    #confirmar
    pag.moveTo(1126, 550, duration=1.5)
    pag.click()

    #salvar
    pag.moveTo(235, 211, duration=1.5)
    pag.click()

# def preencher_dados_linha(numeroDeItem, valor):
