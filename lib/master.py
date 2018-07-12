'''
The mainrun() function is the primary entry-point of the program. It takes all the input, checks the input format is 
correct at each step and creates the Rover and Plateau objects.
'''

import plateau as pt
import rover as rv

def mainrun():
    print("Project X")
    print("Mars Rover Simulation Program Initiating.....")
    x_plateau = 0
    y_plateau = 0
    while 1:
        print("Enter the upper right x,y co-ordinates of the plateau (both x and y must be > 0)")
        try:
            x_plateau, y_plateau = map(int, input().strip().split())
            if x_plateau & y_plateau == 0:
                raise ValueError("x or y cannot be 0")
        except ValueError as e:
            print(e)
            print("ERROR in input, please try again ...")
            continue
        else:
            p = pt.Plateau(x_plateau, y_plateau)
            while 1:
                print("Enter the number of rovers you want to place")
                try:
                    n_rovers = int(input())
                except ValueError as e:
                    print(e)
                    print("ERROR in input, please try again ...")
                    continue
                else:
                    break
            heading = ('N', 'E', 'S', 'W')
            for i in range(1, n_rovers + 1):
                while 1:
                    print("Enter the start x,y coordinate and the heading of the rover", i)
                    try:
                        x_org, y_org, head = input().strip().split()
                        x_org = int(x_org)
                        y_org = int(y_org)
                        #below code checks whether the landing coordinate of the rover are within (0,0) and (x_plateau,y_plateau)
                        if (x_org < 0 or x_org > x_plateau) or (y_org < 0 or y_org > y_plateau):
                            raise ValueError("x,y co-ordinates of the rover must be within 0,0 and " + str(x_plateau) + "," + str(y_plateau))
                        #below code checks whether the heading of the rover is in ['N', 'E', 'S', 'W']
                        if head not in heading:
                            raise ValueError("Heading of the rover must be one among " + str(heading))
                        #below code checks whether the landing coordinate of the rover is occupied or free
                        if p.isOccupied(x_org, y_org):
                            raise ValueError("Given co-ordinates already occupied by previous rovers")
                    except ValueError as e:
                        print(e)
                        print("ERROR in input, please try again ...")
                        continue
                    else:
                        r = rv.Rover(i, x_org, y_org, head, p)
                        try:
                            print("Enter the instructions for the rover to move")
                            ins = input().strip()
                            r.runRover(ins, heading)
                        except ValueError as e:
                            print(e)
                        finally:
                            #the last position of the rover is recorded and blocked

                            p.occupied[r.getPos()] = 1
                            r.display()
                            break
            break


if __name__ == "__main__":
    mainrun()
