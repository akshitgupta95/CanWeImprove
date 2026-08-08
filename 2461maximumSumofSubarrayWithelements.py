# Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k.

# Input  : arr[] = [5, 2, -1, 0, 3], k = 3
# Output : 6
# Explanation : We get maximum sum by considering the subaarray [5, 2 , -1]

# Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
# Output : 39
# Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.
# All elements in array need to be unique

def maximumSubarraySum(nums, k: int):
    running_sum=0
    max_so_far=0
    elements_in_subarray={}

    for i in range(0,k):
        running_sum+=nums[i]
        elements_in_subarray[nums[i]]=elements_in_subarray.get(nums[i],0)+1
    if len(elements_in_subarray) == k:
        max_so_far=running_sum

    for i in range(k,len(nums)):
        running_sum= running_sum + nums[i] - nums[i-k]
        elements_in_subarray[nums[i]]=elements_in_subarray.get(nums[i],0)+1
        elements_in_subarray[nums[i-k]]-=1
        if(elements_in_subarray[nums[i-k]]==0):
            del elements_in_subarray[nums[i-k]]

        if running_sum > max_so_far:
            if len(elements_in_subarray)==k:
                max_so_far=running_sum

    return max_so_far

if __name__ == "__main__":
    print(maximumSubarraySum([10, 10, 10, 1, 2, 3],3))
