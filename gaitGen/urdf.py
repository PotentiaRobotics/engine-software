from urdfpy import URDF

robot = URDF.load('olympian.urdf')

for link in robot.links:
    print(link.name)

print(robot.base_link.name)