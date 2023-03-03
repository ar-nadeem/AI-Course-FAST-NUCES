# Each state is a node
# each visitied will be added to a list to avoid infinite loop on repeated states
# Will stop when goal state reached


# THINGS TO DO
# 1. Make the misplacedTile function in Super class more efficient

import copy
import time
from bootifulPrint import bootifulPrint
p = bootifulPrint()


class Node:
    def __init__(self, state, parent, stepTaken=None, cost=None):
        self.state = state
        self.parent = parent
        self.stepTaken = stepTaken
        self.cost = cost

    def setCost(self, cost):
        self.cost = cost


class Puzzle:
    def __init__(self):
        # Debug Variable
        self.debug = False
        # A priority Queue list | Used to know which node to visit next
        self.queue = []

        # Cost of moving
        self.cost = 1

        # G(n) Function  - Distance of node from goal | Will be calculated for every node, using the cost of moving
        self.gN = -1

        # States
        self.initialState = []
        self.currentState = None
        self.goalState = []

        # Visited
        self.visited = []

        # Tree created in the progress
        self.tree = []

        # Blank Space Tile
        self.blank = -1

        # For rows and columns of states
        self.row = 0
        self.col = 0

    def setDebug(self, t):
        self.debug = t

    def setBlank(self, t):
        self.blank = t

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
    def calculateGN(self, state):
        cost = 0
        parent = state.parent
        if parent == None:
            return cost
        else:
            while (parent != None):
                cost += 1
                parent = parent.parent
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
        index = self.findElement(self.blank, state.state)
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
            stateUP = Node(self.swapIndex(state.state, up, index), state, "UP")

        if (down[0] >= 0 and down[1] >= 0 and down[0] < 3 and down[1] < 3):
            stateDOWN = Node(self.swapIndex(
                state.state, down, index), state, "DOWN")

        if (left[0] >= 0 and left[1] >= 0 and left[0] < 3 and left[1] < 3):
            stateLEFT = Node(self.swapIndex(
                state.state, left, index), state, "LEFT")
        if (right[0] >= 0 and right[1] >= 0 and right[0] < 3 and right[1] < 3):
            stateRIGHT = Node(self.swapIndex(
                state.state, right, index), state, "RIGHT")

        return (stateUP, stateDOWN, stateLEFT, stateRIGHT)

    def manhattanD(self, state, x):
        # Original Index of element
        indexOG = self.findElement(x, state.state)
        # Location of element in the Goal State
        indexG = self.findElement(x, self.goalState)
        cost = abs(indexG[0]-indexOG[0]) + abs(indexG[1]-indexOG[1])

        if self.debug:
            print("For element ", x)
            print("OGIndex = ", indexOG, "GoalIndex = ", indexG)
            print("Cost = ", cost)
        return cost

    def miplacedT(self, state, x):
        # Original Index of element
        indexOG = self.findElement(x, state.state)
        # Location of element in the Goal State
        indexG = self.findElement(x, self.goalState)
        if (indexG == indexOG):
            cost = 0
        else:
            cost = 1

        if self.debug:
            print("For element ", x)
            print("OGIndex = ", indexOG, "GoalIndex = ", indexG)
            print("Cost = ", cost)
        return cost

    def costFunction(self, state=None, num=None):
        return None

    def Solve(self):
        if (self.__class__.__name__ == "Puzzle"):
            print("PLEASE DO NOT USE THE SUPER CLASS !")
            exit(0)
        steps = 0
        # Start from Init state as root node / root state
        # Root Node has no parent
        self.currentState = Node(copy.deepcopy(
            self.initialState), None, None, 0)

        while (True):
            self.visited.append(self.currentState)  # Add to visited
            steps += 1
            states = self.Discover(self.currentState)
            self.tree.append(self.currentState)
            # Caluclate G(n) for each state

            # For each state calculate G(n) and add to queue
            for state in states:
                cost = 0
                if state != None:
                    # Calculate Cost for each state
                    cost += self.costFunction(state)
                    state.setCost(cost)
                    if (state not in self.visited):  # IGNORE VISITED NODES
                        self.queue.append((cost, state))
            # print("STEPS = ", steps)

            if self.debug:
                self.printState(self.currentState.state)
                print(self.currentState.cost)
                print("\n")
                time.sleep(1)
            self.queue.sort(key=lambda x: x[0])  # Sort by Priority
            self.currentState = (self.queue[0])[1]

            # Check if Goal State is reached
            if (self.currentState.state == self.goalState):
                self.visited.append(self.currentState)
                self.finalState = self.currentState
                # Generate Solution
                self.generateSolution()
                break

            # Else Remove the state from queue
            self.queue.pop(0)

        print("SOLVED IN Iterations = ", steps)

    # Print the Traversal
    def printTraversal(self):
        print("Traversal which has ", len(self.tree), " steps : ")
        for node in self.tree:
            self.printState(node.state)
            print("\n")

    def printTraversalSteps(self):
        print("Traversal which has ", len(self.tree), " steps : ")
        for node in self.tree:
            print("Step = ", node.stepTaken)
            self.printState(node.state)
            print("\n")

    def generateSolution(self):
        # Prepare the solution
        self.solutionTree = []
        parent = self.finalState.parent
        self.solutionTree.append(self.finalState)
        while (parent != None):
            self.solutionTree.append(parent)
            parent = parent.parent

    def printSolution(self):
        # Print the solution
        print("SOLUTION which takes ", len(self.solutionTree)-1, " steps : ")
        for node in reversed(self.solutionTree):
            self.printState(node.state)
            print("\n")

    def printSolutionSteps(self):
        # Print the solution with steps
        print("SOLUTION which takes ", len(self.solutionTree)-1, " steps : ")
        for node in reversed(self.solutionTree):
            print("Step = ", node.stepTaken)
            self.printState(node.state)
            print("\n")


