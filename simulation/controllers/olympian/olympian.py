"""olympian controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def main():
    # create the Robot instance.
    print("Initializing world...")
    robot = Robot()
    
    head_motor = robot.getDevice("shoulder_pitch")
    motor2 = robot.getDevice("shoulder_roll")
    motor3 = robot.getDevice("shoulder_yaw")
    head_motor.setVelocity(1)
    motor2.setVelocity(1)
    motor3.setVelocity(1)
    pos = 0
    add = True
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        head_motor.setPosition(pos)
        # motor2.setPosition(pos)
        # motor3.setPosition(pos)
        
        if add:
            pos += 0.2
        else:
            pos -= 0.2
            
        if pos >= 3:
            add = False
        elif pos <= -3:
            add = True
    
    # Enter here exit cleanup code.
    
    
if __name__ == '__main__':
    main()