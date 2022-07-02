import threading
import time

class IMU:
    def __init__(self, num):
        self.val = num

class ping:
    def __init__(self, num):
        self.val = num

class mode:
    def __init__(self, num):
        self.val = num

class jointAngles:
    def __init__(self, num):
        self.val = num

class position:
    def __init__(self, num):
        self.val = num

class velocity:
    def __init__(self, num):
        self.val = num

class registry:
    def __init__(self):
        self.registry = {IMU : None, ping : None, mode : None, jointAngles : None, position : None, velocity : None}

    def addRegister(self, key, value, timestamp):
        temp = self.registry.get[key]
        self.registry[key] = temp.append([value, timestamp])      #[value, timestamp]

    def get(self, register):
        return self.registry.get(register)

class flag:
    def __init__(self):
        self.flag = {'motorActuation' :None, 'mode change' : None, 'movement' : None, 'pathCoords' : None}

    def addFlag(self, key, value, priority, timestamp):   #priority is going to be from range 1-5
        temp = self.flag.get[key]
        self.flag[key] = temp.append([value, priority, timestamp])      #[value, priority, timestamp]

    def get(self, fl):
        return self.flag.get(fl)


def gaitGen():
    if flag[]
    
    
def balance():


def telemetry():


def cv(): 
    if flag['pathCoords'] != None:







def gaitGen():
    if flag['balanced'] != None:
        
     if flag['movement'] != None:





def automatic():
    cv()
    gaitGen()


def manual():
    telemetry()
    addFlag('motorActuation', False, time.time())
    executor()

def sendAuto():
    telemetry()
    addFlag('movement', False, time.time())
    executor()   


def executor():


def loop():
    executor()


class mode:
    def __init__(self, num):
        self.val = num

class commands:
    def __init__(self, num):
        self.mode = mode(3)
        
    

    def changeMode(mode m):
        print()

    def shutDown():



