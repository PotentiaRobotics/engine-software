"""olympian controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import time
import numpy as np

def calculateCOM(robot):
  # links needed to calculate COM
  torso = robot.getDevice("torsoMotor")
  upperLeftLeg= robot.getDevice("upperLeftLegMotor")
  upperRightLeg = robot.getDevice("upperRightLegMotor")

  links = [torso, upperLeftLeg, upperRightLeg] # additional links will be added, when they're made

  totalMass = len(links) # assumption that all links have mass of 1
  centerOfMass = [0, 0, 0, 0]

  for i in links: 
    # instantiation of values
    # need to add code to get joint angles
    if i == torso:
        r = 0.25
        theta0 = 0
        theta1 = 0
    else:
        r = 0.225
        theta0 = 0
        theta1 = 0
    
    # instantiation of matrices 
    # assumption that all angle values are in degrees
    transformationMatrixToLink = [[np.cos(theta0*np.pi/180), -np.sin(theta0*np.pi/180), 
                                 0, 2*r*np.cos(theta0*np.pi/180)], [np.sin(theta0*np.pi/180), 
                                 np.cos(theta0*np.pi/180), 0, 2*r*np.sin(theta0*np.pi/180)], 
                                 [0, 0, 1, 0], [0, 0, 0, 1]]                       
    vectorOfJointAngles = [2*r*np.cos(theta1*np.pi/180), 2*r*np.sin(theta1*np.pi/180), 0, 1]
    transformationMatrixToLinkCOM = [[np.cos(theta1*np.pi/180), 0, -np.sin(theta1*np.pi/180), 
                                    2*r*np.cos(theta0*np.pi/180)], [0, 1, 0, 0], 
                                    [np.sin(theta1*np.pi/180), 0, np.cos(theta1*np.pi/180), 
                                    2*r*np.sin(theta0*np.pi/180)], [0, 0, 0, 1]]
    
    # COM of each link is calculated forward kinematics equations
    calc = np.dot(transformationMatrixToLink,vectorOfJointAngles)
    print(calc)
    calc=np.dot(calc,transformationMatrixToLinkCOM) 
    print(calc)                      
    #calc = transformationMatrixToLink.dot(vectorOfJointAngles).dot(transformationMatrixToLinkCOM)
    
    # COM of the entire rigid body is calculated using a weighted average
    centerOfMass += (1/totalMass)*calc
    
  return centerOfMass[0], centerOfMass[1], centerOfMass[2]


def main():
    # create the Robot instance.
    print("Initializing world...")
    robot = Robot()
    timestep = 64
    start = 0
    while robot.step(32) != -1:
        print(calculateCOM(robot))
        start += 32/1000.0
        head_motor = robot.getDevice("torso_yaw")
        # motor2 = robot.getDevice("neck_roll")
        lknee = robot.getDevice("left_knee_pitch")
        rknee = robot.getDevice("right_knee_pitch")
        lhip = robot.getDevice("left_hip_pitch")
        rhip = robot.getDevice("right_hip_pitch")
        lfoot = robot.getDevice("left_ankle_pitch")
        rfoot = robot.getDevice("right_ankle_pitch")
        
        torso_pitch = robot.getDevice("torso_pitch")
        
        head_motor.setVelocity(1)
        lknee.setVelocity(2)
        rknee.setVelocity(2)
        lknee.setPosition(2)
        rknee.setPosition(2)
        torso_pitch.setVelocity(10)
        # torso_pitch.setTorque(10)
        
        lhip.setVelocity(2)
        rhip.setVelocity(2)
        lhip.setPosition(-0.7)
        rhip.setPosition(-0.7)
        
        lfoot.setVelocity(2)
        rfoot.setVelocity(2)
        lfoot.setPosition(0.3)
        rfoot.setPosition(0.3)
        
        pos = 0
        add = False
        
        if start > 6:
            while robot.step(32) != -1:
                torso_pitch.setPosition(pos)
                # time.sleep(0.1)
                
                if add:
                    pos += 0.2
                else:
                    pos -= 0.2
                    
                if pos >= 2:
                    add = False
                elif pos <= 0:
                    add = True
    
    # get the time step of the current world.
    # timestep = int(robot.getBasicTimeStep())
    # motor2.setPosition(3)
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    # while robot.step(timestep) != -1:
        # head_motor.setPosition(pos)
        # motor2.setPosition(pos)
        # motor2.setPosition(pos)
        # motor3.setPosition(-pos)
        # time.sleep(0.1)
        
        # if add:
            # pos += 0.2
        # else:
            # pos -= 0.2
            
        # if pos >= 3:
            # add = False
        # elif pos <= 3:
            # add = True
    
    # Enter here exit cleanup code.
    
    
if __name__ == '__main__':
    main()