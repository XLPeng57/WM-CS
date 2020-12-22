import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

  # test deque
  # test emtpy duque
  def test_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')

  def test_empty_length_deque(self):
    self.assertEqual(0, len(self.__deque))

  # test push methods 
  # test push_front  
  def test_push_front_with_one(self):
    self.__deque.push_front('CS')
    self.assertEqual('[ CS ]', str(self.__deque))
  
  def test_push_front_with_one_length(self):
    self.__deque.push_front('CS')
    self.assertEqual(1, len(self.__deque))

  def test_push_front_with_two(self):
    self.__deque.push_front('Emma')
    self.__deque.push_front('CS')
    self.assertEqual('[ CS, Emma ]', str(self.__deque))

  def test_push_front_with_two_length(self):
    self.__deque.push_front('Emma')
    self.__deque.push_front('CS')
    self.assertEqual(2, len(self.__deque))

  def test_push_front_with_three(self):
    self.__deque.push_front('Emma')
    self.__deque.push_front('CS')
    self.__deque.push_front('Math')
    self.assertEqual('[ Math, CS, Emma ]', str(self.__deque))

  def test_push_front_with_three_length(self):
    self.__deque.push_front('Emma')
    self.__deque.push_front('CS')
    self.__deque.push_front('Math')
    self.assertEqual(3, len(self.__deque))

  # test push_back 
  def test_push_back_with_one(self):
    self.__deque.push_back('Emma')
    self.assertEqual('[ Emma ]', str(self.__deque))

  def test_push_back_with_one_length(self):
    self.__deque.push_back('Emma')
    self.assertEqual(1, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_back('Emma')
    self.__deque.push_back('Math')
    self.assertEqual('[ Emma, Math ]', str(self.__deque))

  def test_push_back_with_two_length(self):
    self.__deque.push_back('Emma')
    self.__deque.push_back('Math')
    self.assertEqual(2, len(self.__deque))

  def test_push_back_with_three(self):
    self.__deque.push_back('Emma')
    self.__deque.push_back('Math')
    self.__deque.push_back('7')
    self.assertEqual('[ Emma, Math, 7 ]', str(self.__deque))

  def test_push_back_with_three_length(self):
    self.__deque.push_back('Emma')
    self.__deque.push_back('Math')
    self.__deque.push_back('7')
    self.assertEqual(3, len(self.__deque))

  # test push one front and push one back 
  def test_push_one_front_one_back(self):
    self.__deque.push_front('Emma')
    self.__deque.push_back('Math')
    self.assertEqual('[ Emma, Math ]', str(self.__deque))

  def test_push_one_front_one_back_length(self):
    self.__deque.push_front('Emma')
    self.__deque.push_back('Math')
    self.assertEqual(2, len(self.__deque))

  def test_push_one_back_one_front(self):
    self.__deque.push_back('Emma')
    self.__deque.push_front('Math')
    self.assertEqual('[ Math, Emma ]', str(self.__deque))
  
  def test_push_one_back_one_front_length(self):
    self.__deque.push_back('Emma')
    self.__deque.push_front('Math')
    self.assertEqual(2, len(self.__deque))


  # test pop_front method
  def test_pop_front_from_empty_return_value(self):
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)

  def test_pop_front_from_empty_remaining(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_from_empty_length(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

    #test pop_front from one element pushed from front and back
  def test_pop_front_from_one_element_front_return_value(self):
    self.__deque.push_front('Emma')
    returned = self.__deque.pop_front()
    self.assertEqual('Emma', returned)

  def test_pop_front_from_one_element_front_remaining(self):
    self.__deque.push_front('Emma')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_from_one_element_front_length(self):
    self.__deque.push_front('Emma')
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_front_from_one_element_back_return_value(self):
    self.__deque.push_back('Emma')
    returned = self.__deque.pop_front()
    self.assertEqual('Emma', returned)

  def test_pop_front_from_one_element_back_remaining(self):
    self.__deque.push_back('Emma')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_from_one_element_back_length(self):
    self.__deque.push_back('Emma')
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

    #pop front element from two front push elements
  def test_pop_front_from_two_element_front_return_value(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    returned = self.__deque.pop_front()
    self.assertEqual('Econ', returned)

  def test_pop_front_from_two_element_front_remaining(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_front()
    self.assertEqual('[ Math ]', str(self.__deque))
  
  def test_pop_front_from_two_element_front_length(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))

    #pop front element from two back push elements
  def test_pop_front_from_two_element_back_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    returned = self.__deque.pop_front()
    self.assertEqual('Math', returned)

  def test_pop_front_from_two_element_back_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_front()
    self.assertEqual('[ Econ ]', str(self.__deque))
  
  def test_pop_front_from_two_element_back_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))
  
    #test pop_back from two elements pushed from front and back 
  def test_pop_front_from_two_element_front_back_return_value(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    returned = self.__deque.pop_front()
    self.assertEqual('Math', returned)

  def test_pop_front_from_two_element_front_back_remaining(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_front()
    self.assertEqual('[ Econ ]', str(self.__deque))

  def test_pop_front_from_two_element_front_back_length(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))

  def test_pop_front_from_two_element_back_front_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    returned = self.__deque.pop_front()
    self.assertEqual('Econ', returned)

  def test_pop_front_from_two_element_back_front_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_front()
    self.assertEqual('[ Math ]', str(self.__deque))

  def test_pop_front_from_two_element_back_front_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))
  
  #test pop front method with three element
  def test_pop_front_from_three_element_back_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    returned = self.__deque.pop_front()
    self.assertEqual('Math', returned)

  def test_pop_front_from_three_element_back_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    self.__deque.pop_front()
    self.assertEqual('[ Econ, Emma ]', str(self.__deque))

  def test_pop_front_from_three_element_back_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    self.__deque.pop_front()
    self.assertEqual(2, len(self.__deque))

  #test pop_back method

  def test_pop_back_from_empty_return_value(self):
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)

  def test_pop_back_from_empty_remaining(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_from_empty_length(self):
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

    # test pop_back from one element pushed from front and back 
  def test_pop_back_from_one_element_front_return_value(self):
    self.__deque.push_front('Hello')
    returned = self.__deque.pop_back()
    self.assertEqual('Hello', returned)

  def test_pop_back_from_one_element_front_remaining(self):
    self.__deque.push_front('Hello')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_back_from_one_element_front_length(self):
    self.__deque.push_front('Emma')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_from_one_element_back_return_value(self):
    self.__deque.push_back('Hi')
    returned = self.__deque.pop_back()
    self.assertEqual('Hi', returned)

  def test_pop_back_from_one_element_back_remaining(self):
    self.__deque.push_back('Hi')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_back_from_one_element_back_length(self):
    self.__deque.push_back('Hi')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

    #pop back element from two front push elements
  def test_pop_back_from_two_element_front_return_value(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    returned = self.__deque.pop_back()
    self.assertEqual('Math', returned)

  def test_pop_back_from_two_element_front_remaining(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_back()
    self.assertEqual('[ Econ ]', str(self.__deque))
  
  def test_pop_back_from_two_element_front_length(self):
    self.__deque.push_front('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))

    #pop back element from two back push elements
  def test_pop_back_from_two_element_back_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    returned = self.__deque.pop_back()
    self.assertEqual('Econ', returned)

  def test_pop_back_from_two_element_back_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_back()
    self.assertEqual('[ Math ]', str(self.__deque))
  
  def test_pop_back_from_two_element_back_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))

  #test pop_back from two elements pushed from front and back 
  def test_pop_back_from_two_element_front_back_return_value(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    returned = self.__deque.pop_back()
    self.assertEqual('Econ', returned)

  def test_pop_back_from_two_element_front_back_remaining(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_back()
    self.assertEqual('[ Math ]', str(self.__deque))
  
  def test_pop_back_from_two_element_front_back_length(self):
    self.__deque.push_front('Math')
    self.__deque.push_back('Econ')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))

  def test_pop_back_from_two_element_back_front_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    returned = self.__deque.pop_back()
    self.assertEqual('Math', returned)

  def test_pop_back_from_two_element_back_front_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_back()
    self.assertEqual('[ Econ ]', str(self.__deque))
  
  def test_pop_back_from_two_element_back_front_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_front('Econ')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))
  
  #test pop back method with three element
  def test_pop_back_from_three_element_back_return_value(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    returned = self.__deque.pop_back()
    self.assertEqual('Emma', returned)

  def test_pop_back_from_three_element_back_remaining(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    self.__deque.pop_back()
    self.assertEqual('[ Math, Econ ]', str(self.__deque))

  def test_pop_back_from_three_element_back_length(self):
    self.__deque.push_back('Math')
    self.__deque.push_back('Econ')
    self.__deque.push_back('Emma')
    self.__deque.pop_back()
    self.assertEqual(2, len(self.__deque))
  

  #test peek methods
  def test_peek_front_from_one_element_front(self):
    self.__deque.push_front('Emma')
    returned = self.__deque.peek_front()
    self.assertEqual('Emma', returned)

  def test_peek_back_from_one_element_front(self):
    self.__deque.push_front('Emma')
    returned = self.__deque.peek_back()
    self.assertEqual('Emma', returned)

  def test_peek_front_from_one_element_back(self):
    self.__deque.push_back('Emma')
    returned = self.__deque.peek_front()
    self.assertEqual('Emma', returned)

  def test_peek_back_from_one_element_back(self):
    self.__deque.push_back('Haha')
    returned = self.__deque.peek_back()
    self.assertEqual('Haha', returned)

  def test_peek_back_from_two_element(self):
    self.__deque.push_front('Emma')
    self.__deque.push_back('Tina')
    returned = self.__deque.peek_back()
    self.assertEqual('Tina', returned)

  def test_peek_front_from_two_element(self):
    self.__deque.push_front('Emma')
    self.__deque.push_back('Tina')
    returned = self.__deque.peek_front()
    self.assertEqual('Emma', returned)

  # test stack 
  # test emtpy stack
  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')

  def test_empty_length_stack(self):
    self.assertEqual(0, len(self.__stack))

  # test push method 
  def test_push_with_one(self):
    self.__stack.push('CS')
    self.assertEqual('[ CS ]', str(self.__stack))
  
  def test_push_with_one_length(self):
    self.__stack.push('CS')
    self.assertEqual(1, len(self.__stack))

  def test_push_with_two(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.assertEqual('[ Math, CS ]', str(self.__stack))
  
  def test_push_with_two_length(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.assertEqual(2, len(self.__stack))

  def test_push_with_three(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.__stack.push('Econ')
    self.assertEqual(3, len(self.__stack))

  def test_push_with_three_length(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.__stack.push('Econ')
    self.assertEqual('[ Econ, Math, CS ]', str(self.__stack))

  # test pop method 
  def test_pop_with_empty_stack_return_value(self):
    returned = self.__stack.pop()
    self.assertEqual(None, returned)

  def test_pop_with_empty_stack_remaining(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_with_one_return_value(self):
    self.__stack.push('CS')
    returned = self.__stack.pop()
    self.assertEqual('CS', returned)

  def test_pop_with_one_length(self):
    self.__stack.push('CS')
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_pop_with_one_remaining(self):
    self.__stack.push('CS')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_with_two_return_value(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    returned = self.__stack.pop()
    self.assertEqual('Math', returned)

  def test_pop_with_two_length(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_pop_with_two_remaining(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    self.__stack.pop()
    self.assertEqual('[ CS ]', str(self.__stack))

# test peek method 
  def test_peek_with_empty_stack(self):
    returned = self.__stack.peek()
    self.assertEqual(None, returned)

  def test_peek_with_one_return_value(self):
    self.__stack.push('CS')
    returned = self.__stack.peek()
    self.assertEqual('CS', returned)

  def test_peek_with_two_return_value(self):
    self.__stack.push('CS')
    self.__stack.push('Math')
    returned = self.__stack.peek()
    self.assertEqual('Math', returned)
  
  # test queue
  # test empty queue
  def test_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')

  def test_empty_length_queue(self):
    self.assertEqual(0, len(self.__queue))

  # test enqueue
  def test_enqueue_with_one(self):
    self.__queue.enqueue(12)
    self.assertEqual('[ 12 ]', str(self.__queue))

  def test_enqueue_with_one_length(self):
    self.__queue.enqueue(12)
    self.assertEqual(1, len(self.__queue))

  def test_enqueue_with_two(self):
    self.__queue.enqueue('CS')
    self.__queue.enqueue('7')
    self.assertEqual('[ CS, 7 ]', str(self.__queue))

  def test_enqueue_with_two_length(self):
    self.__queue.enqueue('CS')
    self.__queue.enqueue('7')
    self.assertEqual(2, len(self.__queue))

  # test dequeue

  def test_dequeue_with_empty(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_with_one_remaining(self):
    self.__queue.enqueue('CS')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_with_one_return_value(self):
    self.__queue.enqueue('CS')
    returned = self.__queue.dequeue()
    self.assertEqual('CS', returned)

  def test_dequeue_with_one_length(self):
    self.__queue.enqueue('CS')
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_with_two_remaining_value(self):
    self.__queue.enqueue('CS')
    self.__queue.enqueue('7')
    self.__queue.dequeue()
    self.assertEqual('[ 7 ]', str(self.__queue))

  def test_dequeue_with_two_return_value(self):
    self.__queue.enqueue('CS')
    self.__queue.enqueue('7')
    returned = self.__queue.dequeue()
    self.assertEqual('CS', returned)

  def test_dequeue_with_two_length(self):
    self.__queue.enqueue('CS')
    self.__queue.enqueue('7')
    self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

if __name__ == '__main__':
  unittest.main()

