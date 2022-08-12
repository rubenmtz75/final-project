import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0
board = [[" " for x in range(3)] for y in range(3)]   # Creates an empty board to begin


# Defines the rules of gameplay to decide the winner
def winner(one, two):
    return ((one[0][0] == two and one[0][1] == two and one[0][2] == two) or
            (one[1][0] == two and one[1][1] == two and one[1][2] == two) or
            (one[2][0] == two and one[2][1] == two and one[2][2] == two) or
            (one[0][0] == two and one[1][0] == two and one[2][0] == two) or
            (one[0][1] == two and one[1][1] == two and one[2][1] == two) or
            (one[0][2] == two and one[1][2] == two and one[2][2] == two) or
            (one[0][0] == two and one[1][1] == two and one[2][2] == two) or
            (one[0][2] == two and one[1][1] == two and one[2][0] == two))


# Checks when board is full, to know game is over
def isfull():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


# Brains and calculated next move for computer
def pc():
    next = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                next.append([i, j])
    if next == []:
        return
    else:
        for let in ['O', 'X']:
            for i in next:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in next:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in next:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]


# Text on buttons pushed in game
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        messagebox.showinfo("Winner", "You're good!")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        messagebox.showinfo("Loser", "A.I. showed you!")
    elif isfull():
        gb.destroy()
        x = False
        messagebox.showinfo("  ", "Tie Game!")
    if x:
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


# tkinter gui outline
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Start the game board for play
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Ruben Martinez final")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)


# Main function
def main():
    menu = Tk()
    menu.geometry("250x135")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)

    head = Button(menu, text="Tic Tac Toe!",
                  activebackground="yellow", bg="blue",
                  fg="yellow", width=500, font='summer', bd=5)

    b1 = Button(menu, text="Click to Play!", command=wpc,
                activeforeground='red',
                activebackground="purple", bg="blue",
                fg="black", width=500, font='summer', bd=5)

    b2 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="gray", fg="black",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    b1.pack(side='top')
    b2.pack(side='top')
    menu.mainloop()


if __name__ == '__main__':
    main()
