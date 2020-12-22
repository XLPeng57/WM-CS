import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):
  
  def setUp(self):
    self.__search_tree = Binary_Search_Tree()


#test empty tree 
  def test_empty_tree(self):
    self.assertEqual('[ ]', str(self.__search_tree), 'Empty list should print as "[ ]"')   
  def test_empty_tree_height(self):
    self.assertEqual( 0 , self.__search_tree.get_height())

#test insertion

    #tests do not need to rotate
    #test insert one node
  def test_one_node_tree_inorder(self):
    self.__search_tree.insert_element(1)
    self.assertEqual('[ 1 ]', str(self.__search_tree))
  def test_one_node_tree_preorder(self):
    self.__search_tree.insert_element(1)
    self.assertEqual('[ 1 ]', self.__search_tree.pre_order())
  def test_one_node_tree_postorder(self):
    self.__search_tree.insert_element(1)
    self.assertEqual('[ 1 ]', self.__search_tree.post_order())
  def test_one_node_tree_tolist(self):
    self.__search_tree.insert_element(1)
    self.assertEqual([1], self.__search_tree.to_list())
  def test_one_node_tree_height(self):
    self.__search_tree.insert_element(1)
    self.assertEqual( 1 , self.__search_tree.get_height())
  
    #test insert an exsiting value
  def test_one_node_tree_insert_exist_string(self):
    with self.assertRaises(ValueError):
      self.__search_tree.insert_element(1)
      self.__search_tree.insert_element(1)
    self.assertEqual('[ 1 ]', str(self.__search_tree))
  def test_one_node_tree_insert_exist_height(self):
    with self.assertRaises(ValueError):
      self.__search_tree.insert_element(1)
      self.__search_tree.insert_element(1)
    self.assertEqual( 1 , self.__search_tree.get_height())

    #test insert two nodes (root and a left child)
  def test_two_node_left_tree_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)    
    self.assertEqual('[ 0, 1 ]', str(self.__search_tree))
  def test_one_node_left_tree_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.assertEqual('[ 1, 0 ]', self.__search_tree.pre_order())
  def test_one_node_left_tree_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.assertEqual('[ 0, 1 ]', self.__search_tree.post_order())
  def test_one_node_left_tree_tolist(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.assertEqual([0, 1], self.__search_tree.to_list())
  def test_one_node_left_tree_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.assertEqual( 2, self.__search_tree.get_height())

    #test insert two nodes (root and a right child)
  def test_two_node_right_tree_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)    
    self.assertEqual('[ 1, 2 ]', str(self.__search_tree))
  def test_one_node_right_tree_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.assertEqual('[ 1, 2 ]', self.__search_tree.pre_order())
  def test_one_node_right_tree_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.assertEqual('[ 2, 1 ]', self.__search_tree.post_order())
  def test_one_node_right_tree_tolist(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.assertEqual([1, 2], self.__search_tree.to_list())
  def test_one_node_right_tree_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.assertEqual( 2, self.__search_tree.get_height()) 

    #test insert three node (root + left + right)
  def test_two_child_tree_inorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual('[ 2, 5, 7 ]', str(self.__search_tree))
  def test_two_child_tree_preorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual('[ 5, 2, 7 ]', self.__search_tree.pre_order())
  def test_two_child_tree_postorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual('[ 2, 7, 5 ]', self.__search_tree.post_order())
  def test_two_child_tree_tolist(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual([2, 5, 7], self.__search_tree.to_list())
  def test_two_child_right_tree_height(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual( 2, self.__search_tree.get_height()) 



    #tests need to rotate 
    #test single left rotation with three nodes
  def test_left_single_tree_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(17) 
    self.assertEqual('[ 7, 10, 17 ]', str(self.__search_tree))
  def test_left_single_tree_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(17) 
    self.assertEqual('[ 10, 7, 17 ]', self.__search_tree.pre_order())
  def test_left_single_tree_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(17) 
    self.assertEqual('[ 7, 17, 10 ]', self.__search_tree.post_order())
  def test_left_single_tree_tree_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(17) 
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_left_single_tree_tree_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(17) 
    self.assertEqual( [7, 10, 17], self.__search_tree.to_list())


    #test single right rotation with three nodes
  def test_right_single_tree_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(1) 
    self.assertEqual('[ 1, 5, 7 ]', str(self.__search_tree))
  def test_right_single_tree_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(1) 
    self.assertEqual('[ 5, 1, 7 ]', self.__search_tree.pre_order())
  def test_right_single_tree_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(1)  
    self.assertEqual('[ 1, 7, 5 ]', self.__search_tree.post_order())
  def test_right_single_tree_tree_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(1)  
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_right_single_tree_tree_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(1) 
    self.assertEqual( [1, 5, 7], self.__search_tree.to_list())

    #test double left-right rotation with three nodes
  def test_left_right_tree_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(9) 
    self.assertEqual('[ 7, 9, 10 ]', str(self.__search_tree))
  def test_left_right_tree_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(9) 
    self.assertEqual('[ 9, 7, 10 ]', self.__search_tree.pre_order())
  def test_left_right_tree_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(9) 
    self.assertEqual('[ 7, 10, 9 ]', self.__search_tree.post_order())
  def test_left_right_tree_tree_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(9) 
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_left_right_tree_tree_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(9) 
    self.assertEqual( [7, 9, 10], self.__search_tree.to_list())

    #test double right-left rotation with three nodes
  def test_right_left_tree_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(6)
    self.assertEqual('[ 5, 6, 7 ]', str(self.__search_tree))
  def test_right_left_tree_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(6) 
    self.assertEqual('[ 6, 5, 7 ]', self.__search_tree.pre_order())
  def test_right_left_tree_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(6)  
    self.assertEqual('[ 5, 7, 6 ]', self.__search_tree.post_order())
  def test_right_left_tree_tree_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(6)  
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_right_left_tree_tree_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(6) 
    self.assertEqual( [5, 6, 7], self.__search_tree.to_list())  

    # test a complex tree 
  def test_complex_insert_tree_inorder(self):
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(30) 
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(60)
    self.__search_tree.insert_element(70) 
    self.__search_tree.insert_element(80)
    self.__search_tree.insert_element(22)
    self.assertEqual('[ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ]', str(self.__search_tree))
  def test_complex_insert_preorder(self):
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(30) 
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(60)
    self.__search_tree.insert_element(70) 
    self.__search_tree.insert_element(80)
    self.__search_tree.insert_element(22) 
    self.assertEqual('[ 30, 20, 10, 5, 25, 22, 60, 50, 70, 80 ]', self.__search_tree.pre_order())
  def test_complex_insert_postorder(self):
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(30) 
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(60)
    self.__search_tree.insert_element(70) 
    self.__search_tree.insert_element(80)
    self.__search_tree.insert_element(22)  
    self.assertEqual('[ 5, 10, 22, 25, 20, 50, 80, 70, 60, 30 ]', self.__search_tree.post_order())
  def test_complex_insert_height(self):
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(30) 
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(60)
    self.__search_tree.insert_element(70) 
    self.__search_tree.insert_element(80)
    self.__search_tree.insert_element(22)  
    self.assertEqual( 4, self.__search_tree.get_height())
  def test_complex_insert_tolist(self):
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(30) 
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(60)
    self.__search_tree.insert_element(70) 
    self.__search_tree.insert_element(80)
    self.__search_tree.insert_element(22) 
    self.assertEqual([5, 10, 20, 22, 25, 30, 50, 60, 70, 80], self.__search_tree.to_list()) 

#test removal
    #test remove that do not need to rotate
    #test remove with empty tree
  def test_empty_tree_removal_string(self):
    with self.assertRaises(ValueError):
      self.__search_tree.remove_element(1)
    self.assertEqual( '[ ]' , str(self.__search_tree))
  
  def test_empty_tree_removal_height(self):
    with self.assertRaises(ValueError):
      self.__search_tree.remove_element(1)
    self.assertEqual( 0 , self.__search_tree.get_height())

    #test remove with only one value
  def test_one_node_tree_removal_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.remove_element(1)
    self.assertEqual('[ ]', str(self.__search_tree))
  def test_one_node_tree_removal_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.remove_element(1)
    self.assertEqual( 0 , self.__search_tree.get_height())

    #test remove with root node and a left child
  def test_one_node_left_tree_remove_parent_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(1)
    self.assertEqual( 1, self.__search_tree.get_height())

  def test_one_node_left_tree_remove_parent_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(1)
    self.assertEqual( '[ 0 ]', str(self.__search_tree))

  def test_one_node_left_tree_remove_parent_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(1)
    self.assertEqual( '[ 0 ]', self.__search_tree.pre_order())

  def test_one_node_left_tree_remove_parent_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(1)
    self.assertEqual( '[ 0 ]', self.__search_tree.post_order())
  
  def test_one_node_left_tree_remove_child_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(0)
    self.assertEqual( 1, self.__search_tree.get_height())

  def test_one_node_left_tree_remove_child_tolist(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(0)
    self.assertEqual([1], self.__search_tree.to_list())

  def test_one_node_left_tree_remove_child_inoder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(0)
    self.assertEqual( '[ 1 ]', str(self.__search_tree))

  def test_one_node_left_tree_remove_child_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(0)
    self.assertEqual( '[ 1 ]', self.__search_tree.pre_order())

  def test_one_node_left_tree_remove_child_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(0)
    self.__search_tree.remove_element(0)
    self.assertEqual( '[ 1 ]', self.__search_tree.post_order())


# test removal that needs a single left rotation
  def test_left_single_tree_removal_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(17) 
    self.__search_tree.remove_element(5)
    self.assertEqual('[ 7, 10, 17 ]', str(self.__search_tree))
  def test_left_single_tree_removal_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(17) 
    self.__search_tree.remove_element(5)
    self.assertEqual('[ 10, 7, 17 ]', self.__search_tree.pre_order())
  def test_left_single_tree_removal_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(17) 
    self.__search_tree.remove_element(5)
    self.assertEqual('[ 7, 17, 10 ]', self.__search_tree.post_order())
  def test_left_single_tree_removal_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(17) 
    self.__search_tree.remove_element(5) 
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_left_single_tree_removal_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(17) 
    self.__search_tree.remove_element(5) 
    self.assertEqual( [7, 10, 17], self.__search_tree.to_list())


# test removal that needs a single right rotation
  def test_right_single_tree_removal_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(1) 
    self.__search_tree.remove_element(10) 
    self.assertEqual('[ 1, 5, 7 ]', str(self.__search_tree))
  def test_right_single_tree_removal_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(1) 
    self.__search_tree.remove_element(10)
    self.assertEqual('[ 5, 1, 7 ]', self.__search_tree.pre_order())
  def test_right_single_tree_removal_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(1) 
    self.__search_tree.remove_element(10)
    self.assertEqual('[ 1, 7, 5 ]', self.__search_tree.post_order())
  def test_right_single_tree_tree_removal_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(1) 
    self.__search_tree.remove_element(10)  
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_right_single_tree_tree_removal_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(1) 
    self.__search_tree.remove_element(10)
    self.assertEqual( [1, 5, 7], self.__search_tree.to_list())


#test removal needs a double left-right rotation 
  def test_left_right_tree_removal_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(9) 
    self.__search_tree.remove_element(5)

    self.assertEqual('[ 7, 9, 10 ]', str(self.__search_tree))
  def test_left_right_tree_removal_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(9) 
    self.__search_tree.remove_element(5)
    self.assertEqual('[ 9, 7, 10 ]', self.__search_tree.pre_order())
  def test_left_right_tree_removal_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(9) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 7, 10, 9 ]', self.__search_tree.post_order())
  def test_left_right_tree_tree_removal_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(9) 
    self.__search_tree.remove_element(5)
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_left_right_tree_tree_removal_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(10) 
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(9) 
    self.__search_tree.remove_element(5) 
    self.assertEqual( [7, 9, 10], self.__search_tree.to_list())


#test removal needs double right-left rotation 
  def test_right_left_tree_remove_inorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(6)
    self.__search_tree.remove_element(10)
    self.assertEqual('[ 5, 6, 7 ]', str(self.__search_tree))
  def test_right_left_tree_remove_preorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(6)
    self.__search_tree.remove_element(10) 
    self.assertEqual('[ 6, 5, 7 ]', self.__search_tree.pre_order())
  def test_right_left_tree_remove_postorder(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(6)
    self.__search_tree.remove_element(10)  
    self.assertEqual('[ 5, 7, 6 ]', self.__search_tree.post_order())
  def test_right_left_tree_tree_remove_height(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(6)
    self.__search_tree.remove_element(10)  
    self.assertEqual( 2, self.__search_tree.get_height())
  def test_right_left_tree_tree_remove_tolist(self):
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5) 
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(6)
    self.__search_tree.remove_element(10)
    self.assertEqual( [5, 6, 7], self.__search_tree.to_list())  


# test a complex tree with removal(right-left and a single left)
  def test_complex_remove_tree_inorder(self):
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(31) 
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(55) 
    self.__search_tree.insert_element(34)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(25)
    self.__search_tree.remove_element(30)
    self.assertEqual('[ 31, 34, 45, 55 ]', str(self.__search_tree))
  def test_complex_remove_preorder(self):
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(31) 
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(55) 
    self.__search_tree.insert_element(34)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(25)
    self.__search_tree.remove_element(30) 
    self.assertEqual('[ 45, 31, 34, 55 ]', self.__search_tree.pre_order())
  def test_complex_remove_postorder(self):
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(31) 
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(55) 
    self.__search_tree.insert_element(34)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(25)
    self.__search_tree.remove_element(30)  
    self.assertEqual('[ 34, 31, 55, 45 ]', self.__search_tree.post_order())
  def test_complex_remove_height(self):
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(31) 
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(55) 
    self.__search_tree.insert_element(34)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(25)
    self.__search_tree.remove_element(30)
    self.assertEqual( 3, self.__search_tree.get_height())
  def test_complex_remove_tolist(self):
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(31) 
    self.__search_tree.insert_element(50)
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(55) 
    self.__search_tree.insert_element(34)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(25)
    self.__search_tree.remove_element(30) 
    self.assertEqual([31, 34, 45, 55], self.__search_tree.to_list()) 


    #test a complex tree with removal(left-right and a single right)(symmetric)
  def test_complex_remove_tree_symmetric_inorder(self):
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(50) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(55)
    self.__search_tree.insert_element(47) 
    self.__search_tree.insert_element(46)
    self.__search_tree.remove_element(30)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(55)
    self.assertEqual('[ 25, 45, 46, 47 ]', str(self.__search_tree))
  def test_complex_remove_symmetric_preorder(self):
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(50) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(55)
    self.__search_tree.insert_element(47) 
    self.__search_tree.insert_element(46)
    self.__search_tree.remove_element(30)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(55)
    self.assertEqual('[ 45, 25, 47, 46 ]', self.__search_tree.pre_order())
  def test_complex_remove_symmetric_postorder(self):
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(50) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(55)
    self.__search_tree.insert_element(47) 
    self.__search_tree.insert_element(46)
    self.__search_tree.remove_element(30)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(55)  
    self.assertEqual('[ 25, 46, 47, 45 ]', self.__search_tree.post_order())
  def test_complex_remove_symmetric_height(self):
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(50) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(55)
    self.__search_tree.insert_element(47) 
    self.__search_tree.insert_element(46)
    self.__search_tree.remove_element(30)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(55)
    self.assertEqual( 3, self.__search_tree.get_height())
  def test_complex_remove_symmetric_tolist(self):
    self.__search_tree.insert_element(45)
    self.__search_tree.insert_element(30)
    self.__search_tree.insert_element(50) 
    self.__search_tree.insert_element(25)
    self.__search_tree.insert_element(55)
    self.__search_tree.insert_element(47) 
    self.__search_tree.insert_element(46)
    self.__search_tree.remove_element(30)
    self.__search_tree.remove_element(50)
    self.__search_tree.remove_element(55) 
    self.assertEqual([25, 45, 46, 47], self.__search_tree.to_list()) 




if __name__ == '__main__':
  unittest.main()

