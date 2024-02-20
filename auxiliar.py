import pyautogui
import time
from datetime import datetime

time.sleep(3)
print(pyautogui.position())


# img = pyautogui.locateCenterOnScreen('login2.jpg', confidence=0.7)
# print(img)
# pyautogui.click(img.x, img.y)

larguraInicial = 553
larguraFinal = 288
alturaInicial = 426
alturaFinal = 320

now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H.%M.%S")
nomeComprovante = "1" + "_boleto_" + "fies" + "_" + dt_string + ".jpg"

im = pyautogui.screenshot(region=(larguraInicial, alturaInicial, larguraFinal, alturaFinal))
im.save(nomeComprovante, 'jpeg')


#Point(x=543, y=291)
#Point(x=832, y=296)
#Point(x=543, y=799)
#Point(x=832, y=798)
