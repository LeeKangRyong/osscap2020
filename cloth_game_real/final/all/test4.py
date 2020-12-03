from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
from random import *
from option import *
#Configuration for the matrix

'''
mytext = str(3) + str(4)
offscreen_canvas.Clear()
len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,mytext)
offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


'''
'''
is_answer = False

while True:

	mul_1 = randint(1,9)
	mul_2 = randint(1,9)
	mytext = str(mul_1)+ " "+"X"+" "+  str(mul_2)
	while is_answer == False:
		key = input("Enter key")
		if (key ==' r'):
			mul_1 = randint(1,9)

			mul_2 = randint(1,9)
			mytext = str(mul_1)+ " "+"X"+" "+  str(mul_2)
		len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor,mytext)
		offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
		
		offscreen_canvas.Clear()
'''
'''

while True:
	offscreen_canvas.Clear()
	len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, my_text)
	pos -=10
	if(pos + len<0):
		pos = offscreen_canvas.width

	time.sleep(5)
	offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
'''


'''

matrix.SwapOnVSync(offscreen_canvas)
time.sleep(5)
offscreen_canvas.Clear()
'''

'''
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.multiplexing = 3
options.row_address_type = 2

matrix = RGBMatrix(options = options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 255)
pos = offscreen_canvas.width
my_text = "TEST"

len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
time.sleep(5)
offscreen_canvas.Clear()
'''
