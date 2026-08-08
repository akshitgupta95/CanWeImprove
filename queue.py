from collections import deque

class Queue():
  def __init__(self):
    self._data=deque()

  def enqueue(self, item):
    self._data.append(item)

  def dequeue(self):
    return self._data.popleft()

  def front(self):
    return self._data[0]

  def is_empty(self):
    return len(self._data) == 0

  def size(self):
    return len(self._data)


if __name__== "__main__":
  my_data=Queue()
  my_data.enqueue("5")
  my_data.enqueue(10)
  print(my_data.size())
  print(my_data.dequeue())
  print(my_data.is_empty())
  print(my_data.front())