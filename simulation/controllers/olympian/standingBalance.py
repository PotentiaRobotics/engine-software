"""Olympian Controller"""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Accelerometer, Gyro

def integral(error, priorIntegral):
  return priorIntegral + error * (TIMESTEP+1 - TIMESTEP)

def derivative(error, priorError):
  return (error-priorError)/(TIMESTEP+1 - TIMESTEP)

def actuatorMovement(robot, pidOutput):
  #Inverse Kinematic Equation
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
  tauI = 0.0 # tauI is the reset time, which is a tuning param for integral
  tauD = 0.0 # tauD is derivative time. Tuning param for derivative
  maxMotor = 1.0 # How big the signal that goes to the actuator is
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
    integralX = integralX - error[0]*(TIMESTEP+1 - TIMESTEP)
  elif(ux < minMotor):
    ux = minMotor
    integralX = integralX - error[0]*(TIMESTEP+1 - TIMESTEP)
  
  uy = nominalValue + Kc*error[1] + Kc/tauI * integralY + Kc * tauD * derivativeY

  if(uy > maxMotor):
    uy = maxMotor
    integralY = integralY - error[1]*(TIMESTEP+1 - TIMESTEP)
  elif(ux < minMotor):
    uy = minMotor
    integralY = integralY - error[1]*(TIMESTEP+1 - TIMESTEP)

  priorError = error
  priorIntegral = [integralX, integralY]

  actuatorMovement(robot, [ux, uy])


def calculateZMP(gyro, accel):
  # [x,y,z] data -- assuming placed at CoM
  gData = gyro.getValues()
  aData = gyro.getValues()

  CoM_height = 1 # some constant value for CoM Height from Ground
  gravity = 9.81

  xObs = -CoM_height/gravity * aData[0]
  yObs = -CoM_height/gravity * aData[1]

  return xObs, yObs

# Might have to actually code this later
def calculateCOM(robot):
  return

def main():
  print("Initializing Olympiad...")
  robot = Robot()
  
  # get the time step of the current world.
  global TIMESTEP
  TIMESTEP = int(robot.getBasicTimeStep())
  
  # gyroscope, accelorometer
  gyro = robot.getDevice("gyro.wbt name")
  accel = robot.getDevice("accel .wbt name")

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