from __future__ import print_function
from gensim import models, similarities, corpora

def main(start, end, num):
  print (start)
  dictionary, corpus = create_corpus(start)
  lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(start))
  index = similarities.Similarity('/tmp/tst', lsi[corpus], len(start))
  for subs in end:
    vec_bow = dictionary.doc2bow(subs.lower().split())
    vec_lsi = lsi[vec_bow]
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print(sims[0][0]+1)

def create_corpus(documents):
  stoplist = set('for a he his her by she of as an at that the and to in is'.split())
  texts = [[word for word in document.lower().split() if word not in stoplist]
    for document in documents]
  all_tokens = sum(texts, [])
  tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
  texts = [[word for word in text if word not in tokens_once]
    for text in texts]
  dictionary = corpora.Dictionary(texts)
  corpus = [dictionary.doc2bow(text) for text in texts]
  return dictionary, corpus

if __name__ == '__main__':
  num = int(raw_input())
  start = [str(raw_input()) for r in range(num)]
  raw_input()
  end = [str(raw_input()) for r in range(num)]
  main(start, end, num)