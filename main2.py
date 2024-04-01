import pyautogui
import time
import requests
import socketio
from datetime import datetime
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
SO = os.getenv('SO')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
PIN = os.getenv('PIN')
SERVER = os.getenv('API_URL')
APLICACAO_LOTERICA = os.getenv('APLICACAO_LOTERICA')

sio = socketio.Client()

api_url = SERVER + "/boletos"
pronto = False

def localizar(nomeImagem, clicar):
    tentativas = 5

    for _ in range(tentativas):
        imagem = pyautogui.locateOnScreen(nomeImagem, confidence=0.85)
        
        if imagem is not None:
            # A imagem foi encontrada, você pode prosseguir com o código apropriado
            print(f"Imagem {nomeImagem} encontrada nas coordenadas:", imagem.left, imagem.top)
            if (clicar):
                # pyautogui.click(x=imagem.left, y=imagem.top)
                pyautogui.click(x=imagem.left + imagem.width / 2, y=imagem.top + imagem.height / 2)

            return True
            break  # Sai do loop se a imagem for encontrada

        # Se a imagem não for encontrada, aguarde um momento antes de tentar novamente
        pyautogui.sleep(2)

    if imagem is None:
        print(f"Imagem {nomeImagem} não encontrada após", tentativas, "tentativas.")
        return False

# Abrir o navegador
def abrirNavegador():
    pyautogui.PAUSE = 2
    pyautogui.press("win")
    pyautogui.write("firefox")
    pyautogui.press("enter")
    time.sleep(10)

# Abrir a celcoin
def abrirCelcoin():
    link = APLICACAO_LOTERICA
    pyautogui.write(link)
    pyautogui.press("enter")

    #time.sleep(15)
    if(localizar('verificacao.jpg', False)):
        print("Verificação de conexão 1")
        pyautogui.sleep(2)
        if(localizar('checkbox.jpg', True)):
            pyautogui.sleep(2)
            print("Verificação de bot")

    if(localizar('verificacao2.jpg', False)):
        print("Verificação de conexão 2")
        pyautogui.sleep(2)
        if(localizar('checkbox.jpg', True)):
            pyautogui.sleep(2)
            print("Verificação de bot")

    elif(localizar('login2.jpg', False)):
        pyautogui.press("tab")
        pyautogui.write(LOGIN, interval=0.15)
        pyautogui.press("tab")
        pyautogui.write(PASSWORD, interval=0.15)
        pyautogui.press("enter")
        if(localizar('inicio.jpg', False)):
            return True

    elif(localizar('inicio.jpg', False)):
        return True

