# author:  YANG CUI
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
def isSameType(bracket1, bracket2):
    if bracket1 == "(":
        if bracket2 == ")":
            return True
        else:
            return False
    elif bracket1 == "[":
        if bracket2 == "]":
            return True
        else:
            return False
    elif bracket1 == "{":
        if bracket2 == "}":
            return True
        else:
            return False

def isOpeningBracket(bracket):
    if bracket in ("(", "{", "["):
        return True
    else:
        False

def isClosingBracket(bracket):
    if bracket in (")", "}", "]"):
        return True
    else:
        False

def valid_parentheses(inputs):
    """
    :param inputString: given sequnence of parentheses as a string
    :return: True if the sequence is a valid, False otherwise
    :complexity: O(n) a stack approach
    """
    result = True
    current = 0
    stack = []
    for i in range(len(inputs)):
        if isOpeningBracket(inputs[i]):
            stack.insert(0, inputs[i])
        else:
            if isClosingBracket(inputs[i]):
                if len(stack) == 0:
                    result = False
                    return result

                elif len(stack) > 0:
                    if isSameType(stack[0], inputs[i]):
                       stack.__delitem__(0)
                    else:
                        result = False
                        return result
    if stack == []:
        return result
    else:
        result = False
        return result



print(valid_parentheses("()"))


