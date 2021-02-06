"""Olympian Controller"""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Accelerometer, Gyro

def integral(error, priorIntegral):
  global timestep
  return priorIntegral + error * timestep

def derivative(error, priorError):
  global timestep
  return (error-priorError)/timestep

def actuatorMovement(robot, pidOutput):
  #Inverse Kinematic Equation
  continue

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

  derivativeX = derivative(error[0], priorError[0])
  derivativeY = derivative(error[1], priorError[1])
  integralX = integral(error[0], priorIntegral[0])
  integralY = integral(error[1], priorIntegral[1])

  ux = Kp*error[0] + Ki * integralX + Kd * derivativeX + xBias
  uy = Kp*error[1] + Ki * integralY + Kd * derivativeY + yBias

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

def calculateCOM(robot):
  continue

def main():
  print("Initializing Olympiad...")
  robot = Robot()
  
  # get the time step of the current world.
  global timestep
  timestep = int(robot.getBasicTimeStep())
  
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

  while robot.step(timestep) != -1:
    xObs, yObs = calculateZMP(gyro, accel)
    error = [desiredXZMP-xObs, desiredYZMP-yObs]
    controllerPID(robot, error, priorError, priorIntegral)


if __name__ == '__main__':
    main()