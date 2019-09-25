#!/usr/bin/env python
# ---------------------------------------------------------------------
# Tic-Tac-Toe game in Python
# Author: Reza Adle
# Date: 03-09-2015
# Tested with Python 2.7.10
# ---------------------------------------------------------------------

import random
import sys
import os

def game_rules():
    os.system("clear")
    print (""" 
      Welcome to the Game of Tic-Tac-Toe...
      You will make your move by entering a number between 1 to 9
      The numbers correspond to the board position as shown below:

                             1 | 2 | 3            
                            -----------
                             4 | 5 | 6            
                            -----------
                             7 | 8 | 9

      If you want to exit or play new game, please type (q or Q).
      The game is about to begin... may the chance be with you!
      """)


def game_setup():
    human = raw_input("\nWhich player you want to be? (X or O)\n")
    while human not in ('x','X','o','O'):
        print "Invalid choice! Please try again."
        human = raw_input("Which player you want to be? (X or O)\n")
    
    human = human.upper()
    if human == 'X':
        machine = 'O'
    else:
        machine = 'X'

    print "Ok, %s is yours. Let's see who will play first..." % human
    draw_board(range(1,10))
    
    # randomly decide who will play first
    turn = random.choice([True, False])
    if turn:
        print "I play first!\n"
    else: 
        print "You play first!\n"

    return human, machine, turn
    

def draw_board(values):
    print "\n\t", values[0], "|", values[1], "|", values[2]
    print " " * 6, "-" * 11
    print "\t", values[3], "|", values[4], "|", values[5]
    print " " * 6, "-" * 11
    print "\t", values[6], "|", values[7], "|", values[8], "\n"


def win_conditions(human, machine, values):
    # wins list contain all the winning conditions to check
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for v in wins:
        if values[v[0]] == values[v[1]] == values[v[2]] != ' ':
            winner = values[v[0]]
            if winner == human:
                return 'H'
            elif winner == machine:
                return 'M'
    
    if ' ' not in values: 
        return 'T'  # Tie game


def human_move(values): 
    # get the human input for next move
    c = raw_input("What is your move? ")
    while c != 'q' and c != 'Q':
        if c not in ('1','2','3','4','5','6','7','8','9'):
            print "Sorry, invalid choice!"
            c = raw_input("Please try again? ")
        elif values[(int(c) - 1)] != " ":
            print "Sorry, this spot is already taken!"
            c = raw_input("Please try another position? ")
        else:
            return (int(c) - 1)

    # if player quit, ask if she/he wants to play a new game
    play_again()
            

def machine_move(human, machine, values):
    best_move = [0, 2, 4, 6, 8]
    empty_places = []
    best_move_left = []
    
    # create the list of possible moves 
    for i in range(0,9):
        if values[i] == " ":
            empty_places.append(i)
    
    # check if computer can win with a choice for next move
    for p in empty_places:
        values[p] = machine
        if win_conditions(human, machine, values) == "M":
            return p
        values[p] = " "

    # check if human can win with the next move to block it 
    for p in empty_places:
        values[p] = human
        if win_conditions(human, machine, values) == "H":
            return p
        values[p] = " "

    # try one of the best move left to increase odds of winning
    for m in best_move:
        if m in empty_places:
            best_move_left.append(m)      
    if len(best_move_left) != 0:
        return best_move_left[random.randrange(len(best_move_left))]

    # if none of the above possibilities, pick a random spot left
    return empty_places[random.randrange(len(empty_places))]


def play(human, machine, turn, values): 
    while win_conditions(human, machine, values) == None:
        # check & change "turn" variable to see whose turn is to move
        if turn:
            m_move = machine_move(human, machine, values)
            print "Here is my choice:", (m_move + 1)
            values[m_move] = machine        
        else:
            h_move = human_move(values)
            values[h_move] = human
        
        draw_board(values)
        turn = not turn
    
    return win_conditions(human, machine, values)


def play_again():
    # play a new game or exit
    print "\nIf you want to play a new game, please type (r or R)."
    c = raw_input("Otherwise, please press enter to exit: ")
    if c == 'r' or c == 'R':
        main() 
    else:
        print "Thanks for playing. Bye..."
        sys.exit(0)

    
def main():
    # setup human & computer markers and order of playing
    players = game_setup()
    human = players[0]
    machine = players[1]
    turn = players[2]
    values = [' '] * 9
    
    # check who won the game
    state = play(human, machine, turn, values)
    if state == "H":
        print "You won this game. Congratulations!"
    elif state == "M":
        print "I won this game!!!"
    else:
        print "It's a Tie game."
    
    # ask player if she/he wants to play a new game
    play_again()


if __name__ == '__main__':
    game_rules()
    main()