from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise
from sklearn import decomposition
from sklearn import preprocessing

def main(start, end, num):
  tx = start + end
  X = TfidfVectorizer(max_df=0.5,stop_words='english').fit_transform(tx)
  lsa = decomposition.TruncatedSVD(n_components=len(start),n_iterations=10)
  X = lsa.fit_transform(X)
  X = preprocessing.Normalizer(copy=False).fit_transform(X)
  for i in xrange(len(end)):
    res = pairwise.cosine_similarity(X[i:i+1],X[len(start):len(start*2)])[0].tolist()
    print res.index(max(res))+1


def select_max(element, similarity, dim):
  candidates = []
  for i in xrange(dim*2):
    if i >= dim:
      candidates.append(similarity.tolist()[i])
  maximum = max(candidates)
  return candidates.index(maximum) + 1


if __name__ == '__main__':
  num = int(raw_input())
  start = [str(raw_input()) for r in range(num)]
  raw_input()
  end = [str(raw_input()) for r in range(num)]
  main(start, end, num)