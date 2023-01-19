import pyfirmata

comport='COM5'

board=pyfirmata.Arduino(comport)

red=board.get_pin('d:8:o')
green=board.get_pin('d:13:o')

def led(total):
    if total==0:
        red.write(0)
        green.write(0)
    elif total==1:
        red.write(0)
        green.write(0)
    elif total==3:
        red.write(0)
        green.write(0)
    elif total==4:
        red.write(0)
        green.write(0)
    elif total==5:
        red.write(1)
        green.write(0)
    elif total==2:
        red.write(0)
        green.write(1)
