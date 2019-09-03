# author : YANG CUI
"""
Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""

def regularExpressionMatching(s, p):
    """
    this program implement regular expression matching with support for '.' and '*'.
    :param s: the input string
    :param p: the input pattern
    :return: True if p matches s, false otherwise.
    """
    # if both empty, return True
    if not p:
        return not s
    # for the current match to be true, the p[0] is equal to s[0] or p[0] == "."
    currentMatch = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2:
        lookAhead = p[1]
        # if met kleene star, either use 0 or 1 chars in s
        if lookAhead == "*":
            return (regularExpressionMatching(s, p[2:]) or (currentMatch and regularExpressionMatching(s[1:], p)))
        # else just compare the letter one by one
        else:
            return currentMatch and regularExpressionMatching(s[1:], p[1:])
    else:
        return currentMatch and regularExpressionMatching(s[1:], p[1:])






print(regularExpressionMatching("aab", "c*a*b"))
