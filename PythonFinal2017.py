import random
"""Make a tictactoe game using python."""

def put_mark(index, mark, board):
    """stuff

    >>> board = ['', '', '', '', '', '', '', '', '']
    >>> put_mark(1, 'x', board)
    ['', '', '', '', '', '', '', '', '']
    
    """
    board[index] = mark
    return board




##VL = victorylist = [(1,2,3),(4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
##
##open_slot = ''


def show_board(board):
    return """ {0} | {1} | {2}""".format(*board)



def turn_choice():
    turn = None

    while turn not in ("Yes", "yes", "No", "no", 'first', 'second'):
        human = raw_input("Do you wanna go first?")
        if human in ("Yes", "yes"):
            turn = 'first'
        elif human in ("No", "no"):
            turn = 'second'
        else:
            print ("Pick Yes or No, please.")
    return turn



def draw(a):
    
    print "\n\t",a[0]," |",a[1],"|",a[2]
    print "\t", "--------"
    print "\n\t",a[3]," |",a[4],"|",a[5]
    print "\t", "--------"
    print "\n\t",a[6]," |",a[7],"|",a[8], "\n"





def human_move(board, symbol):
    slot = None
    while slot != 'done':
        slot = int(raw_input("Your turn. Please pick a slot"))
        
        if not 1 <= slot <= 9:
            print ("Not a place on the board")
        else:
            if board[slot-1] != '':
                print ("The spot is already taken.")
            else:
                board[slot-1] = symbol
                slot = 'done'   
    return board

def computer_move(board, symbol):
    print("My turn. I pick...")
    open_slots = []
    choice = bestmoves(board)
##    for index, item in enumerate(board):
##        if item == '':
##            open_slots.append(index)
##    choice = random.choice(open_slots)
    return put_mark(choice, symbol, board)

def bestmoves(board):
    bestmoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for move in bestmoves:
        if board[move] == '':
            return move

def checkline(symbol, slot1, slot2, slot3):
    if board[slot1] == symbol and board[slot2] == symbol and board[slot3] == symbol:
        return True

def checkvictory(symbol):
     if checkline(symbol, 0,1,2):
        return True
     if checkline(symbol, 3,4,5):
        return True
     if checkline(symbol, 6,7,8):
        return True
     if checkline(symbol, 0,4,8):
        return True
     if checkline(symbol, 2,4,6):
        return True
     if checkline(symbol, 0,3,6):
        return True
     if checkline(symbol, 1,4,7):
        return True
     if checkline(symbol,2,5,8):
        return True




    
## main
board = ['', '', '', '', '', '', '', '', '']
slots = ['1', '2', '3', '4', '5', '6' , '7', '8', '9']
##mylist = put_mark(1, 'x', mylist)

## Game Loop
choice = None
while choice != 'q':
    human = None
    while human not in ('X', 'x', 'O', 'o'):
        human = raw_input("Choose team, X's or O's: ").upper()
        if human in ('X', 'x'):
            print("Cool. Computer will be Os")
            computer = 'O'
        elif human in ('O', 'o'):
            print("Alight, Computer will be Xs")
            computer = 'X'
        else:
            print("Xs or Os my dude")
    turn = turn_choice()
    print("You do your moves by giving the slot number you want.")
    print("Here are the slots!")
    draw(slots)
    draw(board)

    turns = 0
    while turns != 9:
        print(board)
        turns += 1
        print("Turn number: {}".format(turns))
        if turn == "first":     
            board = human_move(board, human)
            turn = 'second'
            if checkvictory(human):
                
                print "Humanity wins!"
                draw(board)
                break;
        else:
            board = computer_move(board, computer)
            if checkvictory(computer):
                
                print "The Machines have won!"
                draw(board)
                break;
            turn = 'first'
        print("Here's the board now!")
      
        draw(board)
##    winner(board, slots, open_slot)
    choice = raw_input("Do you want to quit? ")
    print("You chose {}".format(choice))


## Game Play


                
                
                
               
        
        





    
