# -*- coding: utf-8 -*-
from EnviarComprovanteWhatsapp import EnviarWhatsapp


# wp = EnviarWhatsapp()
# EnviarWhatsapp.abrirWhatsapp("suelytohm_boleto_deposito_03_01_2024_14.27.19.pdf", "5587991087013")


nomeComprovante = "suelytohm_boleto_deposito_05_01_2024_14.05.02.pdf"

wp = EnviarWhatsapp()
EnviarWhatsapp.mensagem()
# pyautogui.hotkey("ctrl", "w")