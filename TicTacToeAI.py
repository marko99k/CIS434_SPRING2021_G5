# Tic Tac Toe game aganist the computer (AI)
import random
choice = ''
playerLetterChoice = ''
computerLetterChoice = ''

def playerMove(gameBoard, playerLetter, move):
    gameBoard[move] = playerLetter

def playerschoice():
    global choice
    choice = input('heads or tails\n')
    print(choice)

def firstPlayer():
# Function: Randomly choose who goes first within the game
    global playerLetterChoice
    global computerLetterChoice
    if random.randint(0, 1) == 0:
        print('coin is heads!')
        check = 'heads'
    else:
        print('coin is tails!')
        check = 'tails'
    print(choice)
    if choice == check:
        choice1 = input('player or comp\n')
        if choice1 == 'player':
            playerLetterChoice = 'X'
            computerLetterChoice = 'O'
            return 'player'
        if choice1 == 'comp':
            playerLetterChoice = 'O'
            computerLetterChoice = 'X'
            return 'computer'
    else:
        if random.randint(0, 1) == 0:
            print('computer chooses player')
            playerLetterChoice = 'X'
            computerLetterChoice = 'O'
            return 'player'
        else:
            print('computer chooses computer')
            playerLetterChoice = 'O'
            computerLetterChoice = 'X'
            return 'computer'

def freeSpace(gameBoard, move):
# Function: Is true if it is a valid game

    return gameBoard[move] == ' '

def creategameBoard(gameBoard):
# Function: The game board is created and printed to the screen.

    print('   |   |')
    print(' ' + gameBoard[7] + ' | ' + gameBoard[8] + ' | ' + gameBoard[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameBoard[4] + ' | ' + gameBoard[5] + ' | ' + gameBoard[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + gameBoard[1] + ' | ' + gameBoard[2] + ' | ' + gameBoard[3])
    print('   |   |')

def gameWinner(board, letter):
# Function: Returns true if the player is the winner,checks the various parts of the board

    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

def rematchGame():
# Function: True for rematch, False if not. Player's choice.

     print('Do you want a rematch? (yes or no)')
     return input().lower().startswith('y')

def gameMove(gameBoard):
# Function: Allows player to select their

    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(gameBoard, int(move)):
        print('Please select your next game move? (1-9)')
        move = input()
    return int(move)

def gameBoardDuplicate(gameBoard):
# Function:Duplicates and returns the game board

    duplicateBoard = []

    for i in gameBoard:
        duplicateBoard.append(i)
    return duplicateBoard

def randomMove(gameBoard, moveOptions):
#Function: Returns a valid game board , also returns nothing if it is invalid

    moveChoice = []
    for i in moveOptions:

        if freeSpace(gameBoard, i):
          moveChoice.append(i)

    if len(moveChoice) != 0:
        return random.choice(moveChoice)
    else:
        return None

def computerSelection(gameBoard, computerLetterChoice):
# Function: Returns the appropriate  for the game board

    if computerLetterChoice == 'X':
        playerplayerLetter = 'O'

    else:
        playerplayerLetter = 'X'

# Tic-Tac-Toe algorithm for the computer's /to determine win

    for i in range(1, 10):
        replica = gameBoardDuplicate(gameBoard)

        if freeSpace(replica, i):
             playerMove(replica, computerLetterChoice, i)

             if gameWinner(replica, computerLetterChoice):
                return i

    for i in range(1, 10):
        replica = gameBoardDuplicate(gameBoard)

        if freeSpace(replica, i):
            playerMove(replica, playerplayerLetter, i)

            if gameWinner(replica, playerplayerLetter):
                return i

 # Selects free corners if available
    move = randomMove(gameBoard, [1, 3, 7, 9])
    if move != None:
        return move

#Selects center if it is available
    if freeSpace(gameBoard, 5):
        return 5

#Selects one of the sides if it is available
    return randomMove(gameBoard, [2, 4, 6, 8])

def gameBoardComplete(gameBoard):
#Function is true if every game board space is occupied, false if otherwise
    for i in range(1, 10):
        if freeSpace(gameBoard, i):
            return False
    return True
print('Tic-Tac-Toe against the Computer: Welcome to the game!')

#The gameboard is cleared/ restarted
while True:

    tBoard = [' '] * 10
    playerschoice()
    turn = firstPlayer()
    print(turn + ' will go first.')

    activeGame = True
# Player’s 
    while activeGame:
       if turn == 'player':

           creategameBoard(tBoard)

           move = gameMove(tBoard)

           playerMove(tBoard, playerLetterChoice, move)

           if gameWinner(tBoard, playerLetterChoice):
              creategameBoard(tBoard)
              print('Congrats! You are the winner!')

              activeGame = False

           else:
               if gameBoardComplete(tBoard):
                    creategameBoard(tBoard)
                    print('Tied Game!')
                    break

               else:
                  turn = 'computer'
       else:
#Computer's
             move = computerSelection(tBoard, computerLetterChoice)

             playerMove(tBoard, computerLetterChoice, move)
#Computer wins the game:
             if gameWinner(tBoard, computerLetterChoice):
                 creategameBoard(tBoard)
                 print('The computer is the winner! You have lost the gameaaa!')
                 activeGame = False

             else:
# The game is tied:
                 if gameBoardComplete(tBoard):
                     creategameBoard(tBoard)
                     print('The game is a tie!')
                     break
                 else:
                     turn = 'player'
#If no rematch is chosen:
    if not rematchGame():  break