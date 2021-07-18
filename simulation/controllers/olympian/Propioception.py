
class Propioception:
    def __init__(self):
        self.data = {
            'locationX' = 0,
            'locationY' = 0,
            'locationZ' = 0,
            ''
        }

    def update(self, partsAndValues):
        """
        This function updates the dictionary

        arg artsAndValues is {string --> int or float}

        Error codes:
        1 is success
        -1 is the error for NoneType variables
        -2 is for incorrect datatypes
        """

        if partsAndValues == None:
            return -1

        if type(partsAndValues) != dict:
            return -2

        for key in partsAndValues.keys():
            self.data[key] = partsAndValues[key]
