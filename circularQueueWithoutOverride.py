
BUFFER_SIZE=4

class CircularQueue():
    def __init__(self):
        self.data=[None]*BUFFER_SIZE
        self.tail=0
        self.head=0
        self.count=0
    
    def enqueue(self, item):
        if(self.is_full()):
            return "queue is full"
        else:
            self.data[self.tail]=item
            self.tail = (self.tail+1)%BUFFER_SIZE 
            self.count+=1

    def dequeue(self):
        if(self.count==0):
            return "queue is Empty"
        else:
            item=self.data[self.head]
            self.head = (self.head+1)%BUFFER_SIZE
            self.count-=1 
            return item

    def is_full(self):
        if(self.count!=0 and self.head==self.tail):
           return True
        else:
            return False

    def size(self):
        return self.count

    