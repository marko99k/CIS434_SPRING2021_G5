from tkinter import *
from functools import *
from tkinter import messagebox


def game():
    """Main Menu function for Tic-Tac-Toe in Tkinter"""
    menu = Tk()
    menu.geometry("350x350")
    menu.title("Tic Tac Toe")
    # aPC = partial(callback, menu) ## Player against PC function needs to be added
    # aPL = partial(againstPlayer, menu) ## Player against Player function needs to be added

    # Label without functionality
    head = Label(menu, text="Main Menu", bg="white",
                 fg="Black", width=500, font=('summer', 12, 'bold'), bd=5)

    B1 = Button(menu, text="Single Player", command=menu.quit,
                activeforeground='White',
                activebackground="blue", bg="white",
                fg="Black", width=500, font='summer', bd=5)

    # command has to be update with the Player Vs Player function
    B2 = Button(menu, text="Multi Player", command=menu.quit, activeforeground='White',
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


def ExitApplication():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        quit()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


def callback(l, k):
    global player
    if player == 'X':
        b[l][k].configure(text='X')
        player = 'O'
    else:
        b[l][k].configure(text='O')
        player = 'X'


b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

root = Tk()
root.title("Tic Tac Toe")

# Initialize the board
# global board
# """Creates global board"""
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='white',
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

## Assume player 1 is X.
player = 'X'

if __name__ == '__main__':
    game()
