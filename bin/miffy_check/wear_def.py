
from matrix import *

import LED_display as LMD
import threading

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return


def wear_cloth(arr_final, arr_cloth):
    for i in range(32):
        for j in range(16):
            if ( arr_cloth[i][j] != 0 ):
                 arr_final[i][j] = arr_cloth[i][j]
    return arr_final

LED_init()
import time


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range( m.get_dx()):
            if array[y][x] == 0:
                LMD.set_pixel(y, x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, x, 0)
            elif array[y][x] == 2:
                LMD.set_pixel(y, x, 2)
            elif array[y][x] == 3:
                LMD.set_pixel(y, x, 3)    
            elif array[y][x] == 4:
                LMD.set_pixel(y, x, 4)
            elif array[y][x] == 5:
                LMD.set_pixel(y, x, 6)
            elif array[y][x] == 7:
                LMD.set_pixel(y, x, 7)
            else:
                continue
            print()
	    



iScreen = Matrix(arr)
oScreen = Matrix(iScreen)

draw_matrix(oScreen)


arr = wear_cloth(arr, a)
iScreen = Matrix(arr)
time.sleep(1)

oScreen.paste(iScreen, 0, 0)
draw_matrix(oScreen)	
time.sleep(10000)


