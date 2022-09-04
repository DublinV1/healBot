
    



#help


#ToDo List:

#get bot to interface with the game.
#create folder in wow -> interface -> addons

#Select between the different party members:
#	F1-F5

# Use healing abilities
#	Priest spams Flash of Light and or higher ranking spells

#Be able to check other party members to see if they need healing
#	make sure the bot can follow us
#		eventually make the bot smart enough to walk to other party members to be in range of healing.

#Logic for damage over time and threat to differentiate different spells to use.

import macro
import time
import pyautogui
import keyboard
import random
import screenscan
###  MOVEMENT  ###

""" WoW DEFAULTS

Move and Steer: Middle Mouse
Move Forward: W
Move Backward: S
Turn Left: A
Turn Right: D
Strafe Left: Q
Strafe Right: E
Jump: Spacebar
Sit/Move Down: X
Sheath/Unsheath: Z
Toggle Autorun: Num Lock
Toggle Run/Walk: Num Pad/
"""

def Test():
	time.sleep(1.5)
	pyautogui.press('w')

#Test()

screenscan.locateOnScreen()