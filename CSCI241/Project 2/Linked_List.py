class Linked_List:

    class __Node:

        def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
            self.value = val
            self.next = None
            self.prev = None

    def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.prev = None
        self.__trailer.next = None
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
    # return the number of value-containing nodes in
    # this list.
    # TODO replace pass with your implementation
        return self.__size

    def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
        element = Linked_List.__Node(val)

        if self.__size == 0:
            self.__header.next = element
            element.prev = self.__header
            element.next = self.__trailer
            self.__trailer.prev = element
        else:
            element.next = self.__trailer
            self.__trailer.prev.next = element
            element.prev = self.__trailer.prev
            self.__trailer.prev = element
        self.__size += 1

    def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the
    # specified index. If the index is not a valid
    # position within the list, raise an IndexError
    # exception. This method cannot be used to add an
    # item at the tail position.
    # TODO replace pass with your implementation
        element = Linked_List.__Node(val)

        if index < 0 or index >= self.__size:
            raise IndexError

        if index <= self.__size//2:
            current = self.__header
            for i in range (0, index):
                current = current.next
            element.prev = current
            element.next = current.next
            current.next.prev = element
            current.next = element

        else:
            current = self.__trailer
            for i in range(self.__size, index, -1):
                current = current.prev
            element.prev = current.prev
            element.next = current
            current.prev.next = element
            current.prev = element

        self.__size += 1

    def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError

        if index <= self.__size//2:
            current = self.__header
            for i in range (index):
                current = current.next
            remove = current.next
            current.next = current.next.next
            current.next.prev = current


        else:
            current = self.__trailer
            for i in range(self.__size-1, index,-1):
                current = current.prev
            remove = current.prev
            current.prev = current.prev.prev
            current.prev.next = current



        self.__size = self.__size -1
        return remove.value



    def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError
        if index < (self.__size//2):
            current = self.__header.next
            for i in range(0, index):
                current = current.next
        else:
            current = self.__trailer.prev
            for i in range(self.__size-1, index, -1):
                current = current.prev
        return current.value

    def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # TODO replace pass with your implementation.
        if self.__size >0:
            current = self.__header.next
            current.prev = self.__trailer.prev
            self.__trailer.prev.next = current
            self.__trailer.prev = current
            self.__header.next = current.next
            current.next.prev = self.__header
            current.next = self.__trailer


    def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
        #current = self.__head
        if self.__size == 0:
            s = '[ ]'
            return s

        current = self.__header
        s = '[ '
        for i in range(self.__size-1):
            current = current.next
            v = current.value
            s = s + str(v) + ', '
        s = s + str(self.__trailer.prev.value)
        s = s + ' ]'
        return s

    def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
        self.__iterate = self.__header
        return self

    def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
        #if self.__iter_index == self.__size:
            #raise StopIteration
        #toreturn = self.get_element_at(self.__iter_index)

        if self.__iterate.next is self.__trailer:
            raise StopIteration
        to_return = self.__iterate.next.value
        self.__iterate = self.__iterate.next

        return to_return


if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
    a =Linked_List()
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #should failed
    print()
    print('Testing insert element into an empty Linked_List.')
    try:
        a.insert_element_at(8,0)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')
    print()

    #shoule work
    print('Testing append element into Linked_List.')
    a.append_element(2)
    a.append_element(3)
    a.append_element(4)
    a.append_element(5)
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #these should all work without error
    print()
    print('Testing insert element at a valid index.')
    try:
        a.insert_element_at(10,0)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.insert_element_at(-3,2)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.insert_element_at(7,5)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.insert_element_at(17,6)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

    except IndexError:
        print('Index is not valid.')

    #should fail, index invalid
    print()
    print('Testing insert element at an invalid index.')
    try:
        a.insert_element_at(10,-3)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    print()
    try:
        a.insert_element_at(10,9)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    print()
    try:
        a.insert_element_at(10,200)
    except IndexError:
        print('Index is not valid.')

    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #these should all work without error
    print()
    print('Testing get an element at a valid index.')
    try:
        print(a.get_element_at(0))
        print(a.get_element_at(7))
        print(a.get_element_at(3))
    except IndexError:
        print('Index is not valid.')

    #should falied, invalid index
    print()
    print('Testing get an element at an invalid index.')
    try:
        a.get_element_at(-3)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #should falied, invalid index
    print()
    try:
        a.get_element_at(8)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #should falied, invalid index
    print()
    try:
        a.get_element_at(100)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')


    #should work without error
    print()
    print('Testing rotate method.')
    try:
        a.rotate_left()
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #should failed, invalid index
    print()
    print('Testing remove an element from an invalid index.')
    try:
        a.remove_element_at(10)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #test interation
    print()
    print('Testing Iteration.')
    for val in a:
        print(str(val))

    #should work without error
    print()
    print('Testing remove an element from a valid index.')
    try:
        a.remove_element_at(0)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(6)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(3)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(4)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(2)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(0)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(0)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

        a.remove_element_at(0)
        print(a)
        print('Linked list has ' + str(len(a)) + ' elements')

    except IndexError:
        print('Index is not valid.')


    #should failed, invalid index
    print()
    print('Testing remove an element from an empty list.')
    try:
        a.remove_element_at(0)
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')

    #should print a empty list
    print()
    print('Testing rotate an empty Linked_List.')
    try:
        a.rotate_left()
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')


    print()
    print('Testing rotate an one element Linked_List.')
    a.append_element(3)
    try:
        a.rotate_left()
    except IndexError:
        print('Index is not valid.')
    print(a)
    print('Linked list has ' + str(len(a)) + ' elements')
