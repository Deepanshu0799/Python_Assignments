#TIC_TAC_TOE#

import random

def game(space):
    print('   |   |')
    print(' ' + space[7] + ' | ' + space[8] + ' | ' + space[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[4] + ' | ' + space[5] + ' | ' + space[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[1] + ' | ' + space[2] + ' | ' + space[3])

def choose_one():
    choice = ''
    while not (choice == 'X' or choice == 'O'):
        print('Choose either X or O?')
        choice = input().upper()
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def first_Move():
    if random.randint(0, 1) == 0:
        return 'SYSTEM'
    else:
        return 'PLAYER'

def playAgain():
    print('Do you want to play again? Give yes or no ')
    return input().lower().startswith('y')

def makeMove(space, choice, move):
    space[move] = choice


def winner(hit, miss):
    return ((hit[7] == miss and hit[8] == miss and hit[9] == miss) or 
    (hit[4] == miss and hit[5] == miss and hit[6] == miss) or 
    (hit[1] == miss and hit[2] == miss and hit[3] == miss) or 
    (hit[7] == miss and hit[4] == miss and hit[1] == miss) or 
    (hit[8] == miss and hit[5] == miss and hit[2] == miss) or 
    (hit[9] == miss and hit[6] == miss and hit[3] == miss) or 
    (hit[7] == miss and hit[5] == miss and hit[3] == miss) or 
    (hit[9] == miss and hit[5] == miss and hit[1] == miss))


def structure(space):
    showB = []
    for i in space:
        showB.append(i)
    return showB


def freeSpace(space, move):
    return space[move] == ' '


def movePlayer(space):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(space, int(move)):
        print('Make your move while choosing from 1-9')
        move = input()
    return int(move)

def chooseRandom(space, movesPresent):
    possibleMoves = []
    for i in movesPresent:
        if freeSpace(space, i):
            possibleMoves.append(i)
        
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def systemRandom(space, movesSystem):
    if movesSystem == 'X':
        movesPlayer = 'O'
    else:
        movesPlayer = 'X'

    for i in range(1, 10):
        copy = structure(space)
        if freeSpace(copy, i):
            makeMove(copy, movesSystem, i)
            if winner(copy, movesSystem):
                return i

    for i in range(1, 10):
        copy = structure(space)
        if freeSpace(copy, i):
            makeMove(copy, movesPlayer, i)
            if winner(copy, movesPlayer):
                return i
    
    move = chooseRandom(space, [1, 3, 7, 9])
    if move != None:
        return move
    if freeSpace(space, 5):
        return 5
    return chooseRandom(space, [2, 4, 6, 8])


def isBoardFull(space):
    for i in range(1, 10):
        if freeSpace(space, i):
            return False
        return True
print('Lets play a game of Tic Tac Toe ')

while True:
    theBoard = [' '] * 10
    movesPlayer, movesSystem = choose_one()
    turn = first_Move()
    print('The ' + turn + ' will make move and go first.')
    playing = True

    while playing:
        if turn == 'PLAYER':
            game(theBoard)
            move= movePlayer(theBoard)
            makeMove(theBoard, movesPlayer, move)

            if winner(theBoard, movesPlayer):
                game(theBoard)
                print('Awesome! You have beaten system in the game!')
                playing = False
            else:
                if isBoardFull(theBoard):
                    game(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'SYSTEM'
        else:
            move = systemRandom(theBoard, movesSystem)
            makeMove(theBoard, movesSystem, move)
            if winner(theBoard, movesSystem):
                game(theBoard)
                print('The SYSTEM has beaten you! You lose.')
                playing = False
            else:
                if isBoardFull(theBoard):
                    game(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'PLAYER'

    if not playAgain():
        break