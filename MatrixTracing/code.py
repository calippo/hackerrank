def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def main(m, n):
  limit = pow(10,9) + 7
  if n < m:
    m, n = n, m
  n, m = n + m - 2, m - 1
  num = factorial(n) / (factorial(m) * factorial(n - m))
  print num % limit

if __name__ == '__main__':
  tests_number = int(raw_input())
  tests = [raw_input().split(" ") for r in range(tests_number)]
  for n in tests:
    main(int(n[0]), int(n[1]))

