# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 

# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

# Constraints:

# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

# inputs: window size, stream
# 1,2,3
# avg=sum/3
# moving_avg=((N-1)*avg + new_num)/(N)

from collections import deque

# 1 10 3 5 10 15 20 30

# space O(k), time 0(1)

class MovingAverage():
    def __init__(self,size):
        self.data=[0]*size
        self.size=size
        self.index=0
        self.cache=0
    
    def next(self,item):
        self.cache =self.cache+item
        self.cache=self.cache-self.data[self.index%self.size]
        self.data[self.index%self.size]=item
        self.index = (self.index+1)
        if self.index<self.size:
            return self.cache/self.index
        else:
            return self.cache/self.size
# 1 10 3 5 10 15 20 30
class MovingAverageUsingDeque():
    def __init__(self,size):
        self.data=deque(maxlen=size)
        self.size=size
        self.cache=0
    
    def next(self,item):
        if(len(self.data)==self.size):
            self.cache=self.cache+item-self.data[0]
        else:
            self.cache=self.cache+item
        self.data.append(item)
        return self.cache/len(self.data)

if __name__== "__main__":
    test=MovingAverageUsingDeque(3)
    print(test.next(1))
    print(test.next(10))
    print(test.next(3))
    print(test.next(5))


    
    
    

