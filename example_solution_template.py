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

    import pdb
    pdb.set_trace()



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
    convert = 0
    for i in range(row + 1, 8):
        if begin_state[u'board'][i * 8 + column] == player:
            convert = 1
            break
    #change pieces if needed
    if convert == 1:
        for i in range(row + 1, 8):
            if begin_state[u'board'][i * 8 + column] == player:
                break
            begin_state[u'board'][i * 8 + column] = player
    #above
    convert = 0
    for i in range(row - 1, 0, -1):
        if begin_state[u'board'][i * 8 + column] == player:
            convert = 1
            break
            # change pieces if needed
    if convert == 1:
        for i in range(row - 1, 0, -1):
            if begin_state[u'board'][i * 8 + column] == player:
                break
            begin_state[u'board'][i * 8 + column] = player
    #right
    convert = 0
    for i in range(column + 1, 8):
        if begin_state[u'board'][row * 8 + i] == player:
            convert = 1
            break
    #change pieces if needed
    if convert == 1:
        for i in range(column + 1, 8):
            if begin_state[u'board'][row * 8 + i] == player:
                break
            begin_state[u'board'][row * 8 + i] = player
    #left
    convert = 0
    for i in range(column - 1, 0, -1):
        if begin_state[u'board'][row * 8 + i] == player:
            convert = 1
            break
    #change pieces if needed
    if convert == 1:
        for i in range(column - 1, 0, -1):
            if begin_state[u'board'][row * 8 + i] == player:
                break
            begin_state[u'board'][row * 8 + i] = player



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
