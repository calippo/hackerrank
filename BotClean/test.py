#!/usr/bin/python
import math

# Head ends here
def next_move(posr, posc, board):
  print_board(board)
  (posr_dirty, posc_dirty) = closest_dirty(posr, posc, board)
  print (posr, posc)
  print (posr_dirty, posc_dirty)
  if posr_dirty == 15:
    print "END"
  elif(posr_dirty  == posr and posc_dirty == posc):
    board = clean(board, posr, posc)
  elif(posr_dirty < posr):
    board = up(board, posr, posc)
  elif(posr_dirty > posr):
    board = down(board, posr, posc)
  elif(posc_dirty > posc):
    board = right(board, posr, posc)
  elif(posc_dirty < posc):
    board = left(board, posr, posc)
  print_board(board)
  write_board(posr, posc, board)

def clean(board, posr, posc):
  board[posr][posc] = 'b'
  print "CLEAN"
  return board

def up(board, posr, posc):
  board[posr][posc] = '-'
  board[posr-1][posc] = ('d' if board[posr-1][posc] == 'd' else  'b')
  posr -= 1
  print "UP"
  return board

def right(board, posr, posc):
  board[posr][posc] = '-'
  board[posr][posc+1] = ('d' if board[posr][posc+1] == 'd' else  'b')
  posc += 1
  print "RIGHT"
  return board

def left(board, posr, posc):
  board[posr][posc] = '-'
  board[posr][posc-1] = ('d' if board[posr][posc-1] == 'd' else  'b')
  posc -= 1
  print "LEFT"
  return board

def down(board, posr, posc):
  board[posr][posc] = '-'
  board[posr+1][posc] = ('d' if board[posr+1][posc] == 'd' else  'b')
  posr += 1
  print "DOWN"
  return board

def write_board(posr, posc, board):
  with open("input.txt", "w") as input_:
    input_.write(str(posr) + " " + str(posc))
    input_.write("\n")
    for i in range(5):
      input_.write(reduce(lambda x, y: x+y, board[i]))
      input_.write("\n")

def print_board(board):
  for i in range(5):
    print reduce(lambda x, y: x+y, board[i])

def closest_dirty(posr, posc, board):
  posr_dirty, posc_dirty = 15, 15
  for i in range(5):
    for j in range(5):
      if board[i][j] == 'd' and lower_distance(posr, posc, posr_dirty, posc_dirty, i, j):
        posr_dirty, posc_dirty = i, j
  return (posr_dirty, posc_dirty)

def lower_distance(posr, posc, posr_dirty, posc_dirty, i, j):
  d1 = math.fabs(posr - posr_dirty) + math.fabs(posc - posc_dirty)
  d2 = math.fabs(posr - i) + math.fabs(posc - j)
  return d2 < d1

# Tail starts here
if __name__ == "__main__":
  pos = [int(i) for i in raw_input().strip().split()]
  board = [[j for j in raw_input().strip()] for i in range(5)]
  next_move(pos[0], pos[1], board)