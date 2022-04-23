import pyfirmata
import time
board = pyfirmata.Arduino('COM3')


def ascendente():
    #ASCENDENTE
    board.digital[5].write(1)
    time.sleep(.2)
    board.digital[6].write(1)
    time.sleep(.2)
    board.digital[7].write(1)
    time.sleep(.2)
    board.digital[8].write(1)
    time.sleep(.2)
    board.digital[9].write(1)
    time.sleep(.2)
    board.digital[10].write(1)
    time.sleep(.2)
    board.digital[5].write(0)
    board.digital[6].write(0)
    board.digital[7].write(0)
    board.digital[8].write(0)
    board.digital[9].write(0)
    board.digital[10].write(0)


def descendente():
    #DESCENDENTE
    board.digital[10].write(1)
    time.sleep(.2)
    board.digital[9].write(1)
    time.sleep(.2)
    board.digital[8].write(1)
    time.sleep(.2)
    board.digital[7].write(1)
    time.sleep(.2)
    board.digital[6].write(1)
    time.sleep(.2)
    board.digital[5].write(1)
    time.sleep(.2)
    board.digital[10].write(0)
    board.digital[9].write(0)
    board.digital[8].write(0)
    board.digital[7].write(0)
    board.digital[6].write(0)
    board.digital[5].write(0)

def funcion():
    leds = input("Menu\nTeclar 1 si lo desea en forma ascendete\nTeclar 2 si lo desea en forma descendente\n").upper()
    if leds == '1':
        while True:
            ascendente()
            break
    elif leds == '2':
        while True:
            descendente()
            break
while True:
    funcion()
