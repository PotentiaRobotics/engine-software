"""olympian controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def main():
    # create the Robot instance.
    print("Initializing world...")
    robot = Robot()
    
    head_motor = robot.getDevice("neck_pitch")
    head_motor.setVelocity(1)
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        head_motor.setPosition(6)
    
    # Enter here exit cleanup code.
    
    
if __name__ == '__main__':
    main()