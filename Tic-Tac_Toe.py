#The aim of this project is to create a Tic-Tac-Toe Game.
#As I go along, I'll be modifying my code & leaving my rookie mistakes as a trail, in order to see the difference.

#Define the space/limits of the 3x3 cube or game board.
#To do this you need to create a list & it's set out this way for easy "readability", in the words of
#Bennett Garner - https://bennettgarner.medium.com/tic-tac-toe-series-starting-small-with-python-86e2f49db797
#Using this as a guide!

#Initially, I had one list --> game_board = [ [ "_" , "_" , "x", ] ,
#                                             [ "_" ,  "x", "o", ] ,
#                                             [ "x" ,  "_" , "o" ]
#                                           ]

#Then, I changed it to the following in order to print each line/row of the cube separately.

#               game_board_1 = [ "_" , "_" , "x", ]
#               game_board_2 = [ "_" ,  "x", "o", ]
#               game_board_3 = [ "x" ,  "_" , "o" ]

#               print(game_board_1)
#               print(game_board_2)
#               print(game_board_3)

#However, for reuse purposes (ref. Garner), it's better to use a function and wrap the for loop inside of that!

game_board = [ [ "_" , "_" , "x", ] ,
               [ "_" ,  "x", "o", ] ,
               [ "x" ,  "_" , "o" ]
             ]

def print_gboard(game_board):
    for line in game_board:
        print(line)

print_gboard(game_board)

#Making our game board become all blank spaces. Utilizing LIST COMPREHENSION HERE!
# This _ is a throwaway or blank value, in which you don't have to specify the parameter.
# For example, you would normally put for i in; or for x in blah blah blah in the _ spot.
# [["blank" for "blank" in range(3)] for "blank" in range(3)] - because they are 3 spaces
# in EACH of the 3 rows of the list!

game_board = [["_" for _ in range(3)] for _ in range(3)]


