# Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
# Note: A subarray is a continuous part of an array.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

def maxSumSubarray(arr):
    current_sum=arr[0]
    max_so_far=arr[0]
    indices=[]
    indices.append(0)
    indices.append(0)
    indices.append(0)
    start=0
    end=0


    for i in range(1,len(arr)):
        current_sum=current_sum+arr[i]
        if(current_sum>=0):
            if(max_so_far<current_sum):
                max_so_far=current_sum
                indices[1]=i
                end=i
                indices[0]=indices[2]

                
        else:
            current_sum=0
            indices[2]=i+1
            start=i+1
    
    return max_so_far, indices[0:2], (start,end)


if __name__=="__main__":
    print(maxSumSubarray([-2, -5, 6, -2, -3, 1, 5, -6]))
    print(maxSumSubarray([-2, -4,-6]))
    print(maxSumSubarray([5, 4, 1, 7, 8]))
