import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re


class Calculator:

  def __init__(self):

    self.dict = ChainedHashTable.ChainedHashTable()  #var = keys, constants = values
    
  def set_variable(self, k: str, v: float):
    self.dict.add(k, v)

  def matched_expression(self, s: str) -> bool:
    stack = ArrayStack.ArrayStack()
    for w in s:
      if w == '(':
        stack.push(w)
      elif w == ')':
        if stack.size() == 0:
          return False
        stack.pop()
    if stack.size() == 0:
      return True
    else:
      return False

  def _build_parse_tree(self, exp: str) -> BinaryTree:
    # todo
    
    if not self.matched_expression(exp):
      raise ValueError
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    exp = re.findall('[-+*/()]|\w+', exp)
    tree = BinaryTree.BinaryTree()
    tree.r = tree.Node()
    current = tree.r

    for i in exp:
      node = tree.Node()
      if i == '(':
        current = current.insert_left(node)
      elif i in '+-/*':
        current.set_val(i)
        current.set_key(i)
        current = current.insert_right(node)
      elif i in variables:
        current.set_key(i)
        current.set_val(self.dict.find(i))
        current = current.parent
      elif i == ')':
        current = current.parent

    return tree
        

  def _evaluate(self, root):
    op = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
    }
    # todo

    if root.left != None and root.right != None:
      fn = op[root.k]
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

  def print_expression(self, exp):
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]  #creates list of varibales found in exp
    everything_else = re.split('\w+', exp)  #creates a lists of tokens, where each token consists of characters in between two variables, or in between the ends of the string and a variable

    format = ''
    for i in range(len(variables)):

      if self.dict.find(variables[i]) != None:
        variables[i] = str(self.dict.find(variables[i]))

    for i in range(len(everything_else)):
      format += everything_else[i]
      if i < len(variables):
        format += variables[i]

    print(format)
