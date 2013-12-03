import math

# Head ends here
def next_move(posx, posy, dimx, dimy, board):
  (posx_dirty, posy_dirty) = closest_dirty(posx, posy, dimx, dimy, board)
  if posx_dirty == dimx*2:
    print "END"
  elif(posx_dirty  == posx and posy_dirty == posy):
    print "CLEAN"
  elif(posx_dirty < posx):
    print "UP"
  elif(posx_dirty > posx):
    print "DOWN"
  elif(posy_dirty > posy):
    print "RIGHT"
  elif(posy_dirty < posy):
    print "LEFT"

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