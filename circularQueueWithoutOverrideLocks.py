
import threading

BUFFER_SIZE=4

class CircularQueueWithOverride():
    def __init__(self):
        self.data=[None]*BUFFER_SIZE
        self.tail=0
        self.head=0
        self.count=0
        self.lock=threading.Lock()
        self.available_space_cv=threading.Condition(self.lock)
        self.data_consume=threading.Condition(self.lock)

    
    def enqueue(self, item):
        with self.available_space_cv:
            while(self.is_full()):
                self.available_space_cv.wait()

            # if self.tail == self.head and self.count!=0 :
            #     self.head = (self.head+1)%BUFFER_SIZE
            #     self.count -=1
            self.data[self.tail]=item
            self.tail = (self.tail+1)%BUFFER_SIZE
            self.count+=1
            self.data_consume.notify()


    def dequeue(self):
        with self.data_consume:
            while(self.count==0):
                self.data_consume.wait()

            item=self.data[self.head]
            self.head = (self.head+1)%BUFFER_SIZE
            self.count-=1
            self.available_space_cv.notify()
            return item

    def is_full(self):
        if(self.count!=0 and self.head==self.tail):
           return True
        else:
            return False

    def size(self):
        return self.count

    