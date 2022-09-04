import pyautogui
import time

def screensize():
   size = pyautogui.size()
   print(size)

def locateOnScreen():

    renewLocation = pyautogui.locateOnScreen('spell_holy_renew.png', confidence=0.75)# returns (left, top, width, height) of first place it is found
    print(renewLocation)

'''
while 1:
    if pyautogui.locateOnScreen('ability_mount_charger.png', confidence=0.75) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I can't see it")
        time.sleep(0.5)
'''
# screensize() # test screensize function remove # and run
# locateOnScreen() # test location of renew
