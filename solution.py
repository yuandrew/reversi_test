#!/usr/bin/python3

""" Example Reversi implementation that reads a JSON board and move from
    stdin and writes a JSON board to stdout. """

# Libs
import argparse
import json
import sys


def main():
    """ Naively returns the same board it was given """

    # Read input
    args = parse_arguments()
    begin_state = json.load(args.infile)

    #import pdb
    #pdb.set_trace()



    #begin_state[u'board'] to access board array
    #begin_state[u'move'][u'player'] to access board move, with options u'column', u'row', and u'player'

    # Naively copy the input board
    # TODO: Implement move and put the resulting board into end_state
    board_dim = 8
    player = begin_state[u'move'][u'player']
    row = begin_state[u'move'][u'row'] - 1
    column = begin_state[u'move'][u'column'] - 1

    #set move value to player piece
    begin_state[u'board'][row * 8 + column] = player
    #parse rest of board to see effect of move

    #below
    for i in range(row + 1, 8):
        if begin_state[u'board'][i * 8 + column] == player:
            #change pieces if needed
            for j in range(row + 1, 8):
                if begin_state[u'board'][j * 8 + column] == player:
                    break
                if begin_state[u'board'][j * 8 + column] != 0:
                    begin_state[u'board'][j * 8 + column] = player
                else:
                    break
            break

    #above
    for i in range(row - 1, -1, -1):
        if begin_state[u'board'][i * 8 + column] == player:
            # change pieces if needed
            for j in range(row - 1, -1, -1):
                if begin_state[u'board'][j * 8 + column] == player:
                    break
                if begin_state[u'board'][j * 8 + column] != 0:
                    begin_state[u'board'][j * 8 + column] = player
                else:
                    break
            break
    #right
    for i in range(column + 1, 8):
        if begin_state[u'board'][row * 8 + i] == player:
            #change pieces if needed
            for j in range(column + 1, 8):
                if begin_state[u'board'][row * 8 + j] == player:
                    break
                if begin_state[u'board'][row * 8 + j] != 0:
                    begin_state[u'board'][row * 8 + j] = player
                else:
                    break
            break

    #left
    for i in range(column - 1, -1, -1):
        if begin_state[u'board'][row * 8 + i] == player:
            #change pieces if needed
            for j in range(column - 1, -1, -1):
                if begin_state[u'board'][row * 8 + j] == player:
                    break
                if begin_state[u'board'][row * 8 + j] != 0:
                    begin_state[u'board'][row * 8 + j] = player
                else:
                    break
            break

    #diagonals


    #downright diagonal
    temp_col = column + 1
    temp_row = row + 1
    while temp_col < 8 and temp_row < 8:
        if begin_state[u'board'][temp_row * 8 + temp_col] == player:
            #change pieces if needed
            temp_col = column + 1
            temp_row = row + 1
            while temp_col < 8 and temp_row < 8:
                if begin_state[u'board'][temp_row * 8 + temp_col] == player:
                    break
                if begin_state[u'board'][temp_row * 8 + temp_col] != 0:
                    begin_state[u'board'][temp_row * 8 + temp_col] = player
                else:
                    break
                temp_col += 1
                temp_row += 1
            break
        temp_col += 1
        temp_row += 1
    #downleft diagonal
    temp_col = column - 1
    temp_row = row + 1
    while temp_col >= 0 and temp_row < 8:
        if begin_state[u'board'][temp_row * 8 + temp_col] == player:
            #change pieces if needed
            temp_col = column - 1
            temp_row = row + 1
            while temp_col >= 0 and temp_row < 8:
                if begin_state[u'board'][temp_row * 8 + temp_col] == player:
                    break
                if begin_state[u'board'][temp_row * 8 + temp_col] != 0:
                    begin_state[u'board'][temp_row * 8 + temp_col] = player
                else:
                    break
                temp_col -= 1
                temp_row += 1
            break
        temp_col -= 1
        temp_row += 1
    #upleft diagonal
    temp_col = column - 1
    temp_row = row - 1
    while temp_col >= 0 and temp_row >= 0:
        if begin_state[u'board'][temp_row * 8 + temp_col] == player:
            #change pieces if needed
            temp_col = column - 1
            temp_row = row - 1
            while temp_col >= 0 and temp_row >= 0:
                if begin_state[u'board'][temp_row * 8 + temp_col] == player:
                    break
                if begin_state[u'board'][temp_row * 8 + temp_col] != 0:
                    begin_state[u'board'][temp_row * 8 + temp_col] = player
                else:
                    break
                temp_col -= 1
                temp_row -= 1
            break
        temp_col -= 1
        temp_row -= 1
    #upright diagonal
    temp_col = column + 1
    temp_row = row - 1
    while temp_col < 8 and temp_row >= 0:
        if begin_state[u'board'][temp_row * 8 + temp_col] == player:
            #change pieces if needed
            temp_col = column + 1
            temp_row = row - 1
            while temp_col < 8 and temp_row >= 0:
                if begin_state[u'board'][temp_row * 8 + temp_col] == player:
                    break
                if begin_state[u'board'][temp_row * 8 + temp_col] != 0:
                    begin_state[u'board'][temp_row * 8 + temp_col] = player
                else:
                    break
                temp_col += 1
                temp_row -= 1
            break
        temp_col += 1
        temp_row -= 1


    end_state = {}
    end_state["board"] = begin_state["board"]

    # Write board to stdout
    json.dump(end_state, args.outfile)


def parse_arguments():
    """ Configures and parses command-line arguments """
    argparser = argparse.ArgumentParser(
        description="Naive Reversi implementation")
    argparser.add_argument("--infile",
                           nargs="?",
                           type=argparse.FileType("r"),
                           default=sys.stdin,
                           help="Filename of JSON file containing board and move, default stdin")
    argparser.add_argument("--outfile",
                           nargs="?",
                           type=argparse.FileType("w"),
                           default=sys.stdout,
                           help="Filename of JSON file to write board state to, default stdout")
    return argparser.parse_args()


if __name__ == "__main__":
    main()
