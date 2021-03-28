"""Olympian Controller"""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Accelerometer, Gyro, TouchSensor, Supervisor
import time

def integral(error, priorIntegral):
  return priorIntegral + error * (TIMESTEP)

def derivative(error, priorError):
  return (error-priorError)/(TIMESTEP)

def actuatorMovement(robot, pidOutput):
  #Inverse Kinematic Equation
  torso_pitch = robot.getDevice("torso_pitch")
  right_knee_pitch = robot.getDevice("left_hip_pitch")
  left_knee_pitch = robot.getDevice("right_hip_pitch")

  if pidOutput[0] > 0.5:
     torso_pitch.setVelocity(1000)
     right_knee_pitch.setVelocity(1000)
     left_knee_pitch.setVelocity(1000)
     torso_pitch.setPosition(-1.3)   
     right_knee_pitch.setPosition(-1.3)   
     left_knee_pitch.setPosition(-1.3)   
     print("here1")
  elif pidOutput[0] < -0.5:
     torso_pitch.setVelocity(1000)
     right_knee_pitch.setVelocity(1000)
     left_knee_pitch.setVelocity(1000)
     torso_pitch.setPosition(1.3)   
     right_knee_pitch.setPosition(1.3)   
     left_knee_pitch.setPosition(1.3)   
     print("here2")
  return

def controllerPID(robot, error, priorError, priorIntegral):
  # Constant values we change to try to optimize
  # Kp is relevant for dominant response of system
  # Ki brings memory into the system
  # Kd responsible for the rate of change of this controller
  Kp = 1
  Ki = 0
  Kd = 0
  #Usually not needed, but just in case we ever need nonstop motion
  xBias = 0
  yBias = 0

  nominalValue = 0.0
  Kc = 1.0 # Kc is the controller gain
  tauI = 1.0 # tauI is the reset time, which is a tuning param for integral
  tauD = 0.0 # tauD is derivative time. Tuning param for derivative
  maxMotor = 1000.0 # How big the signal that goes to the actuator is
  minMotor = 0.0 # How small the signal that goes to the actuator is
  
  integralX = integral(error[0], priorIntegral[0])
  integralY = integral(error[1], priorIntegral[1])
  
  if(TIMESTEP >= 1):
    derivativeX = derivative(error[0], priorError[0])
    derivativeY = derivative(error[1], priorError[1])
  else:
    derivativeX = 0.0
    derivativeY = 0.0


  ux = nominalValue + Kc*error[0] + Kc/tauI * integralX + Kc * tauD * derivativeX
  
  if(ux > maxMotor):
    ux = maxMotor
    integralX = integralX - error[0]*(TIMESTEP)
  elif(ux < minMotor):
    ux = minMotor
    integralX = integralX - error[0]*(TIMESTEP)
  
  uy = nominalValue + Kc*error[1] + Kc/tauI * integralY + Kc * tauD * derivativeY

  if(uy > maxMotor):
    uy = maxMotor
    integralY = integralY - error[1]*(TIMESTEP)
  elif(ux < minMotor):
    uy = minMotor
    integralY = integralY - error[1]*(TIMESTEP)

  priorError = error
  priorIntegral = [integralX, integralY]

  print("ux " + str(ux))
  print("uy " + str(uy))

  actuatorMovement(robot, [ux, uy])


def calculateZMP(gyro, accel):
  # [x,y,z] data -- assuming placed at CoM
  gData = gyro.getValues()
  aData = gyro.getValues()

  CoM_height = 1 # some constant value for CoM Height from Ground
  gravity = 9.81

  xObs = -CoM_height/gravity * aData[0]
  yObs = -CoM_height/gravity * aData[2]

  return xObs, yObs

def calculateCOM(robot):
    links = ["left_foot", "left_shin", "left_thigh", "left_lower_arm", "left_upper_arm", "right_foot", "right_shin", 
              "right_thigh", "right_lower_arm", "right_upper_arm", "torso", "head", "pelvis"]
    
    centerOfMass = [0, 0, 0]
    
    for i in links:
        temp = Supervisor.getFromDef(i)
        tempCOM = temp.getCenterOfMass()
        centerOfMass += tempCOM
    
    return centerOfMass/8.18

def main():
  print("Initializing Olympiad...")
  robot = Robot()
  
  # get the time step of the current world.
  global TIMESTEP
  TIMESTEP = int(robot.getBasicTimeStep())

  # gyroscope, accelorometer
  gyro = robot.getDevice("torso_gyro")
  accel = robot.getDevice("torso_accelerometer")

  gyro.enable(TIMESTEP)
  accel.enable(TIMESTEP)
  
  # If the ZMP is stable then there will be no trajectory
  # Assumes that the base-frame-origin is in between the two feet since it's standing
  # This stays under the x and y coor of the COM (assuming standing straight)
  desiredXZMP = 0
  desiredYZMP = 0

  priorError = [0,0]
  priorIntegral = [0, 0]

  while robot.step(TIMESTEP) != -1:
    xObs, yObs = calculateZMP(gyro, accel)
    error = [desiredXZMP-xObs, desiredYZMP-yObs]
    controllerPID(robot, error, priorError, priorIntegral)


if __name__ == '__main__':
    main()


# def main():
    #create the Robot instance.
    # print("Initializing world...")
    # robot = Robot()
    # timestep = 16
    # curr_time = 0
    
    # lfootsensor = robot.getDevice("torso_gyro")
    
        
    # while robot.step(timestep) != -1:
        #print(calculateCOM(robot))
        # curr_time += timestep/1000.0
        #head_motor = robot.getDevice("torso_yaw")
        # motor2 = robot.getDevice("neck_roll")
        # lknee = robot.getDevice("left_knee_pitch")
        # rknee = robot.getDevice("right_knee_pitch")
        # lhip = robot.getDevice("left_hip_pitch")
        # rhip = robot.getDevice("right_hip_pitch")
        # lfootsensor.enable(10)
        
        
        #print sensor data every second
        
        # if curr_time % 1 < 0.01:
            
            # print(lfootsensor.getValues())
            
        #lfoot = robot.getDevice("left_ankle_pitch")
        #rfoot = robot.getDevice("right_ankle_pitch")

def func():
 
    torso_pitch = robot.getDevice("torso_pitch")
    
    lknee.setVelocity(2)
    lknee.setPosition(1)
    torso_pitch.setVelocity(2)

    
    lhip.setVelocity(2)
    rhip.setVelocity(2)
    lhip.setPosition(-1)
    torso_pitch.setPosition(0.2)

    
    if curr_time > 1:
        lknee.setPosition(0.1)
        lhip.setPosition(0.5)
        torso_pitch.setPosition(0.7)
    
    
main()