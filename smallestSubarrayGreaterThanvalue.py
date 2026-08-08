# Smallest subarray with sum greater than a given value
# Given an array arr[] of integers and a number x, the task is to find the smallest subarray with a sum strictly greater than x.

# Examples:

# Input: x = 51, arr[] = [1, -1, 4, 45, 4, 6, 19]
# Output: 3
# Explanation: Minimum length subarray is [4, 45, 6]

# Input: x = 100, arr[] = [1, 10, 5, 2, 7]
# Output: 0
# Explanation: No subarray exist

def findsmallSubarray(nums, value):
    start=0
    end=0
    min_length=len(nums)
    sum_so_far=0

    for end in range(len(nums)):
        sum_so_far+=nums[end]

        while sum_so_far>value:
            min_length=min(min_length, end-start+1)
            sum_so_far-=nums[start]
            start+=1

    return min_length


if __name__=="__main__":
    print(findsmallSubarray( [1, 2, 3, -10, 50], 41))

