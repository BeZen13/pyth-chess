import chess
import chess.svg

from IPython.display import svg
board = chess.Board()
SVG(chess.svg.board(board=board, size=400))