# Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) such that their sum is equal to the target.

# Illustration : 

# Input: arr[] = [10, 20, 35, 50], target =70
# Output:  true
# Explanation : There is a pair (20, 50) with given target.

# Input: arr[] = [10, 20, 30], target =70
# Output :  false
# Explanation : There is no pair with sum 70

# Input: arr[] = [-8, 1, 4, 6, 10, 45], target = 16
# Output: true
# Explanation : There is a pair (6, 10) with given target.

def getTarget(arr, target):
    left=0
    right=len(arr)-1
    ans=[]

    while(left<right):
        sum=arr[left]+arr[right]
        if sum==target:
            ans.append(left)
            ans.append(right)
            return ans
        if sum<target:
            left+=1
        else:
            right-=1
    return False

if __name__=="__main__":
    print(getTarget([-3, -1, 0, 1, 2], -2))
    print(getTarget([2,7,11,15], 9))