import re


class Rover:
    def __init__(self, Id, x, y, head, p):
        self._id = Id
        self._x = x
        self._y = y
        self._head = head
        self.p = p

    def getPos(self):
        return str(self._x)+" "+str( self._y)

    def getHead(self):
        return self._head

    def display(self):
        print("Final position of Rover", self._id, "is", self.getPos(), self.getHead()+".\n")

    def runRover(self, ins, heading):
        if (ins == ""):
            raise ValueError("Instruction sequence cannot be empty.")
        pattern = re.compile("^[MRL]*$")
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_head = heading.index(self._head)
        if pattern.match(ins):
            for i in ins:
                if i == 'L':
                    cur_head = (cur_head-1+4) % 4
                    self._head = heading[cur_head]
                elif i == 'R':
                    cur_head = (cur_head+1)%4
                    self._head = heading[cur_head]
                else:
                    x = self._x + shifts[cur_head][0]
                    y = self._y + shifts[cur_head][1]
                    if self.p.isOccupied(x, y):
                        raise ValueError("ERROR .... The position "+str((x,y))+" is already occupied so the rover got blocked.")
                    elif (x >= 0 and x <= self.p.x) and (y >= 0 and y <=self.p.y):
                        self._x = x
                        self._y = y
                    else:
                        raise ValueError("ERROR .... The Rover cannot be moved further "+str(heading[cur_head])+" or it will fall off the edge.")
        else:
            raise ValueError("Only values 'L', 'M' and 'R' are accepted!")



