import numpy as np

class Location:
    def __init__(self,x,y):
        self.cord =np.array([x,y])

    def calculateDistance(self,location):
        calc = self.cord.dot(location.cord)
        return np.sqrt(calc)
