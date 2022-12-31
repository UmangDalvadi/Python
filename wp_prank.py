
import random

import pyautogui as pg

import time


# apran_khunger

animal = ('chutiya', 'benchod', 'laude', 'madarchod',
          'motherfuker', 'bahen_ke_laude', 'teri_maa_ki_chut', )

time.sleep(10)

# apran_khunger

for i in range(50):

    a = random.choice(animal)

    pg.write(a)

    pg.press('enter')
