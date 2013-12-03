heroes = {}
def main(new):
  with open("training.txt","r") as f:
    training_set = [r.split(",") for r in f]
  new_set = []
  for r in training_set:
    n = []
    n.append(r[:5])
    n.append(r[5:10])
    n.append(r[10:])
    new_set.append(n)
  for r in new_set:
    for hero in r[0]:
      count(hero, 1, r[2])
    for hero in r[1]:
      count(hero, 2, r[2])
  num_hero = lambda x: heroes[x]
  sum_xy = lambda x, y: x + y
  for el in new:
    score_1 = reduce(sum_xy, map(num_hero, el[:5]))
    score_2 = reduce(sum_xy, map(num_hero, el[5:10]))
    if score_1 > score_2:
      print "1"
    else:
      print "2"

def count(hero, team, winner):
  if not hero in heroes.keys():
    heroes[hero] = 0
  if team == int(winner[0]):
    heroes[hero] += 1

if __name__ == '__main__':
  num = int(raw_input())
  new = [raw_input().split(',') for i in range(num)]
  main(new)