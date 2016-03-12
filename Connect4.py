def checkRedWinner(board, row, col):
    hWin = False
    vWin = False
    diagWin = False
    for i in range(1,4):
        if (col+3 < 7 and board[row][col+i] == 'R'):
            hWin = True
        else:
            hWin = False
            break
    if (hWin):
        #print "hWin1 at ", row, col
        return True
    #####
    hWin = False
    for i in range(1,4):
        if (col-3 >= 0 and board[row][col-i] == 'R'):
            hWin = True
        else:
            hWin = False
            break
    if (hWin):
        #print "hWin2 at ", row, col
        return True
###########################################
    for i in range(1,4):
        if (row+3 < 7 and board[row+i][col] == 'R'):
            vWin = True
        else:
            vWin = False
            break
    if (vWin):
        #print "vWin1 at ", row, col
        return True
    ######
    vWin = False
    for i in range(1,4):
        if (row-3 >= 0 and board[row-i][col] == 'R'):
            vWin = True
        else:
            vWin = False
            break
    if (vWin):
        #print "vWin2 at ", row, col
        return True
###########################################
    for i in range(1,4):
        if (row+3 < 7 and col+3 < 6 and board[row+i][col+i] == 'R'):
            diagWin = True
        else:
            diagWin = False
            break
    if (diagWin):
        return True
    ########
    diagWin = False
    for i in range(1,4):
        if (row+3 < 7 and col-3 >= 0 and board[row+i][col-i] == 'R'):
            diagWin = True
        else:
            diagWin = False
            break
    if (diagWin):
        return True
    ########
    diagWin = False
    for i in range(1,4):
        if (row == 5 and col == 3):
            pass#print row -4 > 0, col-4 > 0
            #print board[row-i][col-i]
        if (row-3 > 0 and col-3 >= 0 and board[row-i][col-i] == 'R'):
            diagWin = True
        else:
            diagWin = False
            break
    if (diagWin):
        return True
    ########
    diagWin = False
    for i in range(1,4):
        if (row-3 >= 0 and col+3 < 6 and board[row-i][col+i] == 'R'):
            diagWin = True
        else:
            diagWin = False
            break
    if (diagWin):
        return True


    return False


board = []
for row in range(6):
    inputt = raw_input()
    line = []
    for x in inputt.split(","):
        line.append(x)
    board.append(line)
for row in range(6):
    for col in range(7):
        if (board[row][col] == '0' and checkRedWinner(board, row, col)):
            print "(" + str(row+1) + "," + str(col+1) + ")"