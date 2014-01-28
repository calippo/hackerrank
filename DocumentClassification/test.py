from sklearn.svm import LinearSVC, SVC, SVR
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics
from sklearn.metrics import roc_curve, auc

import numpy as np

from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import pylab as pl
from sklearn import cross_validation

class LemmaTokenizer(object):
  def __init__(self):
    self.wnl = WordNetLemmatizer()
  def __call__(self, doc):
    return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

def main():
  with open("trainingdata.txt","r") as f:
    number = int(f.readline())
    training_set = [r.split(" ") for r in f]
  y = [doc[0] for doc in training_set]
  corpus = [reduce(lambda x, y: x + " " + y, doc[1::]) for doc in training_set]
  N = len(corpus)/2
  X_train = corpus[:N]
  data = corpus[N:]
  y_train = y[:N]
  y_test = y[N:]
  # vectorizer = CountVectorizer(tokenizer=LemmaTokenizer(), stop_words='english', lowercase=True)
  vectorizer = HashingVectorizer(non_negative=True, analyzer='word')
  # vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,)
  X_train = vectorizer.transform(X_train)
  data_test = vectorizer.transform(data)
  y_train = np.array(y_train)
  y_test = np.array(y_test)

  # Run classifier
  classifier = SVC(kernel='linear', probability=True, random_state=0)
  probas_ = classifier.fit(X_train, y_train).predict_proba(data_test)

  # Compute ROC curve and area the curve
  fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1])
  roc_auc = auc(fpr, tpr)
  print("Area under the ROC curve : %f" % roc_auc)

  # Plot ROC curve
  pl.clf()
  pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
  pl.plot([0, 1], [0, 1], 'k--')
  pl.xlim([0.0, 1.0])
  pl.ylim([0.0, 1.0])
  pl.xlabel('False Positive Rate')
  pl.ylabel('True Positive Rate')
  pl.title('Receiver operating characteristic example')
  pl.legend(loc="lower right")
  pl.show()

def test(c, X_train, y_train, data_test, y_test):
  clf = c[0]
  clf.fit(X_train, y_train)
  pred = clf.predict(data_test)
  print_confusion_matrix(y_test, pred)

  scores = cross_validation.cross_val_score(clf, X_train, y_train, cv=5)
  # print c[1] + " Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() / 2)
  # kf = KFold(len(y_train), n_folds=10, indices=False)
  # for train, test in kf:
  #   print("%s %s" % (train, test))
  # clf.fit(X_train, y_train)
  # count = 0
  # correct = 0
  # pred = clf.predict(new)
  # #
  # for i in range(len(y_new)):
  #   count += 1
  #   if y_new[i] == pred[i]:
  #     correct += 1
  # print c[1] + ": " + str(correct / (count + 0.0))

def print_confusion_matrix(y_test, y_pred):
  # Compute confusion matrix
  cm = confusion_matrix(y_test, y_pred)

  print(cm)

  # Show confusion matrix in a separate window
  pl.matshow(cm)
  pl.title('Confusion matrix')
  pl.colorbar()
  pl.ylabel('True label')
  pl.xlabel('Predicted label')
  pl.show()

if __name__ == '__main__':
  main()