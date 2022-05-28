import pybullet as p
import time
import pybullet_data
import math
import matplotlib.pyplot as plt
import numpy as np
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version

print("hi")

p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf") #where is plane.urdf
startPos = [0,0,0]
#sphereId = p.loadURDF("sphere.urdf")
startOrientation = p.getQuaternionFromEuler([0,0,0])
robotId = p.loadURDF("olympian.urdf",startPos, startOrientation, 
                   # useMaximalCoordinates=1, ## New feature in Pybullet
                   flags=p.URDF_USE_INERTIA_FROM_FILE)

print("==========SIMULATION ENABLED================")

#GET JOINT INFO

print(p.getNumJoints(robotId))
for i in range(0, p.getNumJoints(robotId)-1):
    print(p.getJointInfo(robotId, i)[0:13])


listOfJointIndeces = []
for i in range(0, p.getNumJoints(robotId)):
    listOfJointIndeces.append(i)
#why not use list(range())?
#also why have 0

def calcCOM():
    
    #CALCULATE COM
    masstimesxpossum = 0.0
    masstimesypossum = 0.0
    masstimeszpossum = 0.0
    masssum = 0.0
    for i in range(0, p.getNumJoints(robotId) -1):
        
        # if(i >= 0):
        #     print(p.getJointInfo(robotId, i)[0:13])
        
        wheight = p.getDynamicsInfo(robotId, i)[0]
        xpos = p.getLinkState(robotId, i)[0][0]
        ypos = p.getLinkState(robotId, i)[0][1]
        zpos = p.getLinkState(robotId, i)[0][2]
        
        masstimesxpossum += (wheight * xpos)
        masstimesypossum += (wheight * ypos)
        masstimeszpossum += (wheight * zpos)
        masssum += wheight
        
        # print(wheight)
        # print(xpos)
        # print(ypos)
        # print(zpos)
        # print("\n")
        p.stepSimulation()
    com = (masstimesxpossum/masssum, masstimesypossum/masssum, masstimeszpossum/masssum)
    
    #print("mass: " + str(masssum))
    #print("center of mass: " + str(com))
    #print("\n")
    return com

#INVERSE KINEMATICS 
#GET JOINT ANGLES NEEDED TO MOVE LINK 10 to (0. 0.6, 2)
#FORCE IS 25NM for every link bc im too lazy to custom set it for every link
#IT FALLS BECAUSE its a lot of torque exerted in a small amount of time

torque = 100
newi = []
comPos = []
comPos2 = []



holdingTorque = 100
actuationTorque = 10
torqueList = [holdingTorque]*23

file = open("xValues.txt", "r")
xValues = []
for word in file.readlines():
    xValues.append(float(word.rstrip('\n')))
file = open("zValues.txt", "r")
zValues = []
for word in file.readlines():
    zValues.append(float(word.rstrip('\n')))

def shiftFoot():
    
    leftAnkle = p.getJointState(robotId, 21)[0]
    leftThigh = p.getJointState(robotId, 18)[0]
    print(leftAnkle)
    print(leftThigh)
    
    for i in range(0, 50):
        positionsList = [0]*23
        angleNeeded = calculateAngleNeeded()
        comPos.append(calcCOM())
        newi.insert(0, i)
        positionsList[21] = angleNeeded/50 * i #left ankle
        positionsList[15] = angleNeeded/50 * i #right ankle
        positionsList[18] = angleNeeded/50 * i#left thigh
        positionsList[12] = angleNeeded/50 * i#right thigh

        #positionsList[14] = 0.3/50 * i
        forceArray = [torque]*23
        p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, targetPositions = positionsList, forces = forceArray)
        p.stepSimulation()
        
    ''
    for i in range(0, 50):
        comPos.append(calcCOM())
        newi.insert(0, i)
        angleNeeded = 0.5

        positionsList[11] = 0.2598371070140097/50 * i #thigh pitch
        positionsList[14] = 0.8123194567657278/50 * i #knee
        positionsList[16] = 0.4891906071331436/50 * i#ankle

        #positionsList[14] = 0.3/50 * i
        forceArray = [torque]*23
        p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, targetPositions = positionsList, forces = forceArray)
        p.stepSimulation()
    

    positionsList = [0]*23

    firstY = p.getLinkState(robotId, 15)[0][1]
    firstZ = p.getLinkState(robotId, 15)[0][2]
    
    
    for i in range(0, len(xValues)//20):
        """
        comPos.append(calcCOM())
        newi.insert(0, i)
        angleNeeded = calculateAngleNeeded()
        positionsList[21] = angleNeeded/len(xValues) * i #left ankle
        #positionsList[15] = angleNeeded/len(xValues) * i #right ankle
        positionsList[18] = angleNeeded/len(xValues) * i#left thigh
        #positionsList[12] = angleNeeded/len(xValues) * i#right thigh
        forceArray = [torque]*23
        p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, targetPositions = positionsList, forces = forceArray)
        p.stepSimulation()
        """
        #thighs are 12 and 18
        angleNeeded = calculateAngleNeeded()
        ikList = p.calculateInverseKinematics(robotId, 15, [xValues[20*i], firstY, zValues[20*i]+(len(xValues)-20*i)/len(xValues)*firstZ])
        
        positionsList = list(ikList)
        #print("uwu")
        #print(positionsList[11])
        #print(positionsList[14])
        #print(positionsList[16])
        #positionsList[11] = 0.5*(len(xValues)-i)/len(xValues)+positionsList[11]*(i/len(xValues))
        #positionsList[14] = 1*(len(xValues)-i)/len(xValues)+positionsList[14]*(i/len(xValues))
        #positionsList[16] = 0.5*(len(xValues)-i)/len(xValues)+positionsList[16]*(i/len(xValues))
        positionsList[21] = angleNeeded*(len(xValues)-8*i)/len(xValues)
        positionsList[18] = angleNeeded*(len(xValues)-8*i)/len(xValues)
        ankleAngle = calculateAnkleAngle()
        
        positionsList[15] = (math.pi/2-ankleAngle*np.sign(ankleAngle))*np.sign(ankleAngle)/len(xValues)*i*20
        ankleAngle = calculateOtherAnkleAngle()
        positionsList[16] = 0.4891906071331436*(len(xValues)-(i*20))/len(xValues)+ankleAngle/len(xValues)*i*20
        pelvisAngle = calculatePelvisAngle()
        print(pelvisAngle)
        positionsList[0] = -1*pelvisAngle
        #positionsList[15] = (math.pi-ankleAngle*np.sign(ankleAngle))*np.sign(ankleAngle)/len(xValues)*i
        '''
        if((ankleAngle)<0):
            positionsList[15] = -1*(math.pi-(abs(ankleAngle)))/len(xValues)*i
        else:
            positionsList[15] = math.pi-(abs(ankleAngle))/len(xValues)*i
        '''
        #positionsList[16] = 
        #positionsList[15] = (math.pi-calculateAnkleAngle())/len(xValues)*i
        # positionsList[0] = math.pi / 4
        forceArray = [torque]*23
        p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, targetPositions = positionsList, forces = forceArray)
        p.stepSimulation()

    for i in range(50000):
        p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, targetPositions = positionsList, forces = forceArray)
        p.stepSimulation()

