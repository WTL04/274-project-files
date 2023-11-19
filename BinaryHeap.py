import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
  """
    helper method; returns the index of the left child of the element at index i
    """
  # todo
  return 2 * i + 1


def right(i: int) -> int:
  """
    helper method; returns the index of the right child of the element at index i
    """
  # todo
  return 2 * (i + 1)


def parent(i: int) -> int:
  """
    helper method; returns the index of the parent of the element at index i
    """
  # todo
  return (i - 1) // 2


def _new_array(n: int) -> np.array:
  """
    helper method; creates a new numpy array of 0's of size n
    """
  return np.zeros(n, object)


class BinaryHeap(Queue, Tree):

  def __init__(self):
    self.a = _new_array(1)
    self.n = 0

  def add(self, x: object):
    # todo
    if len(self.a) == self.n:
      self._resize()

    self.a[self.n] = x
    self.n += 1
    self._bubble_up_last()
    return True

  def remove(self):
    # FIX THIS
    if self.n == 0:
      raise IndexError
    x = self.a[0]
    self.a[0] = self.a[self.n - 1]
    self.n -= 1
    self._trickle_down_root()
    if 3 * self.n < len(self.a):
      self._resize()
    return x

  def depth(self, u) -> int:
    # CHECK IF RIGHT
    if u not in self.a:
      raise ValueError(f"{u} is not found in the binary tree.")

    i = np.where(self.a == u)[0][0]
    d = 0
    while i > 0:
      i = parent(i)
      d += 1

    return d

  def height(self) -> int:
    # CHECK IF RIGHT
    if self.n == 0:
      raise ValueError
    return math.floor(math.log2(self.n))

  def bf_order(self) -> list:
    # CHECK IF RIGHT
    list = []
    for i in range(self.n):
      list.append(self.a[i])
    return list

  def in_order(self) -> list:
    result = []
    self._in_order(0, result)
    return result

  def _in_order(self, index, result):
    if index < self.n:
      # Traverse the left subtree
      self._in_order(left(index), result)

      # Visit the current node (root)
      result.append(self.a[index])

      # Traverse the right subtree
      self._in_order(right(index), result)

  def post_order(self) -> list:
    # todo
    result = []
    self._post_order(0, result)
    return result

  def _post_order(self, index, result):
    if index < self.n:
      self._post_order(left(index), result)

      self._post_order(right(index), result)

      result.append(self.a[index])

  def pre_order(self) -> list:
    # todo
    result = []
    self._pre_order(0, result)
    return result

  def _pre_order(self, index, result):
    if index < self.n:
      # Visit the current node (root)
      result.append(self.a[index])

      # Traverse the left subtree
      self._pre_order(left(index), result)

      # Traverse the right subtree
      self._pre_order(right(index), result)

  def size(self) -> int:
    return self.n

  def find_min(self):
    if self.n == 0: raise IndexError()
    return self.a[0]

  def _bubble_up_last(self):
    # CHECK IF RIGHT
    i = self.n - 1
    p_idx = parent(i)

    while i > 0 and self.a[i] < self.a[p_idx]:
      self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
      i = p_idx
      p_idx = parent(i)

  def _resize(self):
    # todo
    b = _new_array(max(1, 2 * self.n))
    for i in range(0, self.n):
      b[i] = self.a[i]
    self.a = b

  def _trickle_down_root(self):
    abc = 0
    le = left(abc)
    ri = right(abc)
    while abc < self.n and le <= self.n and ri <= self.n and (
        self.a[abc] > self.a[le] or self.a[abc] > self.a[ri]):
      why = {abc: self.a[abc], le: self.a[le], ri: self.a[ri]}
      loc = min(why, key=why.get)
      self.a[abc], self.a[loc] = self.a[loc], self.a[abc]
      abc = loc
      le = left(abc)
      ri = right(abc)

  def __str__(self):
    return str(self.a[0:self.n])
