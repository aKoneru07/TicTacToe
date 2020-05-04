### SIMPLE GAME AI FOR UNBEATABLE TIC-TAC-TOE
### Run to play a game

import time
import random

GAME = 0
states = set()
f = {"x" : max, "o":min}    #function
switchP = {"x" : "o", "o" : "x"}  #Switch player
win = {1 : "x is the WINNER", -1: "o is the WINNER", 0 : "IT IS A TIE"}

def score_test(board, player):
    units = [0, 4, 8, 2,4, 6, 0,3,6, 1,4,7, 2,5,8, 0,1,2, 3,4,5, 6,7,8]
    x = 0
    while x in range(len(units)-1):
        t = board[units[x]] + board[units[x+1]] + board[units[x+2]]
        if t == "xxx":
            return 1
        elif t == "ooo":
            return -1
        x+=3
    if not "." in board:
        return 0
    return 7        ###PLAY = 7###  "PLAY"

def recur(board, player):
    if not score_test(board, player) == 7:
        global GAME, states
        states.add(board)
        GAME+=1
        return
    for r in valid_moves(board,player):
        recur(r, switchP[player])

def make_move(board, player):
    r = (f[player]([minmax(r, switchP[player], r) for r in valid_moves(board, player)]))
    return r[2]

def valid_moves(board, player):     #RETURNS list of possible boards post-move
    l = []
    for x in range(9):
        if board[x] == ".":
            l.append(board[0:x] + player + board[x+1::])
    return l

def minmax(board, player, par):
    score = score_test(board,player)
    if not score == 7:
        return (score, random.random(), par)      #Returns (SCORE, random, board)
    return (f[player]([minmax(r, switchP[player], par) for r in valid_moves(board,player)]))

def hum_move(b, pos, ply):
    return (b[0:pos-1] + ply + b[pos::])

def display(board):
    num = "123456789"
    for x in range(0,9,3):
        print(board[x:x+3] + "  " + num[x:x+3])
    print("---  ---")

def check(move):
    if not move.isnumeric() or len(move) > 1:
        print("Please enter a single integer")
        print()
    elif move == "0":
        print("That position is not on the board")
        print()
    elif not b[int(move) - 1] == ".":
        print("That position is occupied")
        print()
    else:
        return True

b = "........."
ply = "x"
display(b)
count = 1
while score_test(b,ply) == 7:
    move = input("What is your move? (123456789)")
    if not (count == 1 and move == "no"):
        while not check(move) is True:
            move = input("What is your move? (123456789)")
        b = hum_move(b, int(move), ply)     #Human move
        ply = switchP[ply]
        print("Your move: ")
        display(b)
    if not score_test(b, ply) == 7:
        break
    tic = time.time()
    b = make_move(b, ply)
    #print("Time to decide move: ", time.time() - tic)
    ply = switchP[ply]
    print("Computer move: ")
    display(b)
    print()
    count+=1
print("GAME OVER")
print(win[score_test(b, ply)])