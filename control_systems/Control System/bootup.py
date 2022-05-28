# Create priority queue
# In main create three threads
# 1 for managing actions (stores priority queue)
# 1 for reading sensor data
# Updates sensor data through wifi and propiosense system
# 1 for executing the first action in the priority queue

from Propioception import *
# from commands import *

import re
import threading
import socket
import heapq
import time
#import serial

class Receiver:
  def __init__(self, host, port):
    self.commands = []
    self.executions = []
    self.transmit = []
    self.timer = 0
    self.HOST = host
    self.PORT = port

    #connecting using scokets
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    #managing error exception
    try:
      s.bind((self.HOST, self.PORT))
    except socket.error:
        print ('Bind failed ')

    s.listen(5)
    print('Socket awaiting messages')
    (self.conn, addr) = s.accept()
    print('Connected')
  
  """Method receives commands from client and add to queue"""
  def telemetryReceive(self):
    # Commands must be in form "PRIORITY|{COMMAND}|TIMESTAMP|CHECKSUM"
    # awaiting for message
    while True:
      action = self.conn.recv(1024).decode('UTF-8')
      if len(action) > 0:
        heapq.heappush(self.commands,action)
        print("Received|"+action)
        heapq.heappush(self.transmit,"Received|"+action)
          
  """Method checks commands from queue and adds to execution queue"""
  def checkCommand(self):
    while True:
      if len(self.commands) > 0:
        #checking if the checksum of the command
        #equals the sum of all ascii values of every character 
        #in command statement
        pattern = "^[0-5]\|.*\|[0-9]{2}:[0-9]{2}\|" #everything but the checksum value
        checksum = "\w+$" #checksum value
        popped = heapq.heappop(self.commands) #gets smallest value command
        com = re.findall(pattern, popped) 
        numval = re.findall(checksum, popped)
        numval = numval[0]
        numval = int(numval,16) #converts hex to int
        print(com[0])
        print(sum([ord(i) for i in com[0]]))
        if numval == sum([ord(i) for i in com[0]]):
          print("working")
          heapq.heappush(self.transmit, "Correct|"+popped)
          heapq.heappush(self.executions, popped)
          print(self.transmit)
          print(self.executions)
        else: 
          heapq.heappush(self.transmit, "Incorrect|"+popped)
        
  def telemetryTransmit(self):
    while True:
      if len(self.transmit) > 0:
        print("Transmit queue", self.transmit)
        self.conn.send(bytes(heapq.heappop(self.transmit),'utf-8'))    

  def execute(self):
    while True:
      if len(self.executions) > 0:
        command = heapq.heappop(self.executions)
        print(command)
        heapq.heappush(self.transmit, "Executed|"+command)
        # if command == "Password A_on_LED":
          # if onAndOfffLed():
          #   print("Executed: ", command)
          # else:
          #   print("Did not execute correctly ", command)
        print("Inside execute",self.executions)
        time.sleep(5)
        if "Balancing" not in self.executions:
          heapq.heappush(self.executions, "Balancing")

  def balance(self):
    print("Nothing")

  def gaitGen(self):
    print("Nothing")

  def computerVision(self):
    print("Nothing")

  def sensorData(self):
    var = ""
    # Test
  #  print("Inside")
  #  ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
  #  ser.reset_input_buffer()
  #  while True:
  #    print("Inside data")
  ##    # Read from Arduinos to know what motors and sensors there are
    #  ser.write("Send ****s plz\n".encode('utf-8'))
    #  line = ser.readline().decode('utf-8').rstrip()
    #  print(line)

  def runSimul(self):
    threading.Thread(target=self.telemetryReceive).start()
    threading.Thread(target=self.checkCommand).start()
    threading.Thread(target=self.telemetryTransmit).start()
    threading.Thread(target=self.execute).start()

    # threading.Thread(target=self.sensorData).start()

    # threading.Thread(target=self.balance).start()
    threading.Thread(target=self.gaitGen).start()
    # threading.Thread(target=self.comuterVision).start()

def startBoot():
  simulation = Receiver('10.235.1.145',12345)
  simulation.runSimul()
