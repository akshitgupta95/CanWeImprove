from collections import deque

class Stack():
  def __init__(self):
    self._data=deque()
    

  def enqueue(self, item):
    self._data.append(item)

  def dequeue(self):
    return self._data.pop()

  def front(self):
    return self._data[-1]

  def is_empty(self):
    if len(self._data) == 0:
      return True 
    return False

  def size(self):
    if(self.is_empty()):
      return 0
    else:
      return len(self._data)

if __name__== "__main__":
  my_data=Stack()
  my_data.enqueue(5)
  my_data.enqueue(10)
  print(my_data.size())
  print(my_data.dequeue())
  print(my_data.is_empty())
  print(my_data.front())