import pyfirmata
import time
board = pyfirmata.Arduino('COM3')

while True:
    #MITAD DE LOS LEDS 5 AL 7
    board.digital[5].write(1)
    board.digital[6].write(1)
    board.digital[7].write(1)
    time.sleep(1)
    board.digital[5].write(0)
    board.digital[6].write(0)
    board.digital[7].write(0)
    #time.sleep(1)

    #LA OTRA MITAD DE LOS LEDS 8 AL 10
    board.digital[8].write(1)
    board.digital[9].write(1)
    board.digital[10].write(1)
    time.sleep(2)
    board.digital[8].write(0)
    board.digital[9].write(0)
    board.digital[10].write(0)
    #time.sleep(1)
    