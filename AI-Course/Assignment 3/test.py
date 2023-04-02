from math import inf as infinity
from random import choice
import copy

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


class State:
    def __init__(self, board, depth, score):
        self.score = score
        self.board = board
        self.depth = depth


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

# Create all states for some given depth


def createStates(board, depth, player):
    states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # For empty spaces in the board
                tempBoard = copy.deepcopy(board)
                # If player is X (Computer), then the value is 1, else -1 (Human)
                tempBoard[i][j] = (1 if player == 'X' else -1)
                # Evaluate the board if it is the last depth else set the score to infinity or -infinity depending on the Minima or Maxima
                if (depth != 9):
                    states.append(
                        State(tempBoard, depth, (-infinity if depth % 2 == 0 else infinity)))
                else:
                    states.append(State(tempBoard, depth, evaluate(board)))
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


def minmax(state, depth, player):
    # If last move or game is over, return the state
    # If final depth where score is set to evaluate(board) is reached, return the state
    if depth == 8:
        return state

    # Create all possible states
    states = createStates(state.board, depth, player)
    # If Computer playing then find the maximum score for the depth
    if player == 'X':
        best = -infinity
        # For all states, find the maximum score
        for s in states:
            # Call minmax for the next depth and player
            val = minmax(s, depth+1, 'O')
            s.score = val.score  # Set the score of the state to the score of the returned state
            best = max(best, s.score)  # Find the maximum score
        for s in states:  # Return the state with the maximum score
            if s.score == best:  # If the score of the state is the maximum score
                return s  # Return the state
    else:
        best = infinity
        for s in states:
            val = minmax(s, depth+1, 'X')
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


depth = 1
myGlobalState = State(board, 0, None)
humanTurn(myGlobalState)
while True:
    printBoard(myGlobalState.board)
    if checkWin(myGlobalState.board) != 0:
        break
    myGlobalState = minmax(myGlobalState, depth, 'X')
    print("Score is ", myGlobalState.score)
    printBoard(myGlobalState.board)
    if checkWin(myGlobalState.board) != 0:
        break
    humanTurn(myGlobalState)
    depth += 1

print(checkWin(myGlobalState.board),
      " Won the game") if checkWin != "tie" else print("Game Tied !")
