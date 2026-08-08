from collections import deque


class LRUcache:
    def __init__(self,capacity):
        self.data=deque(maxlen=capacity)
        self.value_map={}
    
    def put(self, key, value):
        if(key in self.value_map): # use "in" search in hashmap O(1) access. 
            self.value_map[key]=value
            self.data.remove(key)
            self.data.append(key)
        else:
            if(len(self.data)+1>self.data.maxlen):
                del self.value_map[self.data[0]]
            self.data.append(key)
            self.value_map[key]=value
    
    def get(self,key):
        if key in self.value_map:
            value=self.value_map[key]
            self.data.remove(key)
            self.data.append(key)
            return value
        else:
            return -1

if __name__=="__main__":
    cache=LRUcache(2)
    cache.put(1,1)
    cache.put(2 ,2)
    print(cache.get(1))
    cache.put(3 ,3) 
    print(cache.get(2)) 
    cache.put(4 ,4) 
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    print(cache.value_map)
    
    