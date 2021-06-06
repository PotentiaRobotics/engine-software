from controller import Supervisor

while True:
    # all body names are found above in the body names list
    body = Supervisor.getFromDef(body_name) 
    center_of_mass = body.getCenterOfMass()
    print(center_of_mass)
    # center_of_mass is a list with 3 values, the x y and z coord of the COM
    