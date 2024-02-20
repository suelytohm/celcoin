import requests


def enviarArquivo():
    # URL da rota POST
    url = "https://test-boletos.onrender.com/upload/"

    # Caminho do arquivo que você deseja enviar
    caminho_do_arquivo = "comprovantes/suelytohm_boleto_cartao_29_12_2023_16.06.34.pdf"

    # Abrir o arquivo em modo binário
    with open(caminho_do_arquivo, 'rb') as arquivo:
        resposta = requests.post(url, files={'file': (caminho_do_arquivo, arquivo)})

    # Verificar o status da resposta
    if resposta.status_code == 200:
        print("Arquivo enviado com sucesso!")
    else:
        print(f"Erro ao enviar o arquivo. Código de status: {resposta.status_code}")
        print(resposta.text)

def enviarComprovanteWhatsapp(nomeComprovante, user, telefone):
    urlDownload = "https://boletos-a3ow.onrender.com/arquivo/"
    resposta = requests.get(f"http://localhost:3005/comprovante/{telefone}/{user}/{nomeComprovante}")

    # Verificar o status da resposta
    if resposta.status_code == 200:
        print("Envio do arquivo realizado com sucesso!")
    else:
        print(f"Erro ao enviar o arquivo. Código de status: {resposta.status_code}")
        print(resposta.text)


# enviarArquivo()
enviarComprovanteWhatsapp('suelytohm_boleto_cartao_29_12_2023_16.06.34.pdf', 'Suelytohm', '558791087013')
# enviarComprovanteWhatsapp('suelytohm_boleto_deposito_05_01_2024_14.05.02.pdf', 'Suelytohm', '558791087013')
