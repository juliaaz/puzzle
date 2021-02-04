Puzzle

Puzzle is a program for working with board 9x9.
This program checks whether the puzzle board is ready to start the game.
--------------------------------------------------------------------------------------------------------------------------------------

Functions of the program

Module includes 4 different functions: 
1. first_rule |Function checks whether the colored cells
of each line contain numbers from 1 to 9 without repetition.|

2. second_rule |Function checks whether the colored cells
of each column contain the numbers 1 to 9 without repetition.|

3. third_rule |Function checks whether each block of cells
of the same color contain numbers from 1 to 9 without repetition.|

4. validate_board

The last one is a main one and returns a Boolean value depending on compliance with the rules of previous functions. The others are for working with given data.