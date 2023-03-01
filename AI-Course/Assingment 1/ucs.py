# Each state is a node
# each visitied will be added to a list to avoid infinite loop on repeated states
# Will stop when goal state reached
from bootifulPrint import bootifulPrint
p = bootifulPrint()


class UCSPuzzle:
    def __init__(self):
        # A priority Queue | Used to know which node to visit next
        self.queue = []

        # Cost of moving
        self.cost = 1

        # G(n) Function  - Distance of node from goal | Will be calculated for every node, using the cost of moving
        self.gN = -1

        # States
        self.initialState = []
        self.currentState = []
        self.goalState = []

    def setInitialState(self):
        col = int(input("Enter the number of Columns : "))
        for i in range(0, col):
            myList = [int(items) for items in input(
                "Enter integers seprated by space, press enter to save the row : ").strip().split()]
            self.initialState.append(myList)

    def setInitialState(self, g):
        self.initialState = g

    def setGoalState(self):
        col = int(input("Enter the number of Columns : "))
        for i in range(0, col):
            myList = [int(items) for items in input(
                "Enter integers seprated by space, press enter to save the row : ").strip().split()]
            self.goalState.append(myList)

    def setGoalState(self, g):
        self.goalState = g

    def printInitialState(self):
        for arr in self.initialState:
            p.printArray(arr, "\n")

    def printGoalState(self):
        for arr in self.initialState:
            p.printArray(arr, "\n")


if __name__ == "__main__":
    g_init = [
        [1, 2, 4],
        [3, -1, 2],
        [8, 6, 7],
    ]
    g_final = [
        [-1, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
    myUCS = UCSPuzzle()
    myUCS.setInitialState(g_init)
    myUCS.printInitialState()
    myUCS.setGoalState(g_final)
    myUCS.printGoalState()
