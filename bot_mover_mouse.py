import pyautogui as pag
import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
    
# para adicionar a biblioteca do pyautogui cole o seguinte comando em seu cmd ( py -m pip install pyautogui )


