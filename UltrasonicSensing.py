import RPi.GPIO as GPIO
import time

TrigBack=29
EchoBack=31
Trig = 38
Echo = 40
# 超声波距离探测
def checkdistBack():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo, GPIO.IN)
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig, GPIO.LOW)
    while not GPIO.input(Echo):
        pass
    t1 = time.time()
    while GPIO.input(Echo):
        pass
    t2 = time.time()
    print((t2-t1)*34300/2)
    return (t2-t1)*34300/2

def checkdistForward():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TrigBack, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(EchoBack, GPIO.IN)
    GPIO.output(TrigBack, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(TrigBack, GPIO.LOW)
    while not GPIO.input(EchoBack):
        pass
    t1 = time.time()
    while GPIO.input(EchoBack):
        pass
    t2 = time.time()
    print((t2-t1)*34300/2)
    return (t2-t1)*34300/2



def distStart():
    try:
        while True:
            print('目标距离:%0.2f cm' % checkdist())
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
# while True:
#     print(checkdistForward())
#     print(checkdistBack())
#     time.sleep(1)