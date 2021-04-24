import pyfirmata
import time
import numpy as np
from pyfirmata import util


board = pyfirmata.Arduino('COM3') #"connects" the board to this code

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:1:i')
digital_output = board.get_pin('d:13:o')
led = board.get_pin('d:11:p')

while True:
    analog_value=analog_input.read()
    if analog_value is not None:
        led.write(analog_value)
    print(analog_value)
    digital_output.write(1)
    time.sleep(1)
    digital_output.write(0)
    time.sleep(1)
    time.sleep(0.01)