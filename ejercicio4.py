import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

while True:
    analog_value = analog_input.read()
    #print (analog_value)
    if analog_value == 1:
            board.digital[5].write(1)
            board.digital[6].write(1)
            board.digital[7].write(1)
            board.digital[8].write(1)
            board.digital[9].write(1)
            board.digital[10].write(1)
            print("Led1 - HIGH -- Led2 - HIGH -- Led3 - HIGH -- Led4 - HIGH -- Led5 - HIGH -- Led6 - HIGH")
            #time.sleep(.06)
    elif analog_value == 0.0049:
            board.digital[5].write(0)
            board.digital[6].write(0)
            board.digital[7].write(0)
            board.digital[8].write(0)
            board.digital[9].write(0)
            board.digital[10].write(0)
            print("Led1 - LOW -- Led2 - LOW -- Led3 - LOW -- Led4 - LOW -- Led5 - LOW -- Led6 - LOW")
            #time.sleep(.06)



