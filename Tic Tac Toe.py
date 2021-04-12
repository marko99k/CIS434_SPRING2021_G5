from tkinter import *


def callback(j, k):
    global player
    if player == 'X':
        b[j][k].configure(text='X')
        player = 'O'
    else:
        b[j][k].configure(text='O')
        player = 'X'


root = Tk()

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# initializing the board:
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='white',
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

player = 'X'

mainloop()
