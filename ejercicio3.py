import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

def ascendentepot():
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        board.digital[5].write(1)
        time.sleep(delay)
        board.digital[6].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[10].write(1)
        time.sleep(delay)
        board.digital[5].write(0)
        board.digital[6].write(0)
        board.digital[7].write(0)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.digital[10].write(0)
    else:
        time.sleep(0.1)

def descendentepot():
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        board.digital[10].write(1)
        time.sleep(delay)
        board.digital[9].write(1)
        time.sleep(delay)
        board.digital[8].write(1)
        time.sleep(delay)
        board.digital[7].write(1)
        time.sleep(delay)
        board.digital[6].write(1)
        time.sleep(delay)
        board.digital[5].write(1)
        time.sleep(delay)
        board.digital[10].write(0)
        board.digital[9].write(0)
        board.digital[8].write(0)
        board.digital[7].write(0)
        board.digital[6].write(0)
        board.digital[5].write(0)
    else:
        time.sleep(0.1)

def menu():
    leds = input("Menu\nTeclar 1 si lo desea en forma ascendete\nTeclar 2 si lo desea en forma descendente\n").upper()
    if leds == '1':
        while True:
            ascendentepot()
    elif leds == '2':
        while True:
            descendentepot()
while True:
    menu()

