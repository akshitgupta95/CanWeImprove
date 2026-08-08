
BUFFER_SIZE=8

 


def modulo(item, BUFFER_SIZE):
    return item & (BUFFER_SIZE-1)    
    
class CircularQueue:
    def __init__(self):
        self.data=[None]*BUFFER_SIZE
        self.head=0
        self.tail=0
        self.length=0
    
    def push(self, item):
        if(self.isFull()):
            self.head=(self.head+1) % BUFFER_SIZE
            self.length-=1
        self.data[self.tail]=item
        self.tail = (self.tail+1)% BUFFER_SIZE
        self.length+= 1
       

    def pop(self):
        if(self.isEmpty()):
            return None
        item= self.data[self.head]
        self.data[self.head]=None
        self.head = (self.head+1) % BUFFER_SIZE
        self.length-= 1
        return item

    def front(self):
        if(not self.isEmpty()):
            return self.data[self.head]
        else:
            return None

    def isFull(self):
        return self.length>=BUFFER_SIZE
    
    def isEmpty(self):
        return self.length==0