def pagarBoleto(idBoleto, codigo1, tipo, user, valor, telefone):
    pyautogui.hotkey("alt", "1")
    time.sleep(2)
    pyautogui.write(codigo1, interval=0.5)
    time.sleep(4)    

    if(localizar('ValorAberto.jpg', True)):
        print("Inserir valor do pagamento")
        pyautogui.press("tab", presses=1)
        time.sleep(1)
        pyautogui.press("tab", presses=1)
        time.sleep(1)
        pyautogui.press("tab", presses=1)
        time.sleep(1)        
        pyautogui.write(valor, interval=0.25)
        # INSERIR O VALOR DO BOLETO AQUI ------------------------------------------------------------------------------------------------------------
        pyautogui.press("tab", presses=1)
        time.sleep(1)
        pyautogui.press("tab", presses=1)
        time.sleep(1)        
        pyautogui.press("enter")
        time.sleep(5)    

    # if((tipo == "cartao") or (tipo == "deposito")):
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)        
    #     pyautogui.write(valor, interval=0.25)
    #     # INSERIR O VALOR DO BOLETO AQUI ------------------------------------------------------------------------------------------------------------
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)        
    #     pyautogui.press("enter")
    #     time.sleep(5)

    if(localizar('PagarConta.jpg', True)):
        print("Pagar conta")
        time.sleep(5)


        # pyautogui.press("tab", presses=1)
        # time.sleep(1)        
        # pyautogui.press("tab", presses=1)
        # time.sleep(1)
        # pyautogui.press("tab", presses=1)
        # time.sleep(1)          
        # pyautogui.press("enter")

    # elif((tipo == "compesa") or (tipo == "celpe") or (tipo == "fies")  or (tipo == "internet") or (tipo == "detran")):
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)
    #     pyautogui.press("tab", presses=1)
    #     time.sleep(1)        
    #     pyautogui.press("enter")
    #     time.sleep(5)

    pyautogui.write(PIN, interval=0.25)
    time.sleep(10)        

    if(localizar('telaComprovante.jpg', False)):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H.%M.%S")
        dataPagamento = now.strftime("%d/%m/%Y")
        nomeComprovante = user + "_boleto_" + tipo + "_" + dt_string + ".pdf"

        boletoPago(idBoleto, dt_string, nomeComprovante)

        if(SO == 'windows'):
            salvarComprovanteWindows(tipo, user, nomeComprovante, telefone, valor, dataPagamento)
        else:
            salvarComprovanteLinux(tipo, user, nomeComprovante, telefone, valor, dataPagamento)
        time.sleep(2)
        enviarComprovanteWhatsapp({'telefone': telefone, 'usuario': user, 'nomecomprovante': nomeComprovante, 'datapagamento': dataPagamento, 'tipoPagamento': tipo, 'valor': valor})
        pyautogui.hotkey("ctrl", "w")


def boletoPago(idBoleto, dataPagamento, nomeComprovante):
    dados_atualizados = {
        "pago": "S",
        "nomeComprovante": nomeComprovante
    }

    # Requisição PUT para atualizar o boleto
    response = requests.put(f"{api_url}/{idBoleto}", json=dados_atualizados)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print("Boleto atualizado com sucesso!")
    else:
        print(f"A solicitação falhou com o código de status: {response.status_code}")

def salvarComprovanteLinux(tipo, user, nomeComprovante, telefone, valor, dataPagamento):
    print(tipo)



def salvarComprovanteWindows(tipo, user, nomeComprovante, telefone, valor, dataPagamento):
    if(localizar('btnImprimir.jpg', True)):
        print("Imprimir comprovante")
        time.sleep(0.5)

        if(localizar('btnSalvarComprovante.jpg', True)):
            print("Salvando comprovante")
            time.sleep(1)

            pyautogui.write(nomeComprovante, interval=0.15)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)

def enviarComprovanteWhatsapp(data):
    sio.emit('enviar comprovante', data)

def buscarBoletos():
    response = requests.get(api_url)

    if response.status_code == 200:
        boletos = response.json()  # Os dados da API são interpretados como JSON

        if boletos:
            for boleto in boletos:
                print(boleto['valor'])
                
                abrirNavegador()
                
                if(abrirCelcoin()):
                    pagarBoleto(boleto['id'], boleto['codigoboleto'], boleto['tipo'], boleto['usuario'], boleto['valor'], boleto['telefone'])
                else:
                    print('fim')
        else:
            print("Nenhum boleto novo")

    else:
        print("Erro na requisição: Código", response.status_code)

@sio.event
def connect():
    print("Conectado ao servidor Socket.IO")
    buscarBoletos()

@sio.event
def disconnect():
    print("Desconectado do servidor Socket.IO")
    time.sleep(3600)


@sio.on('novo boleto')
def on_message(data):
    print("Buscando novo boleto")
    buscarBoletos()


@sio.on('enviar comprovante')
def on_enviarComprovante(data):
    print('comprovante')
    print(data)

    telefone = data['telefone']
    usuario = data['usuario']
    nomeComprovante = data['nomecomprovante']

sio.connect(SERVER + "/")

while True:
    time.sleep(1)

# Login ✔
# Pagamento de contas ✔
# Código ✔
# Pin ✔
# Comprovante ✔
# OK ✔