#Read quaternion values from IMUs and cat them to a log file.
#On boot, the program can read the offsets.txt file to pick up where it left off.

#Default IMU recording is 1.00 0.00 0.00 0.00
#After a while (~15 minutes) the readings settle around 1.00 0.00 0.00 -0.10

#This program uses the default values

import serial
import os
ser = serial.Serial('/dev/ttyACM0',115200)

mode = 2
#-1 = do not use offsets at all (just get and print data do nothing with it)
#0 = start new offsets (delete offsets.txt and make/overwrite)
#1 = use offsets but do not overwrite
#2 = use and apply existing offsets, and overwrite

#default offsets
#1.00 0.00 0.00 0.00
#1.00 0.00 0.00 0.00
#1.00 0.00 0.00 0.00
#1.00 0.00 0.00 0.00

#make offsets.txt if it does not exist
if(not os.path.exists("offsets.txt")):

    with open("offsets.txt", "w+") as wfile:
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
    
        
#first param
#first param is 1.00 by default but in code we subtract 1 to make the offsets functionable. 
a1 = 0.0
b1 = 0.0
c1 = 0.0
d1 = 0.0


#second param
a2 = 0.0
b2 = 0.0
c2 = 0.0
d2 = 0.0


#third param
a3 = 0.0
b3 = 0.0
c3 = 0.0
d3 = 0.0


#fourth param
a4 = 0.0
b4 = 0.0
c4 = 0.0
d4 = 0.0




log = open("log.txt","w")

#get offsets
if(mode==0):
    os.remove("offsets.txt")
    with open("offsets.txt","a+") as wfile:
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
        wfile.write("1.00 0.00 0.00 0.00\n")
elif(mode==1 or mode==2):
    with open('offsets.txt') as rfile:
        data = rfile.readlines()
        adata = list(map(float,data[0].split(" ")))
        bdata = list(map(float,data[1].split(" ")))
        cdata = list(map(float,data[2].split(" ")))
        ddata = list(map(float,data[3].split(" ")))
        a1 = adata[0]-1
        a2 = adata[1]
        a3 = adata[2]
        a4 = adata[3]
        
        b1 = bdata[0]-1
        b2 = bdata[1]
        b3 = bdata[2]
        b4 = bdata[3]
        
        c1 = cdata[0]-1
        c2 = cdata[1]
        c3 = cdata[2]
        c4 = cdata[3]
        
        d1 = ddata[0]-1
        d2 = ddata[1]
        d3 = ddata[2]
        d4 = ddata[3]
        
        
        print(data)
        print(a1)
while True:
    read_serial=ser.readline()
    try:
        enc = read_serial.decode('ascii')
    except UnicodeDecodeError:
        pass
    #log.write(enc)
    
    enc = enc.replace("s","")
    enc = enc.replace("!"," ")
    enc = enc.replace("@"," ")
    enc = enc.replace("#"," ")
    enc = enc.replace("e","")
    
    print(enc)
    if(mode>=0):
        if(enc[0] == "a"):
            try:
                proper = list(map(float,enc[1:].split(" ")))
                
                print(proper)
                proper[0] += a1
                proper[1] += a2
                proper[2] += a3
                proper[3] += a4
                
                done = " ".join(list(map(str,proper)))
                if(mode>=1):
                    print(done)
                    if(mode==2):
                        data[0] = done+"\n"
                        log.write("A "+done+"\n")
            
            
            except:
                print("Under 4 numbers")
        if(enc[0] == "b"):
            try:
                proper = list(map(float,enc[1:].split(" ")))
                print(proper)
                proper[0] += b1
                proper[1] += b2
                proper[2] += b3
                proper[3] += b4
                done = " ".join(list(map(str,proper)))
                if(mode>=1):
                    print(done)
                    if(mode==2):
                        data[1] = done+"\n"
                        log.write("B "+done+"\n")
            
            except:
                print("Under 4 numbers")
        if(enc[0] == "c"):
            try:
                proper = list(map(float,enc[1:].split(" ")))
                print(proper)
                proper[0] += c1
                proper[1] += c2
                proper[2] += c3
                proper[3] += c4
                done = " ".join(list(map(str,proper)))
                if(mode>=1):
                    print(done)
                    if(mode==2):
                        data[2] = done+"\n"
                        log.write("C "+done+"\n")
            
            except:
                print("Under 4 numbers")
        if(enc[0] == "d"):
            
            try:
                proper = list(map(float,enc[1:].split(" ")))
                print(proper)
                proper[0] += d1
                proper[1] += d2
                proper[2] += d3
                proper[3] += d4
                done = " ".join(list(map(str,proper)))
                if(mode>=1):
                    print(done)
                    if(mode==2):
                        data[3] = done+"\n"
                        log.write("D "+done+"\n")
            
            except:
                print("Under 4 numbers")
        with open("offsets.txt", "w") as wfile:
            wfile.writelines(data)