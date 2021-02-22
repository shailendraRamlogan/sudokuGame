def solve(bo):
    search = emptyPosition(bo)
    if not search:
        return True
    else:
        row, col = search

    for i in range(1,10):
        if isValid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def isValid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range (len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def outputBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def emptyPosition(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)
    return None

