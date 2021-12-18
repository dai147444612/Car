from flask import Flask,Response
from flask_cors import CORS
import Car
import time
import Camara as ca
import socket
service=Flask(__name__)
CORS(service,supports_credentials=True)
stop=0.2


@service.route('/Auto')
def Auto():
    Car.setup()
    Car.flag=True
    Car.Automove()
    return "自动驾驶"

@service.route('/Manual')
def Manual():
    Car.stop()
    return '人工驾驶'
@service.route('/Forward')
def Forward():
    Car.setup()
    Car.forward()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '前进'
@service.route('/Back')
def Back():
    Car.setup()
    Car.back()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '后退'
@service.route('/right_back')
def right_back():
    Car.setup()
    Car.right_back()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '右后方倒退'
@service.route('/Left_forward')
def Left_forward():
    Car.setup()
    Car.Left_forward()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '左前方'
@service.route('/right_forward')
def right_forward():
    Car.setup()
    Car.right_forward()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '右前方'
@service.route('/Left_back')
def Left_back():
    Car.setup()
    Car.Left_back()
    time.sleep(stop)
    Car.GPIO.cleanup()
    return '左后方'

@service.route('/getCamare')
def Camare():
    return Response(ca.gen(ca.VideoCamera()),
                            mimetype='multipart/x-mixed-replace; boundary=frame')

def getIP():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
        return ip
                                                                                                                  
service.run(host=getIP(),debug=True,port=9099)
