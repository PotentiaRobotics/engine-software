from os import truncate
from controller import Robot, Supervisor, Display
from shapely.geometry import Polygon #for rectangle intersections
from shapely.geometry import Point
import time

supervisor = Supervisor()

global TIMESTEP
TIMESTEP = int(supervisor.getBasicTimeStep())

robotNode = supervisor.getRoot() 
children = robotNode.getField("children")
robot = children.getMFNode(5)

startTime = time.time()

#get devices


gyro = supervisor.getDevice("gyro")
accel = supervisor.getDevice("accelerometer")    

gyro.enable(TIMESTEP)
accel.enable(TIMESTEP)

right_shoulder_pitch = supervisor.getDevice("RShoulderPitch")
left_shoulder_pitch = supervisor.getDevice("LShoulderPitch")

right_torso_pitch = supervisor.getDevice("RHipPitch")
left_torso_pitch = supervisor.getDevice("LHipPitch")

right_hip_roll = supervisor.getDevice("RHipRoll")
left_hip_roll = supervisor.getDevice("LHipRoll")

right_knee_pitch = supervisor.getDevice("RKneePitch")
left_knee_pitch = supervisor.getDevice("LKneePitch")

right_ankle_pitch = supervisor.getDevice("RAnklePitch")
left_ankle_pitch = supervisor.getDevice("LAnklePitch")

left_foot_bumper_left = supervisor.getDevice("LFoot/Bumper/Left")
right_foot_bumper_right = supervisor.getDevice("RFoot/Bumper/Right")

left_foot_sensor = supervisor.getDevice("LFsr")
right_foot_sensor = supervisor.getDevice("RFsr")


rightFootSlot = robot.getField("rightFootSlot")
rightFootSlotPosition = rightFootSlot.getMFNode(0).getPosition()
# print(rightFootSlotPosition)

leftFootSlot = robot.getField("leftFootSlot")
leftFootSlotPosition = leftFootSlot.getMFNode(0).getPosition()
# print(leftFootSlotPosition)

#default +0.075, -0.025, +0.05, -0.05
def isCOMInSupportPlane(wantDistance):
        coordinate1 = ((rightFootSlotPosition[0] + 0.075), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
        coordinate2 = ((rightFootSlotPosition[0] - 0.025), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

        coordinate3 = ((leftFootSlotPosition[0] - 0.025), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
        coordinate4 = ((leftFootSlotPosition[0] + 0.075), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

        coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

        supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

        COMPoint = Point(coordinate5)

     
        if(wantDistance== False):
                return supportRectangle.contains(COMPoint)
        elif(wantDistance == True):
                return supportRectangle.distance(COMPoint)

def isComInSupportPlaneCenter(wantDistance):
        coordinate1 = ((rightFootSlotPosition[0] + 0.075), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
        coordinate2 = ((rightFootSlotPosition[0] - 0.025), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

        coordinate3 = ((leftFootSlotPosition[0] - 0.025), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
        coordinate4 = ((leftFootSlotPosition[0] + 0.075), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

        coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

        supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

        COMPoint = Point(coordinate5)

        print("COM is at " + str(COMPoint))
        print("COM should be at" + str(supportRectangle.centroid))

        if (wantDistance == False):
                if((COMPoint.x > coordinate2[0]) and (COMPoint.x < (coordinate2[0] + 0.03))):
                        return True
                elif(supportRectangle.centroid != COMPoint):
                        return False
        elif (wantDistance == True):
                return ((coordinate2[0] + 0.015) - COMPoint.x)


    




shoulderForce = 1.5


right_shoulder_pitch.setPosition(shoulderForce)
left_shoulder_pitch.setPosition(shoulderForce)




firstTimeMovingTest = True

fallingForward = True

isComInSupportPlaneCenter(False)

while supervisor.step(TIMESTEP) != -1:


        if(time.time() - startTime >= 3 and firstTimeMovingTest == True ):
                # right_torso_pitch.setPosition(testForce)
                # left_torso_pitch.setPosition(testForce)
                # robot.addForce(5, False)
                #145 good
                # forcex = 100
                # forcex = -75/-80
                forcex = -85
                robot.addForce([forcex,0,0], False)
                firstTimeMovingTest = False

        # if(time.time() - startTime >= 6 ):
        #         # isComInSupportPlaneCenter()
        #         # print(robot.getCenterOfMass())
        #         print(isComInSupportPlaneCenter(True))

        if(isCOMInSupportPlane(False) == False and firstTimeMovingTest == False):

                if(robot.getCenterOfMass()[0] > 0):
                        fallingForward = True  #com is forward so apply backwards motor values (positive motor values)
                elif (robot.getCenterOfMass()[0] < 0):
                        fallingForward = False #com is backward so apply forwards motor values (negative motor values)
                
                # print(fallingForward)

                

                # print(error)
                fallModifier = 1

                if(fallingForward == True):
                        fallModifier = 1
                elif(fallingForward == False):
                        fallModifier = -1
                
                
                #PID CONTROL (ADD DERIVITIVE)
                #CO = CObias + KC * e(t)
                ankleerror = isCOMInSupportPlane(True) #find error/e(t)
                anklekc = 1 * fallModifier
                ankleCObias = 0
                ankleCO = ankleCObias + (anklekc * ankleerror) 
                
                torsoerror = isCOMInSupportPlane(True) #find error/e(t)
                torsokc = 2 * fallModifier
                torsoCObias = 0
                torsoCO = torsoCObias + (torsokc * torsoerror) 
                
                shouldererror = isCOMInSupportPlane(True) #find error/e(t)
                shoulderkc = 2 * fallModifier
                shoulderCObias = 0
                shoulderCO = shoulderCObias + (shoulderkc * shouldererror) 
                
                right_ankle_pitch.setPosition(ankleCO)
                left_ankle_pitch.setPosition(ankleCO)
                
                right_torso_pitch.setPosition(torsoCO)
                left_torso_pitch.setPosition(torsoCO)
                
                right_shoulder_pitch.setPosition(shoulderCO)
                left_shoulder_pitch.setPosition(shoulderCO)
                
                
                print("CO " + str(shoulderCO))