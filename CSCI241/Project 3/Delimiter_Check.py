import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

  
  check = Stack()
  with open (filename,'r') as delimiters:
    line = delimiters.read()
  for i in line:
    if i == '(' or i == '[' or i =='{':
      check.push(i)

    if i == ')':
      if check.peek() == '(':
        check.pop()
      else:
        return False
    if i == ']':
      if check.peek() == '[':
        check.pop()
      else:
        return False
    if i == '}':
      if check.peek() == '{':
        check.pop()
      else:
        return False
  if len(check) == 0:
    return True

  


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')

