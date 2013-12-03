import numpy as np
from sklearn.svm import LinearSVC

heroes = {}
def main(new):
  with open("training.txt","r") as f:
    training_set = [r.split(",") for r in f]
  new_set = []
  for r in training_set:
    n = []
    n.append(r[:10])
    n.append(int(r[10:][0]))
    new_set.append(n)
  for r in new_set:
    for i in range(len(r[0])):
      count(r[0][i],i, r[1])
  y_train = [r[1] for r in new_set]
  num_hero = lambda x: heroes[x]
  X_train = []
  for el in new_set:
    my_heroes = map(num_hero, el[0])
    X_train.append(my_heroes)
  X_test = []
  for el in new:
    my_heroes = map(num_hero, el)
    X_test.append(my_heroes)
  X_train = np.matrix(X_train)
  X_test = np.matrix(X_test)
  y_train = np.array(y_train)
  clf = LinearSVC()
  clf.fit(X_train, y_train)
  pred = clf.predict(X_test)
  for i in pred:
    print i

def count(hero,i, winner):
  team = 1 if i <= 5 else 2
  if not hero in heroes.keys():
    heroes[hero] = 0
  if team == winner:
    heroes[hero] += 1

if __name__ == '__main__':
  num = int(raw_input())
  new = [raw_input().split(',') for i in range(num)]
  main(new)