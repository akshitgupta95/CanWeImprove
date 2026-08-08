# Given a binary array arr[] and an integer k, 
# find the maximum length of a subarray containing all ones after flipping at most k zeroes to 1's.

# Examples: 

# Input: arr[] = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], k = 2
# Output: 8
# Explanation: By flipping the zeroes at index 5 and 7, we get the longest subarray from index 3 to 10 containing all 1's.

# Input: arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
# Output: 5 
# Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1's.
# Try It Yourself

def maxOnescorrectsolution(nums, k):
    start=0
    end=0
    max_so_far=0
    max_length=0
    count=k

    for i in range(len(nums)):
        if(nums[i]==0):
            count-=1
        end=i
        while count<0:
            if start <=end:
                if(nums[start]==0):
                    count+=1
            start+=1

        max_so_far=end-start+1
        max_length=max(max_length, max_so_far)

    return max_length


def maxOnes(nums,k):
    count=k
    max_length=0
    max_so_far=0
    addition=0

    for i in range(len(nums)):
        if(count>=0):
            
            if(nums[i]==0):
                count-=1
            if(nums[i]==1 and count==0):
                addition+=1
            if(count<0):
                max_so_far-=1
            max_so_far+=1
            if(max_length<max_so_far):
                max_length=max_so_far      
        else:
            count=k-1
            max_so_far=addition+2
            
            addition=0

    return max_length

    

if __name__=="__main__":
    print(maxOnescorrectsolution([1, 0, 0, 1, 0, 1], 1))
            

    

