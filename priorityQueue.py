from collections import deque
import heapq

class PriorityQueue():
  def __init__(self):
    self._data=[]
    self._length=0

  def enqueue(self, key, value):
    heapq.heappush(self._data, (key, value))
    self._length += 1

  def dequeue(self):
    if(self.is_empty()):
      raise Exception("PQ is empty")
    else:
      self._length -= 1
      return heapq.heappop(self._data)

  def front(self):
    return self._data[0][-1]

  def is_empty(self):
    if len(self._data)==0:
        return True 
    else:
      return False

  def size(self):
    if(self.is_empty()):
      return 0
    else:
      return self._length

if __name__ == "__main__":
    pq=PriorityQueue()
    pq.enqueue(10, "world")
    pq.enqueue(1, "hello")
    # pq.dequeue()
    print(pq.front())