# Inherit from Puzzle
# Child classes that implement the cost function, effectivly implementing the search algorithm
class UCS(Puzzle):
    def __init__(self):
        super().__init__()

    def costFunction(self, state=None, num=None):
        if state != None:
            # Cost of path is G(n) which is the number of branchs
            return (self.calculateGN(state))
        else:
            return None


class GreedyBFS(Puzzle):
    def __init__(self, type="MH"):
        self.type = type
        super().__init__()

    def costFunction(self, state=None, num=None):
        if state != None:

            cost = 0
            for arr in state.state:
                for num in arr:
                    if self.type == "MH":
                        # if you want to use manhattan distance
                        cost += self.manhattanD(state, num)
                    elif self.type == "MT":
                        # if you want to use misplaced tiles
                        cost += self.miplacedT(state, num)
            return cost

        else:
            return None


class Astar(Puzzle):
    def __init__(self, type="MH"):
        self.type = type
        super().__init__()

    def costFunction(self, state=None, num=None):
        if state != None:

            cost = 0
            for arr in state.state:
                for num in arr:
                    if self.type == "MH":
                        # if you want to use manhattan distance
                        cost += self.manhattanD(state, num)
                    elif self.type == "MT":
                        # if you want to use misplaced tiles
                        cost += self.miplacedT(state, num)
            # Always add the cost of the path G(n)
            cost += self.calculateGN(state)
            return cost

        else:
            return None


if __name__ == "__main__":
    g_init = [
        [-1, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
    ]
    g_final = [
        [1, 2, 3],
        [8, -1, 4],
        [7, 6, 5],
    ]

    # -------------
    # | 0 | 3 | 6 |
    # -------------
    # | 1 | 4 | 7 |
    # -------------
    # | 2 | 5 | 8 |
    # -------------
    #
    # The goal is defined as:
    #
    # -------------
    # | 1 | 2 | 3 |
    # -------------
    # | 8 | 0 | 4 |
    # -------------
    # | 7 | 6 | 5 |
    # -------------
    gbfs = GreedyBFS("MH")  # Manhattan Distance
    gbfs.setDebug(True)
    gbfs.setInitialState(g_init)
    gbfs.setGoalState(g_final)
    gbfs.printInitialState()
    print("####### SOLVING #######")
    gbfs.Solve()
    gbfs.printSolutionSteps()
