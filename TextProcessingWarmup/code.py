import re

def main(sentences):
  for sentence in sentences:
    printSentenceElementsNumber(sentence)

def printSentenceElementsNumber(sentence):
  def num_of_articles(article):
    return len(filter(lambda x: x == article,sentence.split(" ")))
  a_num = num_of_articles("a")
  an_num = num_of_articles("an")
  the_num = num_of_articles("the")
  dates_num = num_of_dates(sentence)
  print a_num + "\n" + an_num + "\n" + the_num + "\n" + dates_num

def or_months():
  months = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"]
  months += [str(n+1) for n in range(12)]
  conc = reduce(lambda x, y: str(x.lower()) + "|" + str(y.lower()), months)
  return "("+conc+")"

def or_days():
  days = [str(n + 1) for n in range(31)]
  days += [ str(n + 1) + "st" for n in range(31)]
  days += [ str(n + 1) + "th" for n in range(31)]
  conc = reduce(lambda x, y: str(x) + "|" + str(y), days)
  return "(" + conc + ")"

def add(match, sentence):
  matches = re.findall(match, sentence)
  print matches
  return len(matches)

def num_of_dates(sentence):
  num = add(or_months() + "(,?) " + or_days() + "(,?) (\d?\d?)\d\d", sentence)
  num += add(or_days() + " " + "(of ?)"+ or_months() +"(,?) (\d?\d?)\d\d", sentence)
  num += add("\d\d/\d\d/\d\d", sentence)
  num += add("\d\d/\d\d/\d\d\d\d", sentence)
  return num

if __name__ == '__main__':
  num = int(raw_input())
  def readLine(i, num):
    a = raw_input()
    if i + 1 != num:
      raw_input()
    return a
  sentences = [str(readLine(i, num)).lower() for i in range(num)]
  main(sentences)