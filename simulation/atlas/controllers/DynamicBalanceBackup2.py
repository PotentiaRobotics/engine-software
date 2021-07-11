import time
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
from controller import Robot, Supervisor, Display

#robot - wb_supervisor_node
#supervisor - wb_robot
#so basically supervisor is the robot and robot is the supervisor
#hooray for poor nomenclature
supervisor = Supervisor()

global TIMESTEP
TIMESTEP = int(supervisor.getBasicTimeStep())
startTime = time.time()

robotNode = supervisor.getRoot() 
children = robotNode.getField("children")
robot = children.getMFNode(5)


right_arm_uzi = supervisor.getDevice("RArmUsy")
left_arm_uzi = supervisor.getDevice("LArmUsy")

torso_pitch = supervisor.getDevice("BackMby")
torso_roll = supervisor.getDevice("BackUbx")

right_torso_pitch = supervisor.getDevice("RLegLhy")
left_torso_pitch = supervisor.getDevice("LLegLhy")


right_ankle_pitch = supervisor.getDevice("RLegUay")
left_ankle_pitch = supervisor.getDevice("LLegUay")


# print(rightFootSlotPosition,leftFootSlotPosition)


        

# def isCOMInSupportPlane(wantDistance):
#         coordinate1 = ((rightFootSlotPosition[0] + 0.17), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
#         coordinate2 = ((rightFootSlotPosition[0] - 0.08), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

#         coordinate3 = ((leftFootSlotPosition[0] - 0.08), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
#         coordinate4 = ((leftFootSlotPosition[0] + 0.17), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

#         coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

#         supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

#         COMPoint = Point(coordinate5)

     
#         if(wantDistance== False):
#                 return supportRectangle.contains(COMPoint)
#         elif(wantDistance == True):
#                 return supportRectangle.distance(COMPoint)


def distanceToCOMinSupportPlaneCenter():

        rightFootSlot = robot.getField("rightFootSlot")
        rightFootSlotPosition = rightFootSlot.getMFNode(0).getPosition()


        leftFootSlot = robot.getField("leftFootSlot")
        leftFootSlotPosition = leftFootSlot.getMFNode(0).getPosition()



        coordinate1 = ((rightFootSlotPosition[0] + 0.17), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
        coordinate2 = ((rightFootSlotPosition[0] - 0.08), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

        coordinate3 = ((leftFootSlotPosition[0] - 0.08), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
        coordinate4 = ((leftFootSlotPosition[0] + 0.17), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

        coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

        supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

        COMPoint = Point(coordinate5)

        supportRectangleCenter = supportRectangle.centroid

        return [(COMPoint.x - supportRectangleCenter.x), (COMPoint.y - supportRectangleCenter.y)]


        

# def isCOMInSupportPlaneTight(wantDistance):
#         coordinate1 = ((rightFootSlotPosition[0] + 0.025), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
#         coordinate2 = ((rightFootSlotPosition[0] - 0.05), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

#         coordinate3 = ((leftFootSlotPosition[0] - 0.05), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
#         coordinate4 = ((leftFootSlotPosition[0] + 0.025), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

#         coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

#         supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

#         COMPoint = Point(coordinate5)

     
#         if(wantDistance== False):
#                 return supportRectangle.contains(COMPoint)
#         elif(wantDistance == True):
#                 return supportRectangle.distance(COMPoint)

# def isComInSupportPlaneCenter(wantDistance):
#         coordinate1 = ((rightFootSlotPosition[0] + 0.075), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Front Edge
#         coordinate2 = ((rightFootSlotPosition[0] - 0.025), (rightFootSlotPosition[2] + 0.05)) #Right Foot, Back Edge

#         coordinate3 = ((leftFootSlotPosition[0] - 0.025), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Back Edge
#         coordinate4 = ((leftFootSlotPosition[0] + 0.075), (leftFootSlotPosition[2] - 0.05)) #Left Foot, Front Edge

#         coordinate5 = ((robot.getCenterOfMass()[0]), (robot.getCenterOfMass()[2]))

#         supportRectangle = Polygon([coordinate1,coordinate2,coordinate3,coordinate4])

#         COMPoint = Point(coordinate5)

#         print("COM is at " + str(COMPoint))
#         print("COM should be at" + str(supportRectangle.centroid))

#         if (wantDistance == False):
#                 if((COMPoint.x > coordinate2[0]) and (COMPoint.x < (coordinate2[0] + 0.03))):
#                         return True
#                 elif(supportRectangle.centroid != COMPoint):
#                         return False
#         elif (wantDistance == True):
#                 return ((coordinate2[0] + 0.015) - COMPoint.x)


    




shoulderForce = 1.5


# right_shoulder_pitch.setPosition(shoulderForce)
# left_shoulder_pitch.setPosition(shoulderForce)




firstTimeMovingTest = True

fallingForward = True

# isComInSupportPlaneCenter(False)


while supervisor.step(TIMESTEP) != -1:


        if(time.time() - startTime >= 3 and firstTimeMovingTest == True ):
                # right_torso_pitch.setPosition(testForce)
                # left_torso_pitch.setPosition(testForce)
                # forcex = -4550,6000
                forcex = -4500
                robot.addForce([forcex,0,0], False)
                firstTimeMovingTest = False

        # if(time.time() - startTime >= 6 ):
        #         # isComInSupportPlaneCenter()
        #         # print(robot.getCenterOfMass())
        #         print(isComInSupportPlaneCenter(True))

        wantActuation = True

        if( firstTimeMovingTest == False and wantActuation == True):

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
                

                # print(distanceToCOMinSupportPlaneCenter())
                
                #PID CONTROL (ADD DERIVITIVE)
                #CO = CObias + KC * e(t)
                ankleerrorx = distanceToCOMinSupportPlaneCenter()[0] #find error/e(t)
                anklekc = -0.5 * fallModifier
                ankleCObias = 0
                ankleCOx = ankleCObias + (anklekc * ankleerrorx) 
                
                torsoerrorx = distanceToCOMinSupportPlaneCenter()[0] #find error/e(t)
                torsokc = -1 * fallModifier
                torsoCObias = 0
                torsoCOx = torsoCObias + (torsokc * torsoerrorx) 

                torsoerrory  = distanceToCOMinSupportPlaneCenter()[1] #find error/e(t)
                torsokc = -1 * fallModifier
                torsoCObias = 0
                torsoCOy = torsoCObias + (torsokc * torsoerrorx) 
                
                shouldererrorx = distanceToCOMinSupportPlaneCenter()[0] #find error/e(t)
                shoulderkc = -0.5 * fallModifier
                shoulderCObias = 0
                shoulderCOx = shoulderCObias + (shoulderkc * shouldererrorx) 
                
                right_ankle_pitch.setPosition(ankleCOx)
                left_ankle_pitch.setPosition(ankleCOx)
                

                torso_pitch.setPosition(torsoCOx)
                torso_roll.setPosition(torsoCOy)

                right_torso_pitch.setPosition(torsoCOx*-1)
                left_torso_pitch.setPosition(torsoCOx*-1) 
               
                
                right_arm_uzi.setPosition(shoulderCOx)
                left_arm_uzi.setPosition(shoulderCOx)
                
                
                # print("CO " + str(shoulderCOx))
                        

    
    
#TODO: make it fix y errors as well as x errors.