# Description

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee((t)(c)ode"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a(b(c)d)))"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(( ()"
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.

# w(r)it((t()e))n

def minRemoveToMakeValid( s: str) -> str:
    open = "("
    close = ")"
    s=list(s)
    indicesOpening=[]
    indicesClosing=[]

    for i,char in enumerate(s):
        if char in open:
            indicesOpening.append(i)
        if char in close:
            if(len(indicesOpening)>0):
                indicesOpening.pop()
                # indicesClosing.append(i)
            else:
                indicesClosing.append(i)
    for i in indicesClosing:
        s[i]=""
    for i in indicesOpening:
        s[i]=""

    return "".join(s)


if __name__=="__main__":
    print(minRemoveToMakeValid("))()(("))