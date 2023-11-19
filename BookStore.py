import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import MaxQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import time


class BookStore:
  '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

  def __init__(self):
    self.bookCatalog = ArrayList.ArrayList()
    #updated from arrayqueue to maxqueue
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
        s = Book.Book(key, title, group, rank, similar)
        self.bookCatalog.append(s)
        self.bookIndices.add(key, self.bookCatalog.size() - 1)
        self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
      # The following line is used to calculate the total time
      # of execution
      elapsed_time = time.time() - start_time
      print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

  def setRandomShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = RandomQueue.RandomQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting radomShoppingCart in {elapsed_time} seconds")

  def setShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = ArrayQueue.ArrayQueue()
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
    # Validating the index. Otherwise it crashes
    if i >= 0 and i < self.bookCatalog.size():
      start_time = time.time()
      s = self.bookCatalog.get(i)
      added = self.shoppingCart.add(s)
      elapsed_time = time.time() - start_time
      if type(added) == bool and added:
        print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
      else:
        print(f"Attempted to add {s} to shopping cart.\nAddition was not confirmed.")

  def searchBookByInfix(self, infix: str, cnt: int):
    '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''

    if cnt <= 0:
      return
    num = 0
    start_time = time.time()
    for i in range(self.bookCatalog.size()):
      book = self.bookCatalog.get(i)
      if infix in book.title:
        print(f'{book}')
        num += 1
        if num >= cnt:
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

    book = self.shoppingCart.max()  #returns the best selling book in shoppingCart

    print("getCartBestSeller returned")
    print(book.title)

    elapsed_time = time.time() - start_time
    print(f"Completed in {elapsed_time} seconds")

  def addBookByKey(self, key):
    start_time = time.time()
    bin = self.bookIndices.find(key)

    if bin != None:
      self.shoppingCart.add(self.bookCatalog.get(bin))
      print(f"Added title: {self.bookCatalog.get(bin).title}")

    else:
      print('Book not found.')

    elapsed_time = time.time() - start_time
    print(f"addBookByKey Completed in {elapsed_time} seconds")

  def addBookByPrefix(self, prefix):

    if prefix != "":
      book = self.sortedTitleIndices.findNear(prefix)

      if book != None and book.k[0:len(prefix)] == prefix:
        self.shoppingCart.add(self.bookCatalog.get(book.v))
        return book.k

    else:
      return None

  def bestsellers_with(self, infix, structure, n=0):
    best_sellers = None
    if structure == 1:
      best_sellers = BinarySearchTree.BinarySearchTree()
    elif structure == 2:
      best_sellers = BinaryHeap.BinaryHeap()
    else:
      print("Invalid data structure.")

    if best_sellers is not None:
      if infix == "":
        print("Invalid infix.")
      if n < 0:
        print("Invaid number of titles.")
      else:
        start_time = time.time()
        #todo

        found_books = []
        for i in range(self.bookCatalog.size()):
          book = self.bookCatalog.get(i)
          if infix in book.title:
            found_books.append(book)

        if n == 0:
          n = len(found_books)

        found_books.sort(key=lambda x: int(x.rank), reverse=True)  # Sort by rank (copies sold)

        for i in range(min(n, len(found_books))):
          if structure == 1:
            best_sellers.add(int(found_books[i].rank), found_books[i])
          elif structure == 2:
            found_books[i].rank = -int(
              found_books[i].rank)  # Invert ranks for max heap
            best_sellers.add(found_books[i])

        # Print the books in the selected data structure
        if structure == 1:
          for book in best_sellers.in_order():
            print(book)
        elif structure == 2:
          while best_sellers.size() > 0:
            print(best_sellers.remove())

        elasped_time = time.time() - start_time
        print(f"Displayed bestseller_with({infix}, {structure}, {n}) in {elasped_time} seconds")
