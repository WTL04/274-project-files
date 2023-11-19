import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
  def __init__(self):
    ArrayQueue.__init__(self)

      

  def remove(self) -> object:
    if self.n <= 0:
      raise IndexError()
    i = random.randint(0, self.n-1)
    x = self.a[(self.j + i) % len(self.a)]
    if i<self.n/2:
      for k in range(i, 0, -1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
      self.j = (self.j +1) % len(self.a)
    else:
      for k in range (i, self.n-1, 1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
    self.n = self.n - 1
    if len(self.a) > 3 * self.n:
      self.resize()
    
    return x
    
    
    
