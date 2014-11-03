# coding: utf-8

class Mission:
  def __init__(self):
    self.field = [[0]*21 for i in range(21)]
    self.x = 10
    self.y = 10

  def get_gem(self, x, y):
    self.field[x][y] = 0

  def put_gem(self, x, y):
    self.field[x][y] = 1

  def move_x(self, step, sign=1):
    for i in range(1,step+1): self.get_gem(self.x+(i*sign), self.y)
    self.x += step * sign

  def move_y(self, step, sign=1):
    for j in range(1,step+1): self.get_gem(self.x, self.y+(j*sign))
    self.y += step * sign

  def command(self, direction, step):
    if direction == 'N': self.move_y(step)
    elif direction == 'E': self.move_x(step)
    elif direction == 'S': self.move_y(step, -1)
    elif direction == 'W': self.move_x(step, -1)

def main():
  while True:
    n_gems = input()
    if n_gems == 0: break

    m = Mission()
    for i in range(n_gems):
      x, y = map(int, raw_input().split(' '))
      m.put_gem(x, y)

    n_commands = input()
    for i in range(n_commands):
      direction, step = raw_input().split(' ')
      m.command(direction, int(step))

    if m.field == [[0]*21 for i in range(21)]: print 'Yes'
    else: print 'No'

if __name__ == '__main__':
  main()
