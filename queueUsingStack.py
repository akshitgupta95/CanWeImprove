import stack

class Queue_using_stack():
    def __init__(self):
        self._stack1=stack.Stack()
    
    def enqueue(self, value):
        self._stack1.push(value)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp_stack=stack.Stack()
            while(self._stack1.isEmpty() is not True):
                temp_stack.push(self._stack1.pop())
            front=temp_stack.pop()
            while(temp_stack.isEmpty() is not True):
                self._stack1.push(temp_stack.pop())
            return front

    def isEmpty(self):
        return self._stack1.isEmpty()

    def is_empty(self):
        return self.isEmpty()
    
    def front(self):
        if self.isEmpty():
            return None
        temp_stack = stack.Stack()
        while not self._stack1.isEmpty():
            temp_stack.push(self._stack1.pop())
        front_val = temp_stack.pop()
        temp_stack.push(front_val)
        while not temp_stack.isEmpty():
            self._stack1.push(temp_stack.pop())
        return front_val
    
    def size(self):
        return self._stack1.size()


if __name__ == "__main__":
    my_data = Queue_using_stack()
    my_data.enqueue("5")
    my_data.enqueue(10)
    print("Size:", my_data.size())
    print("Dequeue:", my_data.dequeue())
    print("Is empty:", my_data.is_empty())
    # print("Front:", my_data.front())
   

  