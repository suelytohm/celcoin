import pyautogui
import os
import time
import mysql.connector
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d_%m_%Y_%H.%M.%S")
print("date and time =", dt_string)


# if((1 > 0) or (2 > 1)):
#     print("ok")
#     time.sleep(2)
#     pyautogui.write("10498.37030 97009.115045 00009.143652 8 95020000024813", interval=0.25)



# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='1234',
#     database='celcoin'
# )

# cursor = conexao.cursor()

# id_user = 1
# codigoBoleto = "82840000000-9 56160018012-700167276202-0 72606491215-7"
# tipo = "celpe"
# valor = 56.16

# comando = f'INSERT INTO boletos (USER, codigoBoleto, tipo, valor, pagamentoAgendado, pago) values ("{id_user}", "{codigoBoleto}", "{tipo}", {valor}, curdate(), "N")'
# cursor.execute(comando)
# conexao.commit()


# comando = f'SELECT id, USER, codigoBoleto, valor, tipo, pago FROM boletos WHERE pagamentoAgendado <= CURDATE() AND pago = "N";'
# cursor.execute(comando)
# resultado =cursor.fetchall()

# idBoleto = resultado[0][0]
# user = resultado[0][1]
# codigo = resultado[0][2]
# tipo = resultado[0][4]

# print(codigo, tipo, user)

# cursor.close()
# conexao.close()



#myScreenshot = pyautogui.screenshot()
#myScreenshot.save(dt_string + ".png")




def localizar(nomeImagem, clicar):
    tentativas = 5

    for _ in range(tentativas):
        imagem = pyautogui.locateOnScreen(nomeImagem, confidence=0.85)
        
        if imagem is not None:
            # A imagem foi encontrada, você pode prosseguir com o código apropriado
            print("Imagem encontrada nas coordenadas:", imagem.left, imagem.top)
            if (clicar):
                pyautogui.click(x=imagem.left, y=imagem.top)
            return True
            break  # Sai do loop se a imagem for encontrada

        # Se a imagem não for encontrada, aguarde um momento antes de tentar novamente
        pyautogui.sleep(1)

    if imagem is None:
        print("Imagem não encontrada após", tentativas, "tentativas.")
        return False

localizar('telaComprovante.jpg', False)