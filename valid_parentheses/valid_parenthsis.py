# author : YANG CUI
"""
This program determines if the given sequence of round brackets(of one type)
are valid.
"""

def isValid(inputString):
    """
    :param inputString: given sequnence of parentheses as a string
    :return: True if the sequence is a valid, False otherwise
    :complexity: O(n)
    """
    numOfOpeningParentheses = 0
    result = True
    for i in range(len(inputString)):
        if inputString[i] == "(":
            numOfOpeningParentheses += 1
        elif inputString[i] == ")":
            if numOfOpeningParentheses == 0:
                result = False
                return result
            elif numOfOpeningParentheses > 0:
                numOfOpeningParentheses -= 1
    if numOfOpeningParentheses != 0:
        result = False
    return result
