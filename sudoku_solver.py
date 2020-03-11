# Sudoku boards

easy = [[4, 0, 0, 0, 0, 0, 0, 0, 2],
        [1, 6, 2, 7, 0, 4, 5, 9, 8],
        [0, 0, 8, 0, 1, 9, 7, 6, 0],
        [2, 5, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 7, 3, 0, 0, 9, 1, 0],
        [9, 1, 0, 5, 0, 0, 4, 2, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 6, 0, 5, 1, 0, 0, 0],
        [8, 9, 0, 0, 0, 3, 2, 0, 6]]

medium = [[0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 5, 7, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 6, 1],
        [0, 0, 0, 2, 4, 8, 1, 0, 0],
        [2, 0, 0, 0, 6, 9, 0, 0, 0],
        [4, 0, 6, 0, 7, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 7, 9, 8, 4],
        [6, 4, 9, 0, 0, 0, 2, 5, 0],
        [0, 0, 7, 0, 9, 4, 0, 0, 0]]

hard = [[0, 0, 4, 8, 6, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 9, 0],
        [8, 0, 0, 0, 0, 9, 0, 6, 0],
        [5, 0, 0, 2, 0, 6, 0, 0, 1],
        [0, 2, 7, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 4, 3, 0, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 1, 5]]

expert = [[0, 7, 0, 3, 0, 5, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 1, 0, 8],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 4, 0, 0, 0, 0, 0],
        [0, 9, 8, 0, 0, 2, 0, 0, 7],
        [7, 0, 4, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 6, 8, 0, 0, 4, 3],
        [6, 0, 0, 0, 0, 0, 0, 0, 0]]


def display_grid(board):
    # print dashed horizontal line
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        # print out pipe every 3 numbers
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            # print numbers on board
            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end="")

def empty_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            # find where an empty spot is
            if board[i][j] == 0:
                # return empty spot location i.e. where there is a zero
                return (i, j)
    return False


def solver(board):

    # found solution
    # board will be full and valid function satisfied

    ################################################
    # only print this out to see backtracking steps
    # print(board)
    ################################################

    empty = empty_spot(board)
    if not empty:
        return True
    else:
        row, column = empty

    # set row, column to what i is
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            # if true, found the solution
            if solver(board):
                return True

        # if value fails, reset it back to zero and try again
        board[row][column] = 0

    return False



def valid(board, number, position):
    # number = 1, 10
    # position = row or column location

    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


print("1: Easy, 2: Medium, 3: Hard, 4: Expert: ")
difficulty = int(input("Select difficulty: "))

if difficulty == 1:
    print("Easy Difficulty: ")
    grid = easy
elif difficulty == 2:
    print("Medium Difficulty: ")
    grid = medium
elif difficulty == 3:
    print("Hard Difficulty: ")
    grid = hard
elif difficulty == 4:
    print("Expert Difficulty: ")
    grid = expert
else:
    print("Try Again")

print(" ")
display_grid(grid)
print(" ")
solver(grid)
print("The solved board is:  ")
display_grid(grid)