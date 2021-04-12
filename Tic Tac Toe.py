from tkinter import *


def callback(l, k):
    global player
    if player == 'X':
        b[l][k].configure(text='X')
        player = 'O'
    else:
        b[l][k].configure(text='O')
        player = 'X'


root = Tk()

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
# Initialize the board
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

## Assume player 1 is X.
player = 'X'

mainloop()
