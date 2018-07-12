import lib.rover as rv
import lib.plateau as pt
import unittest


class TestRover(unittest.TestCase):

    def test_runRover(self):
        p = pt.Plateau(5, 5)
        print("\nSize of the plateau is set to (x=5,y=5) at top right corner.\n")
        id=1



        print("TestCase 1")
        print("----------")
        print("Trying to place Rover at x=2,y=3 facing North.")
        print("Instruction Sequence - LRMMRM")
        test_runRover = rv.Rover(id, 2, 3, 'N', p)
        test_runRover.runRover("LRMMRM", ('N', 'E', 'S', 'W'))
        self.assertEqual(test_runRover .getPos(), "3 5")
        self.assertEqual(test_runRover .getHead(), "E")
        p.occupied[test_runRover.getPos()] = 1
        test_runRover.display()
        id+=1



        print("TestCase 2")
        print("----------")
        print("Checking whether the grid (x=3,y=5) of the plateau is empty.")
        self.assertTrue(test_runRover.p.isOccupied(3, 5))
        print("The grid (x=3,y=5) of the plateau is occupied so a rover cannot be landed here.\n")



        print("TestCase 3")
        print("----------")
        print("Trying to place Rover at x=2,y=3 facing North.")
        print("Instruction Sequence - LRMMRM")
        test_runRover = rv.Rover(id, 2, 3, 'N', p)
        with self.assertRaises(ValueError) as context:
            test_runRover.runRover("LRMMRM", ('N', 'E', 'S', 'W'))
        p.occupied[test_runRover.getPos()] = 1
        print(context.exception)
        test_runRover.display()
        id+=1



        print("TestCase 4")
        print("----------")
        print("Trying to place Rover at x=2,y=3 facing North.")
        print("Instruction Sequence - MMMRMMMLM")
        test_runRover = rv.Rover(id, 2, 3, 'N', p)
        with self.assertRaises(ValueError) as context:
            test_runRover.runRover("MMMRMMMLM", ('N', 'E', 'S', 'W'))
        p.occupied[test_runRover.getPos()] = 1
        print(context.exception)
        test_runRover.display()
        id+=1



        print("TestCase 5")
        print("----------")
        print("Trying to place Rover at x=2,y=4 facing North.")
        print("Instruction Sequence - RMMMLMM")
        test_runRover = rv.Rover(id, 2, 4, 'N', p)
        with self.assertRaises(ValueError) as context:
            test_runRover.runRover("RMMMLMM", ('N', 'E', 'S', 'W'))
        p.occupied[test_runRover.getPos()] = 1
        print(context.exception)
        test_runRover.display()
        id += 1



        print("TestCase 6")
        print("----------")
        print("Trying to place Rover at x=1,y=1 facing North.")
        print("Instruction Sequence - lmr")
        test_runRover = rv.Rover(id, 2, 3, 'N', p)
        with self.assertRaises(ValueError) as context:
            test_runRover.runRover("lmr", ('N', 'E', 'S', 'W'))
        print(str(context.exception) + "\n")
        id+=1



        print("TestCase 7")
        print("----------")
        print("Trying to place Rover at x=1,y=1 facing North.")
        print("Instruction Sequence - empty")
        test_runRover = rv.Rover(id, 2, 3, 'N', p)
        with self.assertRaises(ValueError) as context:
            test_runRover.runRover("", ('N', 'E', 'S', 'W'))
        print(str(context.exception) + "\n")
        id += 1


if __name__ == '__main__':
    unittest.main()


