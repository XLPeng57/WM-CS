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
  

#test insert element 
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
  def test_two_child_right_tree_height(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.assertEqual( 2, self.__search_tree.get_height()) 

  #test insertion for a complicated tree
  
  def test_8_nodes_tree_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.assertEqual('[ 5, 7, 10, 17, 18, 19, 20, 27 ]', str(self.__search_tree))
  
  def test_8_nodes_tree_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.assertEqual('[ 17, 7, 5, 10, 20, 19, 18, 27 ]', self.__search_tree.pre_order())

  def test_8_nodes_tree_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.assertEqual('[ 5, 10, 7, 18, 19, 27, 20, 17 ]', self.__search_tree.post_order())

  def test_8_nodes_tree_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.assertEqual(4, self.__search_tree.get_height())

#test remove_element 

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

  #test remove a non-exsiting value
  def test_one_node_tree_removal_non_exist_string(self):
    with self.assertRaises(ValueError):
      self.__search_tree.insert_element(1)
      self.__search_tree.remove_element(3)
    self.assertEqual('[ 1 ]', str(self.__search_tree))
  def test_one_node_tree_removal_non_exist_height(self):
    with self.assertRaises(ValueError):
      self.__search_tree.insert_element(1)
      self.__search_tree.remove_element(3)
    self.assertEqual( 1 , self.__search_tree.get_height())

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


#test remove with root node and a right child

  def test_one_node_right_tree_remove_child_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2) 
    self.__search_tree.remove_element(2)   
    self.assertEqual('[ 1 ]', str(self.__search_tree))
  def test_one_node_right_tree_remove_child_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(2)
    self.assertEqual('[ 1 ]', self.__search_tree.pre_order())
  def test_one_node_right_tree_remove_child_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(2)
    self.assertEqual('[ 1 ]', self.__search_tree.post_order())
  def test_one_node_right_tree_remove_child_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(2)
    self.assertEqual( 1, self.__search_tree.get_height()) 
  
  def test_one_node_right_tree_remove_parent_inorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2) 
    self.__search_tree.remove_element(1)   
    self.assertEqual('[ 2 ]', str(self.__search_tree))
  def test_one_node_right_tree_remove_parent_preorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(1)
    self.assertEqual('[ 2 ]', self.__search_tree.pre_order())
  def test_one_node_right_tree_remove_parent_postorder(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(1)
    self.assertEqual('[ 2 ]', self.__search_tree.post_order())
  def test_one_node_right_tree_remove_parent_height(self):
    self.__search_tree.insert_element(1)
    self.__search_tree.insert_element(2)
    self.__search_tree.remove_element(1)
    self.assertEqual( 1, self.__search_tree.get_height()) 
  

#test remove with root node and two child

  def test_two_child_tree_removal_parent_inorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 2, 7 ]', str(self.__search_tree))
    
  def test_two_child_tree_removal_parent_preorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 7, 2 ]', self.__search_tree.pre_order())

  def test_two_child_tree_removal_parent_postorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 2, 7 ]', self.__search_tree.post_order())

  def test_two_child_tree_removal_parent_height(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(5) 
    self.assertEqual( 2, self.__search_tree.get_height())

  def test_two_child_tree_removal_left_inorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(2) 
    self.assertEqual('[ 5, 7 ]', str(self.__search_tree))
    
  def test_two_child_tree_removal_left_preorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(2) 
    self.assertEqual('[ 5, 7 ]', self.__search_tree.pre_order())

  def test_two_child_tree_removal_left_postorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(2) 
    self.assertEqual('[ 7, 5 ]', self.__search_tree.post_order())

  def test_two_child_tree_removal_left_height(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(2) 
    self.assertEqual( 2, self.__search_tree.get_height())


  def test_two_child_tree_removal_right_inorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 2, 5 ]', str(self.__search_tree))
    
  def test_two_child_tree_removal_right_preorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 5, 2 ]', self.__search_tree.pre_order())

  def test_two_child_tree_removal_right_postorder(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 2, 5 ]', self.__search_tree.post_order())

  def test_two_child_tree_removal_right_height(self):
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(2) 
    self.__search_tree.insert_element(7) 
    self.__search_tree.remove_element(7) 
    self.assertEqual( 2 , self.__search_tree.get_height())

  
