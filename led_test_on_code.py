#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


from rgbmatrix import RGBMatrix, RGBMatrixOptions
options = RGBMatrixOptions()
self_matrix = RGBMatrix(options = options)

offscreen_canvas = self_matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(25, 25, 0)
pos = offscreen_canvas.width

my_text = "wanted str"

while True:
    offscreen_canvas.Clear()
    len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, my_text)
    pos -= 1
    if (pos + len < 0):
        pos = offscreen_canvas.width

    time.sleep(0.05)
    offscreen_canvas = self_matrix.SwapOnVSync(offscreen_canvas)


# Main function
'''if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):

      	run_text.print_help()'''

'''
offscreen_canvas =matrix.CreateFrameCanvas()
run_text = RunText()
offscreen_canvas.Clear()
len = graphics.DrawText(offscreen_canvas, font, leftPos, topPos, textColor, textToDisplay)
offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
time.sleep(.8)
#lock.release()'''
