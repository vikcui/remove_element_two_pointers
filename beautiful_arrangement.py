# author : YANG CUI
"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is
constructed by these N numbers successfully if one of the following is true for the ith position
(1 <= i <= N) in this array:
    1. The number at the ith position is divisible by i.
    2. i is divisible by the number at the ith position.

This file returns the number of beautiful arrangments an array has given the size of that array.
"""

def beautiful_arrangement_aux(n):
    # number of arrangments
    numberOfArrangement = 0
    #visited array to indicate whether a num is used already
    visited = [0] * n
    result = [0] * n
    return beautiful_arrangement(n,result,visited,numberOfArrangement)

def beautiful_arrangement(n,result,visited,numberOfArrangement):
    if check_arrangement(n,visited):
        numberOfArrangement += 1
        return
    







def check_arrangement(n,visited):
    for i in range(n):
        if i == 0:
            if visited[i] != 0:
                return False
        else:
            if visited[i] != 1:
                return False
    return True








