import numpy as np
from ArrayStack import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re

class Calculator:

  def __init__(self):
    self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

  def set_variable(self, k: str, v: float):
    self.dict.add(k, v)

  def matched_expression(self, s: str) -> bool:
    stack = ArrayStack()
    for char in s:
      if char == '(':
        stack.push(char)
      elif char == ')':
        if stack.size() == 0 or stack.pop() != '(':
          return False
    return stack.size() == 0

  def _build_parse_tree(self, exp: str) -> BinaryTree:
    if not self.matched_expression(exp):
        raise ValueError
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    exp = re.findall('[-+*/()]|\w+', exp)
    tree = BinaryTree.BinaryTree()
    tree.r = tree.Node()
    currentNode = tree.r
    for el in exp:
        node = tree.Node()
        if el == '(':
            currentNode = currentNode.insert_left(node)
        elif el in '+-/*':
            currentNode.set_val(el)
            currentNode.set_key(el)
            currentNode = currentNode.insert_right(node)
        elif el in variables:
            currentNode.set_key(el)
            currentNode.set_val(self.dict.find(el))
            currentNode = currentNode.parent
        elif el == ')':
            currentNode = currentNode.parent
    return tree
    

  def _evaluate(self, root):
    op = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
    }
    if root.left != None and root.right != None:
      fn  = op[root.k]
      return fn(self._evaluate(root.left), self._evaluate(root.right))
    elif root.left == None and root.right == None:
      if root.v != None:
          return float(root.v)
      raise ValueError(f"Missing value for variable {root.k}")
    elif root.left != None:
      return self._evaluate(root.left)
    else:
      return self._evaluate(root.right)
    

  def evaluate(self, exp):
    parseTree = self._build_parse_tree(exp)
    return self._evaluate(parseTree.r)

  def print_expression(self, exp: str):
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    everything_else = re.split('\w+', exp)

    result = ''
    for i in range(len(everything_else)):
      result += everything_else[i]
      if i < len(variables):
        value = self.dict.find(variables[i])
        if value != None:
          result += str(value)
        else:
          result += variables[i]
    print(result)


  
    
    