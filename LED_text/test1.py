
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
#Configuration for the matrix

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
