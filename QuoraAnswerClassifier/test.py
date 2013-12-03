from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.svm import LinearSVC, SVC, SVR
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import numpy as np
import re as re

names_of_the_users = {}
def main(X_train, y_train, X_test, names):
  vectorizer = HashingVectorizer(non_negative=True)
  # X_train = vectorizer.transform(X_train)
  # X_test = vectorizer.transform(X_test)
  X_train = np.matrix(X_train)
  X_test = np.matrix(X_test)
  y_train = np.array(y_train)
  clf = LinearSVC()
  X_scaled = preprocessing.scale(X_train)
  X_tscaled = preprocessing.scale(X_test)
  clf.fit(X_scaled, y_train)
  pred = clf.predict(X_tscaled)
  for i in range(len(names)):
    val = "+1" if pred[i] == 1 else "-1"
    print str(names[i]) + " " + val

def removeNumbers(ds):
  print ds
  ds = [re.sub("\d+:","", el) for el in ds]
  ds = [re.sub("  "," ", el) for el in ds]
  dt = [el.split(" ") for el in ds]
  dt = nameToNum(dt)
  dt = [[float(el) for el in row] for row in dt]
  # ds = [reduce(lambda x, y: x + " " + y, doc[1::]) for doc in dt]
  return dt

def nameToNum(dt):
  for el in dt:
    if el[0] in names_of_the_users.keys():
      el[0] = names_of_the_users[el[0]]
    else:
      names_of_the_users[el[0]] = len(names_of_the_users) + 1
      el[0] = names_of_the_users[el[0]]
  return dt

if __name__ == '__main__':
  nums = [int(j) for j in raw_input().split(" ")]
  N, M = nums[0], nums[1]
  Raw_data = [str(raw_input()) for r in range(N)]
  q = int(raw_input())
  X_test = [str(raw_input()) for r in range(q)]
  y_train = [ 1 if ("+1" in el) else 0 for el in Raw_data]
  X_train = [ x.replace("+1","").replace("-1","") for x in Raw_data]
  names = [ el.split(" ")[0] for el in X_test]
  X_train = removeNumbers(X_train)
  X_test = removeNumbers(X_test)
  main(X_train, y_train, X_test, names)