def calculateAngleNeeded():
    anklePos = p.getLinkState(robotId, 21)[0]
    comPos = calcCOM()
    hipPos = p.getLinkState(robotId, 18)[0]
    ankleCom = (comPos[1]-anklePos[1], comPos[2]-anklePos[2])
    ankleHip = (hipPos[1]-anklePos[1], hipPos[2]-anklePos[2])
    cosAngle = (ankleCom[0]*ankleHip[0] + ankleCom[1]*ankleHip[1])/(np.sqrt((ankleCom[0]**2+ankleCom[1]**2))*np.sqrt((ankleHip[0]**2 + ankleHip[1]**2)))
    angle = np.arccos(cosAngle)
    #print(angle)
    return angle

def calculateAnkleAngle():
    anklePos = p.getLinkState(robotId, 15)[0]
    kneePos = p.getLinkState(robotId, 14)[0]
    angle = np.arctan((kneePos[2]-anklePos[2])/(kneePos[1]-anklePos[1]))
    print("thing " + str(angle))
    return angle

def calculateOtherAnkleAngle():
    anklePos = p.getLinkState(robotId, 15)[0]
    kneePos = p.getLinkState(robotId, 14)[0]
    angle = np.arctan((kneePos[0]-anklePos[0])/(kneePos[2]-anklePos[2]))
    print("thing " + str(angle))
    return angle

def calculatePelvisAngle():
    pelvisPos = p.getLinkState(robotId, 0)[0]
    chestPos = p.getLinkState(robotId, 1)[0]
    print(chestPos)
    print(pelvisPos)
    angle = np.arctan((chestPos[0]-pelvisPos[0])/(chestPos[2]-pelvisPos[2]))
    return angle

shiftFoot()

print(p.getLinkState(robotId, 21)[0][1]-calcCOM()[1])

print(str(p.getLinkState(robotId, 21)) + "HIIII")

for i in range(1000000):
    p.stepSimulation()

"""
for i in range(0, len(xValues), 1):
    ikList = p.calculateInverseKinematics(robotId, 15, [xValues[i], 0, zValues[i]])
    p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, 
                            targetPositions = ikList, forces = torqueList)
    p.stepSimulation()
    time.sleep(1./240.)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)
"""

z = list(range(len(xValues)))
area = 3  # 0 to 15 point radii

plt.scatter(z, zValues, s=area, alpha=0.5)
#plt.show()

#ikList = p.calculateInverseKinematics(robotId, 10, [0,0.6,2] )

"""
p.setJointMotorControlArray(robotId, listOfJointIndeces, p.POSITION_CONTROL, 
                            targetPositions = ikList, forces = torqueList)


#CALCULATE COM
masstimesxpossum = 0.0
masstimesypossum = 0.0
masstimeszpossum = 0.0
masssum = 0.0
for i in range(0, p.getNumJoints(robotId) -1):
    
    if(i >= 0):
        print(p.getJointInfo(robotId, i)[0:13])
    
    wheight = p.getDynamicsInfo(robotId, i)[0]
    xpos = p.getLinkState(robotId, i)[0][0]
    ypos = p.getLinkState(robotId, i)[0][1]
    zpos = p.getLinkState(robotId, i)[0][2]
    
    masstimesxpossum += (wheight * xpos)
    masstimesypossum += (wheight * ypos)
    masstimeszpossum += (wheight * zpos)
    masssum += wheight
    
    print(wheight) #what is wheight
    print(xpos)
    print(ypos)
    print(zpos)
    print("\n")

com = (masstimesxpossum/masssum, masstimesypossum/masssum, masstimeszpossum/masssum)
print("==========COM APROX EQUALS===========")
print(com)
print("\n")
#STEP SIMULATION
for i in range(0,10000):
    p.stepSimulation()
    time.sleep(1./240.)
    

print("========REALTIME SIMULATION DISABLED===============")
# p.calculateInverseKinematics(robotId, )
"""