import pyautogui
import os
import time
import mysql.connector
from datetime import datetime

# Abrir o navegador
def abrirNavegador():
    pyautogui.PAUSE = 2
    pyautogui.press("win")
    pyautogui.write("firefox")    
    pyautogui.press("enter")
    time.sleep(10)

# Abrir a celcoin
def abrirCelcoin():
    link = "https://app.celcoin.com.br/"
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(15)

def pagarBoleto(idBoleto, codigo, tipo, user):
    pyautogui.hotkey("alt", "1")
    time.sleep(5)
    pyautogui.write(codigo, interval=0.25)
    time.sleep(10)
    if((tipo == "compesa") or (tipo == "celpe") or (tipo == "fies")):
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)        
        pyautogui.press("enter")
        time.sleep(10)
    elif(tipo == "cartao"):
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)        
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)        
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.press("tab", presses=1)
        time.sleep(2)        
        pyautogui.press("tab", presses=1)
        time.sleep(2)
        pyautogui.press("tab", presses=1)
        time.sleep(2)          
        pyautogui.press("enter")
        time.sleep(5)        
    pyautogui.write("1612", interval=0.25)
    time.sleep(10)        

    if(1+1 == 2):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H.%M.%S")
        nomeComprovante = user + "_boleto_" + tipo + "_" + dt_string + ".pdf"

        salvarComprovante(tipo, user, nomeComprovante)
        boletoPago(idBoleto, nomeComprovante)

def boletoPago(idBoleto, nomeComprovante):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='celcoin'
    )
    cursor = conexao.cursor()
    comando = f'UPDATE boletos SET pago = "S", diaPagamento = now(), nomeComprovante = "{nomeComprovante}" where id = "{idBoleto}"'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()


def salvarComprovante(tipo, user, nomeComprovante):
    time.sleep(10)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    # Colocar a data, empresa e usuário no nome
    pyautogui.write(nomeComprovante, interval=0.25)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)



    # print("1")
    # pyautogui.press("tab", presses=5)
    # print("2")
    # time.sleep(5)
    # pyautogui.press("enter")   
    # time.sleep(5) 
    # pyautogui.press("tab", presses=3)
    # time.sleep(5)
    # pyautogui.press("enter")            

def buscarBoletos():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='celcoin'
    )

    cursor = conexao.cursor()
    comando = f'SELECT id, USER, codigoBoleto, valor, tipo, pago FROM boletos WHERE pagamentoAgendado <= CURDATE() AND pago = "N";'
    cursor.execute(comando)
    resultado =cursor.fetchall()

    #print("Resultado " + resultado.length())

    if not resultado:
        print("Nenhum boleto novo")
    else:
        idBoleto = resultado[0][0]
        user = resultado[0][1]
        codigo = resultado[0][2]
        tipo = resultado[0][4]

        cursor.close()
        conexao.close()
        time.sleep(5)

        abrirNavegador()
        abrirCelcoin()
        pagarBoleto(idBoleto, codigo, tipo, user)


buscarBoletos()

#pagarBoleto("00190000090337049301198047013176995000000006218", "compesa")
#pagarBoleto("10498.37030 97009.115045 00009.143652 8 95020000024813", "boleto")
#pagarBoleto(codigo, tipo)
#codigoCartao = "23794150099003486944750000211404600000000000000" # + "00000000000"
#pagarBoleto(codigoCartao, "cartao")
#pagarBoleto("26090340267542843413062600000004795020000002000", "celpe")

# Login
# Pagamento de contas
# Código
# Pin
# Comprovante
