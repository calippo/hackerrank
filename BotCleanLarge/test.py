#!/usr/bin/python
import math

# Head ends here
def next_move(posx, posy, dimx, dimy, board):
  print_board(board, dimx)
  (posx_dirty, posy_dirty) = closest_dirty(posx, posy, dimx, dimy, board)
  print (posx, posy)
  print (posx_dirty, posy_dirty)
  if posx_dirty == dimx*2:
    print "END"
  elif(posx_dirty  == posx and posy_dirty == posy):
    board = clean(board, posx, posy)
  elif(posx_dirty < posx):
    (board, posx) = up(board, posx, posy)
  elif(posx_dirty > posx):
    (board, posx) = down(board, posx, posy)
  elif(posy_dirty > posy):
    (board, posy) = right(board, posx, posy)
  elif(posy_dirty < posy):
    (board, posy) = left(board, posx, posy)
  print_board(board, dimx)
  write_board(posx, posy, board, dimx, dimy)

def clean(board, posx, posy):
  board[posx][posy] = 'b'
  print "CLEAN"
  return board

def up(board, posx, posy):
  board[posx][posy] = '-'
  posx -= 1
  board[posx][posy] = ('d' if board[posx][posy] == 'd' else  'b')
  print "UP"
  return (board, posx)

def right(board, posx, posy):
  board[posx][posy] = '-'
  posy += 1
  board[posx][posy] = ('d' if board[posx][posy] == 'd' else  'b')
  print "RIGHT"
  return (board, posy)

def left(board, posx, posy):
  board[posx][posy] = '-'
  posy -= 1
  board[posx][posy] = ('d' if board[posx][posy] == 'd' else  'b')
  print "LEFT"
  return (board, posy)

def down(board, posx, posy):
  board[posx][posy] = '-'
  posx += 1
  board[posx][posy] = ('d' if board[posx][posy] == 'd' else  'b')
  print "DOWN"
  return (board, posx)

def write_board(posx, posy, board, dimx, dimy):
  with open("input.txt", "w") as input_:
    input_.write(str(posx) + " " + str(posy))
    input_.write("\n")
    input_.write(str(dimx) + " " + str(dimy))
    input_.write("\n")
    for i in range(dimx):
      input_.write(reduce(lambda x, y: x+y, board[i]))
      input_.write("\n")

def print_board(board, dimx):
  for i in range(dimx):
    print reduce(lambda x, y: x+y, board[i])

def closest_dirty(posx, posy, dimx, dimy, board):
  posx_dirty, posy_dirty = dimx*2, dimy*2
  for i in range(dimx):
    for j in range(dimy):
      if board[i][j] == 'd' and lower_distance(posx, posy, posx_dirty, posy_dirty, i, j):
        posx_dirty, posy_dirty = i, j
  return (posx_dirty, posy_dirty)

def lower_distance(posx, posy, posx_dirty, posy_dirty, i, j):
  d1 = math.fabs(posx - posx_dirty) + math.fabs(posy - posy_dirty)
  d2 = math.fabs(posx - i) + math.fabs(posy - j)
  return d2 < d1

# Tail starts here
if __name__ == "__main__":
  pos = [int(i) for i in raw_input().strip().split()]
  dim = [int(i) for i in raw_input().strip().split()]
  board = [[j for j in raw_input().strip()] for i in range(dim[0])]
  next_move(pos[0], pos[1], dim[0], dim[1], board)