#test remove one element from a complicated tree
  #remove 27
  def test_complicated_tree_remove_27_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(27) 
    self.assertEqual('[ 5, 7, 10, 17, 18, 19, 20 ]', str(self.__search_tree))

  def test_complicated_tree_remove_27_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(27) 
    self.assertEqual('[ 17, 7, 5, 10, 20, 19, 18 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_27_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(27) 
    self.assertEqual('[ 5, 10, 7, 18, 19, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_27_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(27) 
    self.assertEqual( 4, self.__search_tree.get_height())

  
  #remove 18
  def test_complicated_tree_remove_18_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(18) 
    self.assertEqual('[ 5, 7, 10, 17, 19, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_18_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(18) 
    self.assertEqual('[ 17, 7, 5, 10, 20, 19, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_18_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(18) 
    self.assertEqual('[ 5, 10, 7, 19, 27, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_18_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(18) 
    self.assertEqual( 3, self.__search_tree.get_height())

  #remove 19
  def test_complicated_tree_remove_19_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(19) 
    self.assertEqual('[ 5, 7, 10, 17, 18, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_19_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(19) 
    self.assertEqual('[ 17, 7, 5, 10, 20, 18, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_19_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(19) 
    self.assertEqual('[ 5, 10, 7, 18, 27, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_19_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(19) 
    self.assertEqual( 3, self.__search_tree.get_height())

  #remove 20
  def test_complicated_tree_remove_20_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(20) 
    self.assertEqual('[ 5, 7, 10, 17, 18, 19, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_20_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(20) 
    self.assertEqual('[ 17, 7, 5, 10, 27, 19, 18 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_20_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(20) 
    self.assertEqual('[ 5, 10, 7, 18, 19, 27, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_20_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(20) 
    self.assertEqual( 4, self.__search_tree.get_height())

  #remove 10
  def test_complicated_tree_remove_10_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(10) 
    self.assertEqual('[ 5, 7, 17, 18, 19, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_10_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(10) 
    self.assertEqual('[ 17, 7, 5, 20, 19, 18, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_10_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(10) 
    self.assertEqual('[ 5, 7, 18, 19, 27, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_10_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(10) 
    self.assertEqual( 4, self.__search_tree.get_height())

  #remove 5
  def test_complicated_tree_remove_5_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 7, 10, 17, 18, 19, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_5_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 17, 7, 10, 20, 19, 18, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_5_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(5) 
    self.assertEqual('[ 10, 7, 18, 19, 27, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_5_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(5) 
    self.assertEqual( 4, self.__search_tree.get_height())
  
  #remove 7
  def test_complicated_tree_remove_7_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 5, 10, 17, 18, 19, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_7_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 17, 10, 5, 20, 19, 18, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_7_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(7) 
    self.assertEqual('[ 5, 10, 18, 19, 27, 20, 17 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_7_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(7) 
    self.assertEqual( 4, self.__search_tree.get_height())

  #remove 17
  def test_complicated_tree_remove_17_inorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(17) 
    self.assertEqual('[ 5, 7, 10, 18, 19, 20, 27 ]', str(self.__search_tree))

  def test_complicated_tree_remove_17_preorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(17) 
    self.assertEqual('[ 18, 7, 5, 10, 20, 19, 27 ]', self.__search_tree.pre_order())

  def test_complicated_tree_remove_17_postorder(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(17) 
    self.assertEqual('[ 5, 10, 7, 19, 27, 20, 18 ]', self.__search_tree.post_order())
  
  def test_complicated_tree_remove_17_height(self):
    self.__search_tree.insert_element(17)
    self.__search_tree.insert_element(7)
    self.__search_tree.insert_element(5)
    self.__search_tree.insert_element(10)
    self.__search_tree.insert_element(20)
    self.__search_tree.insert_element(19)
    self.__search_tree.insert_element(18) 
    self.__search_tree.insert_element(27) 
    self.__search_tree.remove_element(17) 
    self.assertEqual( 3, self.__search_tree.get_height())
  
if __name__ == '__main__':
  unittest.main()
