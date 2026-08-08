

def quickSelect(nums,k):
    if len(nums) == 1: return nums[0]
    pivot=nums[0]
    left=[num for num in nums if num<pivot]
    mid=[num for num in nums if num==pivot]
    right=[num for num in nums if num>pivot]
    if k<len(left):
        return quickSelect(left,k)
    elif k<len(left)+len(mid):
        return pivot
    else:
        return quickSelect(right,k-len(left)-len(mid))

if __name__=="__main__":
    print(quickSelect([38, 27, 43, 10, 1, 2, 3,2],5))


