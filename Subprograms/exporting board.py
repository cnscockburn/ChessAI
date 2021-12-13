import chess
import chess.svg
import sys


board = chess.Board()
boardsvg = chess.svg.board()
outputfile = open('export.svg', "w")
outputfile.write(boardsvg)
outputfile.close()