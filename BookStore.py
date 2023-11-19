import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
#import BinaryHeap
#import AdjacencyList
import time
import MaxQueue

class BookStore:
  '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

  def __init__(self):
    self.bookCatalog = ArrayList.ArrayList()
    self.shoppingCart = MaxQueue.MaxQueue()
    self.bookIndices = ChainedHashTable.ChainedHashTable()
    self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()
  def loadCatalog(self, fileName: str):
    '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
    self.bookCatalog = DLList.DLList()
    with open(fileName, encoding="utf8") as f:
      # The following line is the time that the computation starts
      start_time = time.time()
      for line in f:
        (key, title, group, rank, similar) = line.split("^")
        b = Book.Book(key, title, group, rank, similar)
        self.bookCatalog.append(b)
        self.sortedTitleIndices.add(title, self.bookCatalog.size() -1)
      # The following line is used to calculate the total time
      # of execution
      elapsed_time = time.time() - start_time
      print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

  def setRandomShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = MaxQueue.MaxQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting radomShoppingCart in {elapsed_time} seconds")

  def setShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = MaxQueue.MaxQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting radomShoppingCart in {elapsed_time} seconds")

  def removeFromCatalog(self, i: int):
    '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
    # The following line is the time that the computation starts
    start_time = time.time()
    self.bookCatalog.remove(i)
    # The following line is used to calculate the total time
    # of execution
    elapsed_time = time.time() - start_time
    print(f"Remove book {i} from books in {elapsed_time} seconds")

  def addBookByIndex(self, i: int):
    '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
    # Validating the index. Otherwise it  crashes
    if i >= 0 and i < self.bookCatalog.size():
      start_time = time.time()
      s = self.bookCatalog.get(i)
      added = self.shoppingCart.add(s)
      elapsed_time = time.time() - start_time
      if type(added) == bool and added:
        print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
      else:
        print(
          f"Attempted to add {s} to shopping cart.\nAddition was not confirmed."
        )

  def searchBookByInfix(self, infix: str, cnt: int):
    '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
    start_time = time.time()

    count = 0

    for book in self.bookCatalog:
      if infix in book.title:
        print(book)
        count += 1

        if count == cnt:
          break
    

    elapsed_time = time.time() - start_time
    print(f"searchBookByInfix Completed in {elapsed_time} seconds")

  def removeFromShoppingCart(self):
    '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
    start_time = time.time()
    if self.shoppingCart.size() > 0:
      u = self.shoppingCart.remove()
      elapsed_time = time.time() - start_time
      print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

  def getCartBestSeller(self):
    start_time = time.time()
    book = self.shoppingCart.max()
    elapsed_time = time.time() - start_time    
    print("getCartBestSeller returned")
    print(book.title)
    print(f"Completed in {elapsed_time} seconds")


  def addBookByKey(self, key):
    start_time = time.time()
    book = self.bookIndices.find(key)
    if book != None:
      self.shoppingCart.add(self.bookCatalog.get(book))
      print(f"Added title: {self.bookCatalog.get(book).title}")
    else:
      print("Book not found")
    
    elapsed_time = time.time() - start_time
    print(f"addBookByKey Completed in {elapsed_time} seconds")

  def addBookByPrefix(self, prefix):
    if prefix != "":
      book = self.sortedTitleIndices.find_smallest_greater_node(prefix)
      if book != None and (book.k[0:len(prefix)] == prefix):
        b = self.bookCatalog.get(book.v)
        self.shoppingCart.add(b)
        return b.title
    else:
      return None

    '''if book != None and book.k[0:len(prefix)] == prefix:

      print(f"Added first matched title: {book.k}")
      self.shoppingCart.add(self.bookCatalog.get(book.v))

    else:
      print("Error: Prefix was not found.")'''
    
    
    
    
    
    
    
    
    
    








      
    
    
        

  
