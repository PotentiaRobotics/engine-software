"""olympian controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import time

def main():
    # create the Robot instance.
    print("Initializing world...")
    robot = Robot()
    timestep = 64
    start = 0
    while robot.step(32) != -1:
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