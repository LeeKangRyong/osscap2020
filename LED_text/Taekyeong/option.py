
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
options = RGBMatrixOptions()
options.gpio_slowdown = 4
options.hardware_mapping = 'regular'
options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../fonts/6x10.bdf")
textColor = graphics.Color(255, 36, 0)
pos = 2.5
