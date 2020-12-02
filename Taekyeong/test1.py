from matrix import *
from all_t import *
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

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()


        

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range( m.get_dx()):
            if array[y][x] == 0:
                LMD.set_pixel(y, x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, x, 1)
            elif array[y][x] == 2:
                LMD.set_pixel(y, x, 2)
            elif array[y][x] == 3:
                LMD.set_pixel(y, x, 3)    
            elif array[y][x] == 4:
                LMD.set_pixel(y, x, 4)
            elif array[y][x] == 5:
                LMD.set_pixel(y, x, 5)
            elif array[y][x] == 6:
                LMD.set_pixel(y, x, 6)
            elif array[y][x] == 7:
                LMD.set_pixel(y, x, 7)
            else:
                continue
            print()
	    
i = 0	
cloth_arr = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14]
oScreen = Matrix(cloth_arr[i])
while(True):
	key = input("enter key")
	if key == 'r':
		i += 1
		oScreen = Matrix(cloth_arr[i])

	draw_matrix(oScreen)

	
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
'''if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()'''


        
