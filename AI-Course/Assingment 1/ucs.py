# Each state is a node
# each visitied will be added to a list to avoid infinite loop on repeated states
# Will stop when goal state reached
import copy
from bootifulPrint import bootifulPrint
p = bootifulPrint()


class UCSPuzzle:
    def __init__(self):
        # Debug Variable
        self.debug = False
        # A priority Queue tuples| Used to know which node to visit next
        self.queue = []

        # Cost of moving
        self.cost = 1

        # G(n) Function  - Distance of node from goal | Will be calculated for every node, using the cost of moving
        self.gN = -1

        # States
        self.initialState = []
        self.currentState = []
        self.goalState = []

        # Visited
        self.visited = []

        # Tree created in the progress
        self.tree = []

        # For rows and columns of states
        self.row = 0
        self.col = 0

    def setDebug(self, t):
        self.debug = t

    def setInitialState(self):
        self.row = 0
        self.col = int(input("Enter the number of Columns : "))
        for i in range(0, self.col):
            myList = [int(items) for items in input(
                "Enter integers seprated by space, press enter to save the row : ").strip().split()]
            for i, x in enumerate(myList):
                self.row += 1
            self.initialState.append(myList)

    def setInitialState(self, g):
        self.initialState = g.copy()
        self.row = 0
        self.col = 0

        # Set Rows and columns
        for i, x in enumerate(g):
            self.col += 1
            for j, z in enumerate(x):
                self.row += 1

    def printState(self, state):
        for arr in state:
            p.printArray(arr, "\n")

    def setGoalState(self):
        if self.col == 0:
            print("PLEASE ENTER INIT STATE FIRST !")
            return
        for i in range(0, self.col):
            myList = [int(items) for items in input(
                "Enter integers seprated by space, press enter to save the row : ").strip().split()]
            self.goalState.append(myList)

    def setGoalState(self, g):
        self.goalState = g.copy()

    def printInitialState(self):
        self.printState(self.initialState)

    def printGoalState(self):
        self.printState(self.goalState)

    # Find the location of given element from the given state
    def findElement(self, x, state):
        for i, arr in enumerate(state):
            if x in arr:
                index = (i, arr.index(x))
        return index

    # Calculate distnace from given state to goal state
    def calculateGN(self, state, x):
        # Original Index of element
        indexOG = self.findElement(x, state)
        # Location of element in the Goal State
        indexG = self.findElement(x, self.goalState)
        cost = abs(indexG[0]-indexOG[0]) + abs(indexG[1]-indexOG[1])

        if self.debug:
            print("For element ", x)
            print("OGIndex = ", indexOG, "GoalIndex = ", indexG)
            print("Cost = ", cost)
        return cost

    def swapIndex(self, state, index1, index2):
        # NEW THING LEARNED PYTHON SUTPIDLY OVERWRITES LISTS AS IF ITS A GLOBAL VARIABLE **** We need to create Deep copy
        newState = copy.deepcopy(state)

        temp = newState[index1[0]][index1[1]]
        newState[index1[0]][index1[1]] = newState[index2[0]][index2[1]]
        newState[index2[0]][index2[1]] = temp

        return newState

    def Discover(self, state):
        # Discover States that be achienved from given state
        index = self.findElement(-1, state)
        # 4 ways UP DOWN LEFT RIGHT
        up = (index[0]-1, index[1])
        down = (index[0]+1, index[1])
        left = (index[0], index[1]-1)
        right = (index[0], index[1]+1)

        stateUP = None
        stateDOWN = None
        stateLEFT = None
        stateRIGHT = None

        # Check if possible and then proceed to create the states
        if (up[0] >= 0 and up[1] >= 0 and up[0] < 3 and up[1] < 3):
            stateUP = self.swapIndex(state, up, index)

        if (down[0] >= 0 and down[1] >= 0 and down[0] < 3 and down[1] < 3):
            stateDOWN = self.swapIndex(state, down, index)

        if (left[0] >= 0 and left[1] >= 0 and left[0] < 3 and left[1] < 3):
            stateLEFT = self.swapIndex(state, left, index)
        if (right[0] >= 0 and right[1] >= 0 and right[0] < 3 and right[1] < 3):
            stateRIGHT = self.swapIndex(state, right, index)

        return (stateUP, stateDOWN, stateLEFT, stateRIGHT)

    def Solve(self):
        steps = 0
        # Start from Init state as root node / root state
        self.currentState = copy.deepcopy(self.initialState)

        while (True):
            self.visited.append(self.currentState)  # Add to visited
            steps += 1
            states = self.Discover(self.currentState)
            self.tree.append(self.currentState)
            # Caluclate G(n) for each state

            for state in states:
                cost = 0
                if state != None:
                    for arr in state:
                        for num in arr:
                            cost += self.calculateGN(state, num)
                    if (state not in self.visited):  # IGNORE VISITED NODES
                        self.queue.append((cost, state))

            self.queue.sort(key=lambda x: x[0])  # Sort by Priority

            self.currentState = (self.queue[0])[1]
            if ((self.queue[0])[0] == 0):
                self.visited.append(self.currentState)
                break
            self.queue.pop(0)

        print("SOLVED IN STEPS = ", steps)

    def printTraversal(self):
        for v in self.visited:
            self.printState(v)
            print("\n")


if __name__ == "__main__":
    # g_init = [
    #     [1, 2, 4],
    #     [3, -1, 5],
    #     [8, 6, 7],
    # ]
    # g_final = [
    #     [-1, 1, 2],
    #     [3, 4, 5],
    #     [6, 7, 8],
    # ]

    g_init = [
        [2, 8, 3],
        [1, 6, 4],
        [7, -1, 5],
    ]
    g_final = [
        [1, 2, 3],
        [8, -1, 4],
        [7, 6, 5],
    ]

    myUCS = UCSPuzzle()
    myUCS.setDebug(False)
    print("###### INITIAL STATE ######")
    myUCS.setInitialState(g_init)
    myUCS.setGoalState(g_final)
    myUCS.printInitialState()
    print("####### SOLVING #######")
    myUCS.Solve()
    myUCS.printTraversal()
