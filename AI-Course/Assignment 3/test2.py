# %%
# Assumptions are as follows
# Computer is always X
# Computer is always the maximizer
# Human is always O
# Human is always the minimizer
# Human always goes first

from math import inf as infinity
from random import choice
import copy

# %%
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# %%
class State:
    def __init__(self, board, score):
        self.score = score
        self.board = board


def computerTurn(pos):
    board[pos[0]][pos[1]] = 1


def humanTurn(pos):
    board[pos[0]][pos[1]] = -1


def printBoard(b):
    for row in (b if (b) else board):
        for num in row:
            if num == 0:
                print('_   ', end=' ')
            elif num == 1:
                print('X   ', end=' ')
            elif num == -1:
                print('O   ', end=' ')
        print('\n')


def checkWin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if (board[i][0] == 1):
                return 'X'
            else:
                return 'O'
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            if (board[0][i] == 1):
                return 'X'
            else:
                return 'O'
    if board[0][0] == board[1][1] == board[2][2] != 0:
        if (board[0][0] == 1):
            return 'X'
        else:
            return 'O'
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        if (board[0][2] == 1):
            return 'X'
        else:
            return 'O'
    if (0 not in board[0] and 0 not in board[1] and 0 not in board[2]):
        return 'tie'
    return 0


def isLeaf():
    if checkWin(board) != 0:
        return True
    return False

# Create all states for some given depth


def createStates(board, player):
    states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # For empty spaces in the board
                tempBoard = copy.deepcopy(board)
                # If player is X (Computer), then the value is 1, else -1 (Human)
                tempBoard[i][j] = (1 if player == 'X' else -1)
                # Evaluate the board if it is the last depth else set the score to infinity or -infinity depending on the Minima or Maxima
                if isLeaf():
                    states.append(State(tempBoard, evaluate(board)))
                else:
                    states.append(
                        State(tempBoard, (-infinity if player == 'X' else infinity)))

    return states


def evaluate(board):
    if checkWin(board) == 'X':
        return 10
    elif checkWin(board) == 'O':
        return -10
    elif checkWin(board) == 'tie':
        return 0
    else:
        return -1


def minmax(state, player):
    # If last move or game is over, return the state
    # If final depth where score is set to evaluate(board) is reached, return the state
    if isLeaf():
        return state

    # Create all possible states
    states = createStates(state.board, player)
    # If Computer playing then find the maximum score for the depth
    if player == 'X':
        best = -infinity
        # For all states, find the maximum score
        for s in states:
            val = minmax(s, 'O')  # Call minmax for the next depth and player
            s.score = val.score  # Set the score of the state to the score of the returned state
            best = max(best, s.score)  # Find the maximum score
        for s in states:  # Return the state with the maximum score
            if s.score == best:  # If the score of the state is the maximum score
                return s  # Return the state
    else:
        best = infinity
        for s in states:
            val = minmax(s, 'X')
            s.score = val.score
            best = min(best, s.score)
        for s in states:
            if s.score == best:
                return s


def humanTurn(myGlobalState):
    while True:
        try:
            x = int(input('Enter x: '))
            y = int(input('Enter y: '))
            if myGlobalState.board[x][y] == 0:
                myGlobalState.board[x][y] = -1
                break
            else:
                print('Invalid move')
        except:
            print('Invalid move')


# %%
board = [
    [-1, -1, 0],
    [1, -1, -1],
    [1, 1, 1]
]
myGlobalState = State(board, None)
s = createStates(board, 'X')
print(s[0].score)
myGlobalState = minmax(myGlobalState, 'X')
print(myGlobalState.score)

# %%
# depth = 1
# myGlobalState = State(board,0,None)
# humanTurn(myGlobalState)
# while True:
#     printBoard(myGlobalState.board)
#     if checkWin(myGlobalState.board) != 0:
#         break
#     myGlobalState = minmax(myGlobalState,depth,'X')
#     print("Score is ", myGlobalState.score)
#     printBoard(myGlobalState.board)
#     if checkWin(myGlobalState.board) != 0:
#         break
#     humanTurn(myGlobalState)
#     depth+=1

# print(checkWin(myGlobalState.board), " Won the game") if checkWin != "tie" else print("Game Tied !")


# %%
# states = createStates(board, depth, "O")
# for state in states:
#     printBoard(state.board)
#     print(state.score)
#     print("\n")

# # printBoard()
# # print (checkWin(),"Won") if checkWin() != 0 else print("Game in Progress")
