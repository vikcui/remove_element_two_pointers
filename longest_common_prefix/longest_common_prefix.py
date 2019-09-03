# author: YANG CUI
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):
    # length of the input strs array
    strsLen = len(strs)
    if strsLen == 0:
        return ""
    # initialize the number of chars we have to check at most to be +inf
    minLen = float('inf')
    # compute the number of chars we have to check at most
    for i in range(strsLen):
        if len(strs[i]) < minLen:
            minLen = len(strs[i])
    # longest common prefix index
    lcpIndex = 0
    # loop thru each word minLen number of times to calculate the longest common prefix
    i = 0
    # flag helps decides whether or not to increment lcpIndex
    flagIncrement = True
    while i < minLen:
        j = 0
        while j < strsLen-1:
            if strs[j][i] != strs[j+1][i]:
                j = strsLen
                i = minLen + 1
                flagIncrement = False
            j = j + 1
        i = i + 1
        if flagIncrement == True:
            lcpIndex = lcpIndex + 1
        else:
            flagIncrement = True
    if lcpIndex == 0:
        return ""
    else:
        return strs[0][:lcpIndex]

# print(longestCommonPrefix(["dog","racecar","car"]))