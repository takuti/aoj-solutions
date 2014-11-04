# coding: utf-8

def main():
  while True:
    (n, m, a) = map(int, raw_input().split(' '))
    if (n, m, a) == (0, 0, 0): break

    bars = []
    for i in range(m):
      (h, p, q) = map(int, raw_input().split(' '))
      bars.append((h, p, q))

    x = a
    while True:
      # Down step by step, and above bars are removed in each step
      # To handle straight down case (no possible bars), next_bar can be (0,x,x)
      next_bar = max([b for b in bars if b[1] == x or b[2] == x] + [(0, x, x)])
      x = next_bar[2] if next_bar[1] == x else next_bar[1]
      y = next_bar[0]
      map(lambda b: bars.remove(b), [b for b in bars if b[0] >= y])
      if bars == []: break
    print x

if __name__ == '__main__':
  main()
