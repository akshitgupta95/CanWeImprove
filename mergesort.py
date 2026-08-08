def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid=len(nums)//2
    left_sorted=mergeSort(nums[0:mid])
    right_sorted=mergeSort(nums[mid:len(nums)])
    return merge(left_sorted,right_sorted)

def merge(left, right):

    combined=[]
    start=0
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i+=1
        else:
            combined.append(right[j])
            j+=1

    while i<len(left):
        combined.append(left[i])
        i+=1
    while j<len(right):
        combined.append(right[j])
        j+=1
    return combined

if __name__=="__main__":
    print(mergeSort([38, 27, 43, 10]))


