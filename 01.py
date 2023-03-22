import time

from onlinehile import *
import pyautogui

def anvilac():
    click(530, 320)
    rightclick(530, 320)
    time.sleep(0.350)
    click(520, 396)
    time.sleep(0.25 )

def slot1(x,y):
    # slot1
    click(x,y)  #item select
    time.sleep(0.15)
    rightclick(x, y)  #item select
    time.sleep(0.1)
    rightclick(966, 654)   #scroll sabit kalacaktır.
    time.sleep(0.15)
    click(742, 408)  # confirm 1
    time.sleep(0.1)
    click(744, 478)  # confirm 2
    time.sleep(1)
    click(998,102)


slot1X = 660
slot1Y = 495

for x in range(7):
    anvilac()
    slot1(slot1X, slot1Y)
    slot1X = slot1X + 50

slot1X = 660
slot1Y = 545
for x in range(7):
    anvilac()
    slot1(slot1X, slot1Y)
    slot1X = slot1X + 50