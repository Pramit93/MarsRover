class Plateau:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = {}

    def isOccupied(self, x, y):
        if str(x)+" "+str(y) in self.occupied:
            return True
        else:
            return False
