class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

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
  
  def __recursive_insert(self,value,t):
  
    if t.value < value:
      if t.right == None:
        t.right = Binary_Search_Tree.__BST_Node(value)  
        t.change_height()
        return t.right
      else:
        self.__recursive_insert(value,t.right)
        t.change_height()

    if t.value > value:
      if t.left == None:
        t.left = Binary_Search_Tree.__BST_Node(value)
        t.change_height()
        return t.left
      else:
        self.__recursive_insert(value,t.left)
        t.change_height()
    if t.value == value:
      raise ValueError  

  def insert_element(self,value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
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
    return t
    
      

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root == None:
      raise ValueError
    if self.__root.value == value and self.__root.left == None and self.__root.right == None:
      self.__root = None
    else:
      self.__root = self.__recursive_remove(value, self.__root)
    
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
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
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
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
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
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    else:
      return '[ ' + self.__postorder(self.__root) + ' ]'

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
      return 0
    else:
      return self.__root.height
    

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass
  

