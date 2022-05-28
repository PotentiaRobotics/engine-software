"""
This class keeps track of all the motors, sensors and import variables needed for the robot.
"""
class Propioception:
    """
    Standard kwargs to give for this function

    data = {
        # Motors (all units are in degrees)
        'left_hip_pitch': 0,
        'left_hip_yaw': 0,
        'left_hip_roll': 0,
        'left_knee_pitch': 0,
        'left_ankle_pitch': 0,
        'left_ankle_yaw': 0,
        'left_ankle_roll': 0,
        'right_hip_pitch': 0,
        'right_hip_yaw': 0,
        'right_hip_roll': 0,
        'right_knee_pitch': 0,
        'right_ankle_pitch': 0,
        'right_ankle_yaw': 0,
        'right_ankle_roll': 0,
        'left_shoulder_pitch': 0,
        'left_shoulder_yaw': 0,
        'left_shoulder_roll': 0,
        'left_elbow_pitch': 0,
        'right_shoulder_pitch': 0,
        'right_shoulder_yaw': 0,
        'right_shoulder_roll': 0,
        'right_elbow_pitch': 0,
        'torso_pitch': 0,
        'torso_yaw': 0,
        'torso_roll': 0,
        'neck_pitch': 0,
        'neck_yaw': 0,
        'neck_roll': 0,

        # Sensors
        # Add later
    }

    This will also have the constants
    """
    def __init__(self, **kwargs):
        self.data = {
            # Add defualt later
        }
        self.constants = {
            # Add some constants here later
        }
        for key, value in kwargs.items():
            self.data[str(key)] = value

    def update(self, partsAndValues):
        """
        This function updates the dictionary

        arg artsAndValues is {string --> int or float}

        Error codes:
        1 is success
        -1 is the error for NoneType variables
        -2 is for incorrect datatypes
        -3 is for when the key is not in the dictionary
        """

        if partsAndValues == None:
            return -1

        if type(partsAndValues) != dict:
            return -2

        for key in partsAndValues.keys():
            if key in self.data:
                self.data[str(key)] = partsAndValues[key]
            else:
                return -3
            return 1

    def add(self, partsAndValues):
        """
        This function will add a part to the system if needed

        arg artsAndValues is {string --> int or float}

        Error codes:
        1 is success
        -1 is the error for NoneType variables
        -2 is for incorrect datatypes
        -3 is for when the key is in the dictionary
        """

        if partsAndValues == None:
            return -1

        if type(partsAndValues) != dict:
            return -2

        for key in partsAndValues.keys():
            if key in self.data:
                return -3
            else:
                self.data[str(key)] = partsAndValues[key]
            return 1

    def remove(self, partsAndValues):
        """
        This function will remove a part to the system if needed

        arg artsAndValues is [string]

        Error codes:
        1 is success
        -1 is the error for NoneType variables
        -2 is for incorrect datatypes
        -3 is for when the key is not in the dictionary
        """

        if partsAndValues == None:
            return -1
            

        if type(partsAndValues) != list:
            return -2

        for key in partsAndValues:
            if key in self.data:
                self.data.pop(str(key))
            else:
                return -3
            return 1
        

# # Test
# stuff = Propioception(
#         left_hip_pitch= 0,
#         left_hip_yaw= 0,
#         left_hip_roll= 0,
#         left_knee_pitch= 0,
#         left_ankle_pitch= 0,
#         left_ankle_yaw= 0,
#         left_ankle_roll= 0,
#         right_hip_pitch= 0,
#         right_hip_yaw= 0,
#         right_hip_roll= 0,
#         right_knee_pitch= 0,
#         right_ankle_pitch= 0,
#         right_ankle_yaw= 0,
#         right_ankle_roll= 0,
#         left_shoulder_pitch= 0,
#         left_shoulder_yaw= 0,
#         left_shoulder_roll= 0,
#         left_elbow_pitch= 0,
#         right_shoulder_pitch= 0,
#         right_shoulder_yaw= 0,
#         right_shoulder_roll= 0,
#         right_elbow_pitch= 0,
#         torso_pitch= 0,
#         torso_yaw= 0,
#         torso_roll= 0,
#         neck_pitch= 0,
#         neck_yaw= 0,
#         neck_roll= 0
#         )
        
# """Update cases"""
# # Success case
# print(stuff.data['neck_roll'])        
# stuff.update({'neck_roll': 21})
# print(stuff.data['neck_roll'])

# # -1 case
# print(stuff.update(None))

# # -2 case
# print(stuff.update([]))

# # -3 case
# print(stuff.update({'test': 21}))

# """Remove cases"""
# # Success case
# print(stuff.data['neck_roll'])        
# print(stuff.remove(['neck_roll']))

# # -1 case
# print(stuff.remove(None))

# # # -2 case
# print(stuff.remove({}))

# # -3 case
# print(stuff.remove(['test']))

# """Add cases"""
# # Success case
# print('test' in stuff.data.keys())        
# stuff.add({'test': 21})
# print(stuff.data['test'])

# # -1 case
# print(stuff.add(None))

# # -2 case
# print(stuff.add([]))

# # -3 case
# print(stuff.add({'test': 21}))