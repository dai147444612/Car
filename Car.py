import RPi.GPIO as GPIO
import time
import InfraredDetection as InD
import UltrasonicSensing as UlS
import random

INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INT1,GPIO.OUT)
    GPIO.setup(INT2,GPIO.OUT)
    GPIO.setup(INT3,GPIO.OUT)
    GPIO.setup(INT4,GPIO.OUT)

def forward():
    GPIO.output(INT1,GPIO.HIGH)
    GPIO.output(INT2,GPIO.LOW)
    GPIO.output(INT3,GPIO.HIGH)
    GPIO.output(INT4,GPIO.LOW)

def back():
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.HIGH)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.HIGH)

def right_back():
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.HIGH)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.LOW)

def Left_forward():
    GPIO.output(INT1, GPIO.HIGH)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.LOW)

def right_forward():
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.HIGH)
    GPIO.output(INT4, GPIO.LOW)

def Left_back():
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.HIGH)


def Automove():
    while True:
        x=UlS.checkdistForward()
        y=UlS.checkdistBack()
        RF=InD.InfRF()
        RB=InD.InfRB()
        LF=InD.InfLF()
        LB=InD.InfLB()
        if x>20 and LF=='safe' and RF=='safe':
            GPIO.cleanup()
            setup()
            forward()
        elif x<20 and y>20 and LB=='safe' and RB=='safe':
            GPIO.cleanup()
            setup()
            x=random.randint(0,1)
            if x==0:
                right_back()
                time.sleep(0.75)
            elif x==1:
                Left_back()
                time.sleep(0.75)
        elif x<20 and y>20 and LB=='danger' and RB=='danger':
            GPIO.cleanup()
            setup()
            back()
            time.sleep(1)
        elif x>20 and LF=='safe' and RF=='danger':
            GPIO.cleanup()
            setup()
            Left_forward()
        elif x>20 and LF=='danger' and RF=='safe':
            GPIO.cleanup()
            setup()
            right_forward()
        elif x<20 and y>20 and LB=='safe' and RB=='danger':
            GPIO.cleanup()
            setup()
            Left_back()
        elif x<20 and y>20 and LB=='danger' and RB=='safe':
            GPIO.cleanup()
            setup()
            right_back()
        else:
            stop()
def stop():
    GPIO.cleanup()

