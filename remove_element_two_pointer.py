# author: YANG CUI
"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

def removeElement(nums, val):
    numberOfElementsAfter = 0
    count = 0
    while count < len(nums):
        if nums[count] != val:
            nums[numberOfElementsAfter] = nums[count]
            numberOfElementsAfter += 1
        count += 1
    return numberOfElementsAfter

print(removeElement([0,1,2,2,3,0,4,2], 2))