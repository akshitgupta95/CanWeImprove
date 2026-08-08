# Given a string s of length n consisting of uppercase English letters and an integer k, 
# you are allowed to perform at most k operations.  
# In each operation, you can change any character of the string to any other uppercase English letter.

# Determine the length of the longest substring that can be transformed into a string with all identical characters 
# after performing at most k such operations.

# Examples:

# Input: s = "ABBABB", k = 2 
# Output: 4 
# Explanation: The string "ABBAB" can be fully converted into the same character using at most 2 changes. 
# By replacing both 'A' with 'B', it becomes "BBBB". Hence, the maximum length is 4.
# Input: s = "AsDBDe", k = 1
# Output: 3
# Explanation: In the string "ADBD", we can make at most 1 change. 
# By changing 'B' to 'D', the string becomes "ADDD", which contains a substring "DDD" of length 3.


def longestStringIdentical(str,k):
    chars=list(str)
    start=0
    max_length=0
    max_so_far=0
    currentChar=str[start]
    frequencyMap={currentChar:1}
    count=k
    max_freq=1

    for end in range(1,len(str)):
        
        frequencyMap[chars[end]]=frequencyMap.get(chars[end],0)+1
        
        for key,value in frequencyMap.items():
            if(value>=max_freq):
                max_freq=frequencyMap[key]
                # currentChar=key

        while (end-start+1) -max_freq>k:
           
            frequencyMap[chars[start]]-=1
            if(frequencyMap[chars[start]]==0):
                del frequencyMap[chars[start]]
            start+=1

        max_length=max(max_length,end-start+1)

    return max_length

if __name__=="__main__":
    print(longestStringIdentical("ADBDDD",1))
