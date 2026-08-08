# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , 
# return the elements in the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. 
# The intersection should not count duplicate elements and the result should contain items in sorted order.

# Examples:

# Input: a[] = [1, 1, 2, 2, 2, 4], b[] = [ 2, 4, 4]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.



# Input: a[] = [1, 2], b[] = [3, 4]
# Output: []
# Explanation: No common elements.

# Input: a[] = [1, 2, 3], b[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation: All elements are common

def intersection(arr1, arr2):
    ptr1=0
    ptr2=0
    commonElements=[]

    for ptr1 in range(len(arr1)):
        while ptr2<len(arr2) and arr2[ptr2]<arr1[ptr1] :
            ptr2+=1
        if(ptr2>=len(arr2)):
            break
        if(arr1[ptr1]==arr2[ptr2]):
            commonElements.append(arr1[ptr1])
            ptr2+=1
        
      
    return commonElements

def intersectioneasy(arr1, arr2):
    ptr1=0
    ptr2=0
    commonElements=[]

    while ptr1<len(arr1) and ptr2<len(arr2) :
        if(arr1[ptr1]==arr2[ptr2]):
            commonElements.append(arr1[ptr1])
            ptr1+=1
            ptr2+=1
        elif arr2[ptr2]<arr1[ptr1]:
            ptr2+=1
        else:
            ptr1+=1
      
    return commonElements


if __name__=="__main__":
    print(intersection([5],[ 1,2]))

