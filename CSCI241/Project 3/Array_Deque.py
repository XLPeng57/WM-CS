from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__size = 0
    self.__front = 0
    self.__back = 0
    
  def __str__(self):
    if self.__size == 0:
      arr = '[ ]'
      return arr

    arr = '[ '
    index = self.__front
    for i in range(self.__size-1):
      arr = arr + str(self.__contents[index]) + ', '
      index = (index+1+self.__capacity) % self.__capacity

    arr = arr + str(self.__contents[self.__back])
    arr = arr +' ]'

    return arr

  def __len__(self):
    return self.__size

  def __grow(self):
    old = self.__contents
    self.__capacity = 2 * self.__capacity 
    self.__contents = [None] * self.__capacity
    current = self.__front
    for i in range(self.__size):
      self.__contents[i] = old[current]
      current = (1+current) % len(old)
    self.__front = 0
    self.__back = len(old)-1
    
    
  def push_front(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    index = (self.__front - 1 + self.__capacity) % self.__capacity 
    self.__contents[index] = val
    self.__size += 1
    self.__front = index
    
  def pop_front(self):
    if self.__size == 0:
      return
    front_value = self.__contents[self.__front]
    self.__contents[self.__front] = None
    self.__front = (self.__front + 1 + self.__capacity) % self.__capacity
    self.__size -= 1
    return front_value

  def peek_front(self):
    if self.__size == 0:
      return
    return self.__contents[self.__front]
    
  def push_back(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    index = (self.__back + 1 + self.__capacity) % self.__capacity
    self.__contents[index] = val
    self.__size += 1
    self.__back = index
  
  def pop_back(self):
    if self.__size == 0:
      return
    back_value = self.__contents[self.__back]
    self.__contents[self.__back] = None
    self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
    self.__size -= 1
    return back_value

  def peek_back(self):
    if self.__size == 0:
      return
    return self.__contents[self.__back]


  

