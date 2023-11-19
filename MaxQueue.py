from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):

  def __init__(self):
    SLLQueue.__init__(self)
    self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList

  def add(self, x: object):
    """
    adds an element to the end of this max queue
      INPUT: x the element to add
    """
    super().add(x)
    while self.max_deque.n != 0 and self.max_deque.dummy.prev.x < x:
      self.max_deque.remove_last()
    self.max_deque.add_last(x)
    
    
    

  def remove(self) -> object:
    """removes and returns the element at the head of the max queue"""
    x = super().remove()
    if x == self.max():
      self.max_deque.remove_first()
    
    return x
    
  def max(self):
    """returns the maximum element stored in the queue"""
    return self.max_deque.get(0)