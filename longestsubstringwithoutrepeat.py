# 3. Longest Substring Without Repeating Characters
# Medium

# Topics
# premium lock icon
# Companies

# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcacbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longestsubstring(str):
    characters=list(str)
    start=0
    end=0
    dict={}
    max_length=0

    for end in range(len(characters)):
        dict[characters[end]]=dict.get(characters[end],0)+1
        while(dict[characters[end]]>1):
            dict[characters[start]]-=1
            if(dict[characters[start]]==0):
                del dict[characters[start]]
            start+=1

        max_length=max(max_length, end-start+1)
    return max_length

if __name__=="__main__":
    print(longestsubstring("abcdefabcbb"))