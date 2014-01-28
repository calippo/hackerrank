import math

def next_move(posr, posc, board):
  (posr_dirty, posc_dirty) = closest_dirty(posr, posc, board)
  if posr_dirty == 15:
    print "END"
  elif(posr_dirty  == posr and posc_dirty == posc):
    print "CLEAN"
  elif(posr_dirty < posr):
    print "UP"
  elif(posr_dirty > posr):
    print "DOWN"
  elif(posc_dirty > posc):
    print "RIGHT"
  elif(posc_dirty < posc):
    print "LEFT"

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

if __name__ == "__main__":
  pos = [int(i) for i in raw_input().strip().split()]
  board = [[j for j in raw_input().strip()] for i in range(5)]
  next_move(pos[0], pos[1], board)