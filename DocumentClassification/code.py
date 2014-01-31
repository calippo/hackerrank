from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np

class LemmaTokenizer(object):
  def __init__(self):
    self.wnl = WordNetLemmatizer()
  def __call__(self, doc):
    return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

def main(new):
  with open("trainingdata.txt","r") as f:
    int(f.readline())
    training_set = [r.split(" ") for r in f]
  y = [int(doc[0]) for doc in training_set]
  corpus = [reduce(lambda x, y: x + " " + y, doc[1::]) for doc in training_set]
  # vectorizer = CountVectorizer(tokenizer=LemmaTokenizer(), stop_words='english', lowercase=True)
  vectorizer = HashingVectorizer()
  # vectorizer = HashingVectorizer()
  X_train = vectorizer.fit_transform(corpus)
  y_train = np.array(y)
  data = vectorizer.fit_transform(new)
  clf = (LinearSVC(), "SVM")
  # print Corups
  test(clf, X_train, y_train, data)

def test(c, X_train, y_train, data):
  clf = c[0]
  clf.fit(X_train, y_train)
  pred = clf.predict(data)
  for i in pred:
    print i

if __name__ == '__main__':
  num = int(raw_input())
  new = [ str(raw_input()) for r in range(num)]
  main(new)
