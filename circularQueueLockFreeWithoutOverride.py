
BUFFER_SIZE=4

class CircularQueueLockFree():
    def __init__(self):
        self.data=[None]*BUFFER_SIZE
        self.tail=0
        self.head=0
        
    
    def enqueue(self, item):
        if(self.is_full()):
            raise IndexError("queue is full")
        else:
            self.data[self.tail%BUFFER_SIZE]=item
            self.tail = (self.tail+1)
    

    def dequeue(self):
        if(self.size()==0):
             raise IndexError("queue is empty")
        else:
            item=self.data[self.head%BUFFER_SIZE]
            self.head = (self.head+1)
            return item

    def is_full(self):
        if self.size()==BUFFER_SIZE:
           return True
        else:
            return False

    def size(self):
        return (self.tail-self.head)

    