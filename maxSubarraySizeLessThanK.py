# Given an array of positive integers arr[] of size n, and an integer k. 
# The task is to find the maximum subarray size such that all subarrays of that size have sum less than or equals to k.
# INFO: The task is equal to: find the minimum subrray size such that all even one subrray of such size has sum greater than k 
# (using formal logic, applies to +ve numbers)
# Examples : 

# Input :  arr[] = [1, 2, 3, 4, i, j, k], k = 8.
# Output : 2
# Explanation: Following are the sum of subarray of size 1 to 4.

# Sum of subarrays of size 1: 1, 2, 3, 4. 
# Sum of subarrays of size 2: 3, 5, 7. 
# Sum of subarrays of size 3: 6, 9. 
# Sum of subarrays of size 4: 10. 
# So, maximum subarray size such that all subarrays of that size have the sum of elements less than 8 is 2.

# Input:  arr[] = [1, 2, 10, 4], k = 8. 
# Output : -1 
# Explanation: There is an array element (10) with value greater than k, so subarray sum cannot be less than k. 

# Input :  arr[] = [1, 2, 10, 4], k = 14 
# Output : 2

#BruteForce1
#size:for()
#indice :for(i=0,i<n,i++)
#window: for(i, i<windowSize, i++)

#bruteForce2:
#maxLength with contrainst = min of all at indice based subarray
#indice :for(i=0,i<n,i++)
#subarrayatIndice: for(j=i,j<n,j++)

#[1, 2, 3, 4, 1], k = 8       r=l+1...r, subarraySum=arr[r]+arr[r-1]...arr[l], find max r-l such that for all max(subarraysum)<=k
# preSum: [1,3,6,10,11], subarray sum = presum[r]-presum[l], find max(r - l), such that max(presum[r]-presum[l])<=k 


def minK(arr,k):

    preSum=[arr[0]]
    for i in range(1,len(arr)):
        preSum.append(preSum[i-1]+arr[i])

    minSoFar=len(arr)
    start=0
    maxsoFar=0
    for end in range(len(preSum)-1,0,-1):
        if(end!=start):
            subSum=preSum[end]-preSum[start]
        else:
            subSum=preSum[end]
        maxsoFar=end-start+1
        while subSum>k:
            start+=1
            if(end!=start):
                subSum=preSum[end]-preSum[start]
            else:
                subSum=preSum[end]
                break
            maxsoFar=end-start+1
        minSoFar=max(minSoFar, maxsoFar)
    
    return minSoFar

if __name__=="__main__":
    print(minK([1, 2, 3, 4,], 8))








