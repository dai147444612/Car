import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
OUTRB =16
OUTLB =32
OUTLF =18
OUTRF =7
def InfRB():
    GPIO.setup(OUTRB, GPIO.IN)
    print(GPIO.input(OUTRB))
    if GPIO.input(OUTRB)==0:
        return 'danger'
    else:
        return 'safe'
def InfLB():
    GPIO.setup(OUTLB, GPIO.IN)
    print(GPIO.input(OUTLB))
    if GPIO.input(OUTLB)==0:
        return 'danger'
    else:
        return 'safe'
def InfLF():
    GPIO.setup(OUTLF, GPIO.IN)
    print(GPIO.input(OUTLF))
    if GPIO.input(OUTLF)==0:
        return 'danger'
    else:
        return 'safe'
def InfRF():
    GPIO.setup(OUTRF, GPIO.IN)
    print(GPIO.input(OUTRF))
    if GPIO.input(OUTRF)==0:
        return 'danger'
    else:
        return 'safe'
# while True:
#     print(InfRB())
#     time.sleep(1)