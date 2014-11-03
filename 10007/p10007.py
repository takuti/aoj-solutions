# coding: utf-8

def swap(a, b):
  """ swap arguments to ascend order
  >>> swap(3, 2)
  2 3
  >>> swap(2, 2)
  2 2
  >>> swap(5, 3)
  3 5
  """
  result = (a, b) if a < b else (b, a)
  print '%d %d' % result

def main():
  while True:
    a, b = map(int, raw_input().split(' '))
    if [a, b] == [0, 0]: break
    swap(a, b)

if __name__ == '__main__':
  # import doctest
  # doctest.testmod()
  main()
