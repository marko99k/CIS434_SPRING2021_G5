from tkinter import *
from functools import *
from tkinter import messagebox


def game():
    """Main Menu function for Tic-Tac-Toe in Tkinter"""
    menu = Tk()
    menu.geometry("350x350")
    menu.title("Tic Tac Toe")
    aPC = partial(PvP, menu)  # Player against PC function needs to be added
    aPL = partial(againstPC, menu)  # Player against Player function needs to be added

    # Label without functionality
    head = Label(menu, text="Main Menu", bg="white",
                 fg="Black", width=500, font=('summer', 12, 'bold'), bd=5)

    B1 = Button(menu, text="Single Player", command=aPC,
                activeforeground='White',
                activebackground="blue", bg="white",
                fg="Black", width=500, font='summer', bd=5)

    # command has to be update with the Player Vs Player function
    B2 = Button(menu, text="Multi Player", command=aPL, activeforeground='White',
                activebackground="blue", bg="white", fg="Black",
                width=500, font='summer', bd=5)

    # command has to be updated with the againstPC function
    B3 = Button(menu, text="Exit", command=ExitApplication, activeforeground='White',
                activebackground="blue", bg="white", fg="Black",
                width=500, font='summer', bd=5)

    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


def gameWinner(board, letter):
    """Function: Returns true if the player is the winner,checks the various parts of the board"""
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def tText(k, j, bgame, layer1, layer2):
    """Initializing text per click"""
    global symbol
    if board[k][j] == ' ':
        if symbol % 2 == 0:
            # layer1/2 config is changing the appearance in style
            # so squares have to change to X/O depending on the input/move
            layer1.config(state=DISABLED)
            layer2.config(state=ACTIVE)
            board[k][j] = "X"
        else:
            # layer1/2 config is changing the appearance in style
            # so squares have to change to X/O depending on the input/move
            layer2.config(state=DISABLED)
            layer1.config(state=ACTIVE)
            board[k][j] = "O"
        symbol += 1
        gameWinner[k][j].config(text=board[k][j])
    # if X is the winner, destroy the board, can implement message to state the winner.
    if gameWinner(board, "X"):
        bgame.destroy()
    # if O is the winner, destroy the board, can implement message to state the winner.
    elif gameWinner(board, "O"):
        bgame.destroy()
    # if it's a TIE, destroy the board, can implement message to state the Tie message.
    elif freeSpace():
        bgame.destroy()


def freeSpace():
    """Check if the board is full"""
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


global board
"""Initialize the board"""
board = [[" " for x in range(3)]
         for y in range(3)]


def ExitApplication():
    """Exit button function"""
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        quit()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def playBoard(game_board, layer1, layer2):
    """Function to create 3x3 board in
    Tkinter gui"""
    global button
    # Dictionary list to store the molve
    button = []
    for k in range(3):
        m = 3 + k
        button.append(k)
        button[k] = []
        for j in range(3):
            n = j
            button[k].append(j)
            get_t = partial(tText, k, j, game_board, layer1, layer2)
            button[k][j] = Button(game_board, bd=5, command=get_t,
                                  height=4, width=8)
            button[k][j].grid(row=m, column=n)
    game_board.mainloop()


def PvP(game_board):
    """Function Player vs Player which creates board
    in Tkinter and once the game is complete, destroys it"""
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    layer1 = Label(game_board, text="Player 1", width=10)
    layer1.grid(row=1, column=1)

    layer2 = Label(game_board, text="Player 2",
                   width=10, state=DISABLED)
    layer2.grid(row=2, column=1)
    playBoard(game_board, layer1, layer2)


def againstPC(game_board):
    """Function Player vs Computer which creates board
    in Tkinter and once the game is complete, destroys it"""
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    layer1 = Label(game_board, text="Player", width=10)
    layer1.grid(row=1, column=1)

    layer2 = Label(game_board, text="Computer",
                   width=10, state=DISABLED)
    layer2.grid(row=2, column=1)
    playBoard(game_board, layer1, layer2)


# Main function
if __name__ == '__main__':
    game()

# below can be ignore since I already implemented the board in the Tkinter
# def callback(l, k):
#    global player
#    if player == 'X':
#        b[l][k].configure(text='X')
#        player = 'O'
#    else:
#        b[l][k].configure(text='O')
#        player = 'X'


# b = [[0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]]

# root = Tk()
# root.title("Tic Tac Toe")

# Initialize the board
# global board
# """Creates global board"""
# for i in range(3):
#    for j in range(3):
#        b[i][j] = Button(font=('Verdana', 56), width=3, bg='white',
#                         command=lambda r=i, c=j: callback(r, c))
#        b[i][j].grid(row=i, column=j)

## Assume player 1 is X.
# player = 'X'
