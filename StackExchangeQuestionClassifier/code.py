import json
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np

topic_classes = {}
def findClass(topic):
  for class_ in topic_classes.keys():
    if topic_classes[class_] == topic:
      return class_

def popTopics(topics):
  t = ["gis", "security", "photo", "mathematica", "unix", "wordpress", "scifi", "electronics", "android", "apple"]
  for topic in t:
      topic_classes[topic] = len(topic_classes.keys())+1
  for i in range(len(topics)):
    cla = topics[i]
    topics[i] = topic_classes[cla]
  return topics

def main(data):
  test = [j["question"] + " " + j["excerpt"] for j in data]
  vectorizer = HashingVectorizer()
  with open("training.json","r") as f:
    f.readline()
    X_train, y_train = zip(*[(json.loads(j)["question"] + " " + json.loads(j)["excerpt"],json.loads(j)["topic"]) for j in f])
  X_train, y_train = list(X_train), list(y_train)
  X_train = vectorizer.fit_transform(X_train)
  y_train = np.array(popTopics(y_train))
  X_test = vectorizer.fit_transform(test)
  C = 1
  clfs = [(RandomForestClassifier(),"LR")]
  for i in range(20):
    C = C + 0.05
    clfs.append((LinearSVC(C=C), "C="+str(C)))
  for clf in clfs:
    clf[0].fit(X_train, y_train)
    scores = cross_validation.cross_val_score(clf[0], X_train, y_train, cv=5)
    print clf[1] + " Accuracy: %0.5f (+/- %0.5f)" % (scores.mean(), scores.std() / 2)

if __name__ == '__main__':
  num = int(raw_input())
  data = [json.loads(raw_input()) for i in range(num)]
  main(data)
