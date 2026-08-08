# Majority Element
# Last Updated :
# 28 Mar, 2026
# Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times. If no such element exists, return -1.

# Examples:

# Input: arr[] = [1, 1, 1,1, 2, 1, 2, 2, 2] [1,2,3,1,1,4,1,6,1]
# Output: 1
# Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

# Input: arr[] = [7]
# Output: 7
# Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

# Input: arr[] = [2, 13]
# Output: -1
# Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.

def find_majority(arr):
    dict={}
    for i in range(len(arr)):
        dict[arr[i]]=dict.get(arr[i],0)+1
    for key in dict:
        if dict[key]>len(arr)//2:
            return True
    return False



if __name__=="__main__":
    print(find_majority([1] ))
        