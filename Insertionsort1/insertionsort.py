#!/bin/python

def main():
  input()
  ar = [int(i) for i in raw_input().strip().split()]
  insertionSort(ar)

# Head ends here
def insertionSort(ar):
  last = len(ar) - 1
  tbs = ar[last]
  for i in reversed(range(last)):
    if tbs < ar[i]:
      ar[i + 1] = ar[i]
      printArray(ar)
      if i == 0:
        ar[i + 1] = ar[i]
        ar[i] = tbs
        printArray(ar)
    else:
      ar[i + 1] = tbs
      printArray(ar)
      break


def printArray(ar):
  arr = ""
  for i in range(len(ar)):
    arr += str(ar[i])
    if i < len(ar) - 1:
      arr += " "
  print arr


# Tail starts here
if __name__ == '__main__':
  main()