import sys


#Creating the Vectors of the(First & Second) Players

# Here is the First Player Pits in the Tuple Form
First_Player_Pits = ('M', 'N', 'O', 'P', 'Q', 'R')

# Here is the Secong Player Pits in the Tuple Form
Second_Player_Pits = ('U', 'V', 'W', 'X', 'Y', 'Z')

#Creating Some Important Dictionaries & Variables with Values

# Here we are Creating the Corresponding Pit Dictionary
Corresponding_Pit = {'M': 'U', 'N': 'V', 'O': 'W', 'P': 'X', 'Q': 'Y', 'R': 'Z', 'U': 'M', 'V': 'N', 'W': 'O', 'X': 'P',
                     'Y': 'Q', 'R': 'Z'}

# Here we are Creating the get Next Pit Dictionary
Next_Pit = {'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': '1', '1': 'Z', 'Z': 'Y', 'Y': 'X', 'X': 'W',
            'W': 'V', 'V': 'U', 'U': '2', '2': 'M'}

# Mancala Game

# Assign the Value of the Pit
def initalizePit():
    return {'1': 0, '2': 0, 'M': 4, 'N': 4, 'O': 4, 'P': 4, 'Q': 4, 'R': 4, 'U': 4, 'V': 4, 'W': 4, 'X': 4, 'Y': 4,
            'Z': 4}


# Define the Priority of First Player
def definePriorityPlayer1(data):
    if data == 1:
        data = 'M'
    elif data == 2:
        data = 'N'
    elif data == 3:
        data = 'O'
    elif data == 4:
        data = 'P'
    elif data == 5:
        data = 'Q'
    elif data == 6:
        data = 'R'
    elif data == -1:
        data = -1
    else:
        data = -2
    return data


# Define the Priority of Second Player
def definePriorityPlayer2(data):
    if data == 1:
        data = 'U'
    elif data == 2:
        data = 'V'
    elif data == 3:
        data = 'W'
    elif data == 4:
        data = 'X'
    elif data == 5:
        data = 'Y'
    elif data == 6:
        data = 'Z'
    elif data == -1:
        data = -1

    else:
        data = -2
    return data



# Display the Results of the Mancala Game Pit
def displayResults(mancalaBoard):
    Results = []
    for pit in 'UVWXYZ21MNOPQR':
        data = str(mancalaBoard[pit]).rjust(2)
        Results.append(data.strip())

    # Display the Results with the Help of Results List
    print(Results[7])
    data = [print(Results[x], end=' ') for x in [8, 9, 10, 11, 12, 13]]
    print('\n')
    print(Results[6])
    data = [print(Results[x], end=' ') for x in [0, 1, 2, 3, 4, 5]]
    print('\n')



# Get the Move from Player Input
def getPlayerMove(playerTurn, mancalaBoard):
    while True:
        if playerTurn == '1':
            print('First Player Move : 1-6 (-1 QUIT) : ')
            response = int(input('Please Enter Your Move==>'))
            response = definePriorityPlayer1(response)

            if response == -1:
                print('Thanks For Playing!')
                sys.exit()
            elif response == -2:
                print('Please Select Correct Number!')
                continue

            return response

        elif playerTurn == '2':
            print('Second Player Move : 1-6 (-1 QUIT) : ')
            response = int(input('Please Enter Your Move==>'))
            response = definePriorityPlayer2(response)

            if response == -1:
                print('Thanks For Playing!')
                sys.exit()
            elif response == -2:
                print('Please Select Correct Number!')
                continue

            return response
        return response




# Print the Next Move of the Player (mancalaBoard hold the (Player 1 & Player 2 Integer Values like a Vectors))
def printNextMove(mancalaBoard, turnOfPlayer, pitRes):
    # Get the Data of that Pit
    pitData = mancalaBoard[pitRes]
    # Set taht pit with zero
    mancalaBoard[pitRes] = 0

    while pitData > 0:
        # Get the Pit with the help of Next_Pit
        pitRes = Next_Pit[pitRes]
        if (turnOfPlayer == '1' and pitRes == '2') or (turnOfPlayer == '2' and pitRes == '1'):
            continue
        # Add the Pit Data in the Game Board
        mancalaBoard[pitRes] += 1
        # Subtract the pit Data
        pitData -= 1

    # Check the Which Player Turn than Add the Data into the Mancala Game
    if (pitRes == turnOfPlayer == '1') or (pitRes == turnOfPlayer == '2'):
        return turnOfPlayer
    if turnOfPlayer == '1' and pitRes in First_Player_Pits and mancalaBoard[pitRes] == 1:
        correspondPit = Corresponding_Pit[pitRes]
        mancalaBoard['1'] += mancalaBoard[correspondPit]
        mancalaBoard[correspondPit] = 0
    elif turnOfPlayer == '2' and pitRes in Second_Player_Pits and mancalaBoard[pitRes] == 1:
        correspondPit = Corresponding_Pit[pitRes]
        mancalaBoard['2'] += mancalaBoard[correspondPit]
        mancalaBoard[correspondPit] = 0
    if turnOfPlayer == '1':
        return '2'
    elif turnOfPlayer == '2':
        return '1'



# Check which Player Won
def mancalaGameWinner(mancalaBoard):
    # Total sum of the First Player Pits
    firstPlayerSum = mancalaBoard['M'] + mancalaBoard['N'] + mancalaBoard['O'] + mancalaBoard['P'] + mancalaBoard['Q'] + \
                     mancalaBoard['R']

    # Total Sum of the Second Player Pits
    secondPlayerSum = mancalaBoard['U'] + mancalaBoard['V'] + mancalaBoard['W'] + mancalaBoard['X'] + mancalaBoard[
        'Y'] + mancalaBoard['Z']

    # Find out the which Player Win
    if firstPlayerSum == 0:
        mancalaBoard['2'] += secondPlayerSum
        for pit in Second_Player_Pits:
            mancalaBoard[pit] = 0
    elif secondPlayerSum == 0:
        mancalaBoard['1'] += firstPlayerSum
        for pit in First_Player_Pits:
            mancalaBoard[pit] = 0
    else:
        return 'no winner'

    # Declare the which Player Win
    if mancalaBoard['1'] > mancalaBoard['2']:
        num = '1'
        return num
    elif mancalaBoard['2'] > mancalaBoard['1']:
        num = '2'
        return num
    else:
        num = 'tie'
        return num



def mancalaGame():
    input('If you Start the Game, Press Enter Begin...')

    # Initial The Pit with Default Values\
    mancalaBoard = initalizePit()




    # Start Game with First Player
    playerTurn = '1'
    while True:
        # Display the Results
        displayResults(mancalaBoard)
        # Selcct the Move from Input
        movePlayer = getPlayerMove(playerTurn, mancalaBoard)
        # Print the Next Move of the Player
        playerTurn = printNextMove(mancalaBoard, playerTurn, movePlayer)  # Mancala Board Player 1 & Player 2 Values
        # Check the Winner After End the Game
        playerWinner = mancalaGameWinner(mancalaBoard)

        # Check which Player Win
        if playerWinner == '1' or playerWinner == '2':
            displayResults(mancalaBoard)
            print('That Player {} has won!'.format(playerWinner))
            sys.exit()
        elif playerWinner == 'tie':
            displayResults(mancalaBoard)
            print('That is a Tie!')
            sys.exit()

        print('\n' * 2)

if __name__ == '__main__':
    mancalaGame()