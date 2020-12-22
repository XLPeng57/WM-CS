class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
  
      
    def change_height(self):
      if self.right == None and self.left == None:
        self.height = 1
      if self.right == None and self.left != None:
        self.height = self.left.height + 1
      if self.left == None and self.right != None:
        self.height = self.right.height + 1
      if self.left != None and self.right != None:
        if self.left.height > self.right.height:
          self.height = self.left.height + 1
        elif self.left.height <= self.right.height:
          self.height = self.right.height + 1

  def __init__(self):
    self.__root = None
  
  def __balance(self,t):

    if t.right == None and t.left == None:
      balance = 0 
      return t
    if t.left == None and t.right != None:
      balance = t.right.height
    if t.right == None and t.left != None:
      balance = 0 - t.left.height
    if t.right != None and t.left != None:
      balance = t.right.height - t.left.height

    if balance == -1 or balance == 1:
      return t


    #right heavy
    #rotate left
    if balance == 2:
      if t.right.right == None:
        sub_balance = 0 - t.right.left.height
      elif t.right.left == None:
        sub_balance = t.right.right.height
      elif t.right.right != None and t.right.left != None:
        sub_balance = t.right.right.height - t.right.left.height
    

      if sub_balance >= 0:
        #single rotation
        if t == self.__root:
          oldroot = Binary_Search_Tree.__BST_Node(t.value)
          oldroot.left = t.left
          oldroot.right = t.right.left
          oldroot.change_height()
          self.__root = t.right
          self.__root.left = oldroot
          self.__root.change_height()
        else:
          oldroot = Binary_Search_Tree.__BST_Node(t.value)
          oldroot.left = t.left
          oldroot.right = t.right.left
          oldroot.change_height()
          t = t.right
          t.left = oldroot
          t.change_height()
        
      if sub_balance == -1 :
        #double rotation 
        if t == self.__root:
          first = Binary_Search_Tree.__BST_Node(t.right.value)
          first.right = t.right.right
          first.left = t.right.left.right
          first.change_height() 
          t.right = self.__root.right.left
          t.right.right = first
          t.change_height()
          second = Binary_Search_Tree.__BST_Node(t.value)
          second.left = self.__root.left
          second.right = self.__root.right.left
          second.change_height()
          self.__root = t.right
          self.__root.left = second
          self.__root.change_height()

        else:
          first = Binary_Search_Tree.__BST_Node(t.right.value)
          first.right = t.right.right
          first.left = t.right.left.right 
          first.change_height()
          t.right = t.right.left
          t.right.right = first
          t.change_height()
          second = Binary_Search_Tree.__BST_Node(t.value)
          second.left = t.left
          second.right = t.right.left
          second.change_height()
          t = t.right
          t.left = second
          t.change_height()
     
        
     #left heavy
     #rotate right
    if balance == -2:
      if t.left.right == None and t.left.left != None:
        sub_balance = 0 - t.left.left.height
      elif t.left.left == None and t.left.right != None:
        sub_balance = t.left.right.height
      else:
        sub_balance = t.left.right.height - t.left.left.height

      if sub_balance  <= 0 :
      #single rotation
        if t == self.__root:
          oldroot = Binary_Search_Tree.__BST_Node(t.value)
          oldroot.right = t.right
          oldroot.left = t.left.right 
          oldroot.change_height()           
          self.__root = t.left
          self.__root.right = oldroot
          self.__root.change_height()
        else:
          oldroot = Binary_Search_Tree.__BST_Node(t.value)
          oldroot.right = t.right
          oldroot.left = t.left.right
          oldroot.change_height()
          t = t.left
          t.right = oldroot
          t.change_height()

      if sub_balance == 1 :
        #double rotation     
        if t == self.__root:
          first = Binary_Search_Tree.__BST_Node(t.left.value)
          first.left = t.left.left
          first.right = t.left.right.left
          first.change_height()
          t.left = t.left.right
          t.left.left = first
          t.change_height()
          second = Binary_Search_Tree.__BST_Node(t.value)
          second.right = t.right
          second.left = t.left.right
          second.change_height()
          self.__root = t.left
          self.__root.right = second
          self.__root.change_height()
        
        else:
          first = Binary_Search_Tree.__BST_Node(t.left.value)
          first.left = t.left.left
          first.right = t.left.right.left
          first.change_height()
          t.left = t.left.right
          t.left.left = first
          t.change_height()
          second = Binary_Search_Tree.__BST_Node(t.value)
          second.right = t.right
          second.left = t.left.right
          second.change_height()
          t = t.left
          t.right = second
          t.change_height()
     
    return t

  def __recursive_insert(self,value,t):

    if t is None:
      t = Binary_Search_Tree.__BST_Node(value)  
      t.change_height()
      return self.__balance(t)
      
    else:
      if t.value < value:
        t. right = self.__recursive_insert(value,t.right)
        t.change_height()
      if t.value > value:
        t.left = self.__recursive_insert(value,t.left)
        t.change_height()
      if t.value == value:
        raise ValueError 

    return self.__balance(t)


  def insert_element(self,value):

    if self.__root == None:
      self.__root = Binary_Search_Tree.__BST_Node(value)
      return self.__root
    else:
      self.__recursive_insert(value,self.__root)
      
  def __find_min(self,t):
    min = t.right
    while min.left is not None:
      min = min.left
    return min

  def __recursive_remove(self,value,t):
    if t == None:
      raise ValueError
    if t.value < value:
      t.right = self.__recursive_remove(value,t.right)
    if t.value > value:
      t.left = self.__recursive_remove(value,t.left)
    if t.value == value:
      if t.left == None and t.right == None:
        return None
      elif t.left == None and t.right != None:
        return t.right
      elif t.right == None and t.left != None:
        return t.left
      else:
        min_val = self.__find_min(t)
        t.value = min_val.value
        t.right = self.__recursive_remove(min_val.value,t.right)
    t.change_height()
    return self.__balance(t)
    
  def remove_element(self, value):
    if self.__root == None:
      raise ValueError
    if self.__root.value == value and self.__root.left == None and self.__root.right == None:
      self.__root = None
      return self.__root
    if self.__root.value == value and self.__root.left != None and self.__root.right == None:
      self.__root = self.__root.left
      return self.__root
    if self.__root.value == value and self.__root.left == None and self.__root.right != None:
      self.__root = self.__root.right
      return self.__root
    else:
      self.__recursive_remove(value, self.__root)
    
  def __inorder(self,t):
    if t != None:
      left_child = self.__inorder(t.left)
      parent = str(t.value)
      right_child = self.__inorder(t.right)  
  
      if left_child != None and right_child != None:
        return left_child + ', ' + parent + ', ' + right_child
      if left_child != None and right_child == None:
        return left_child + ', ' + parent
      if right_child != None and left_child == None:
        return parent + ', ' + right_child
      if left_child == None and right_child == None:
        return parent

  def in_order(self):
    
    if self.__root == None:
      return '[ ]'
    else:
      return '[ ' + self.__inorder(self.__root) + ' ]'

  def __preorder(self,t):
    if t != None:
      left_child = self.__preorder(t.left)
      parent = str(t.value)
      right_child = self.__preorder(t.right) 
    
      if left_child != None and right_child != None:
        return parent + ', ' + left_child + ', '  + right_child
      if left_child != None and right_child == None:
        return parent + ', ' + left_child
      if right_child != None and left_child == None:
        return parent + ', ' + right_child
      if left_child == None and right_child == None:
        return parent

  def pre_order(self):
    
    if self.__root == None:
      return '[ ]'
    else:
      return '[ ' + self.__preorder(self.__root) + ' ]'


  def __postorder(self,t):
     if t != None:
      left_child = self.__postorder(t.left)
      parent = str(t.value)
      right_child = self.__postorder(t.right)  

      if left_child != None and right_child != None:
        return left_child + ', ' + right_child + ', ' + parent
      if left_child != None and right_child == None:
        return left_child + ', ' + parent
      if right_child != None and left_child == None:
        return right_child + ', ' + parent
      if left_child == None and right_child == None:
        return parent 

  def post_order(self):
    
    if self.__root == None:
      return '[ ]'
    else:
      return '[ ' + self.__postorder(self.__root) + ' ]'
 
  def get_height(self):
  
    if self.__root == None:
      return 0
    else:
      return self.__root.height
    
  def to_list(self):
    tolist = []
    return self.__recursive_list(self.__root,tolist)
  
  def __recursive_list(self,t,tolist):
    
    if t != None:
      self.__recursive_list(t.left,tolist)
      tolist.append(t.value)
      self.__recursive_list(t.right,tolist) 
      return tolist

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass
  