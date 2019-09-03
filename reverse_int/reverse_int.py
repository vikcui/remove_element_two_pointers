# author : YANG CUI
# Given a 32-bit signed integer, reverse digits of an integer.
import sys

def reverse(num):
    neg_input = False
    if num <= 0:
        neg_input = True
        num = abs(num)
    rev = 0
    while num != 0 :
        pop = num % 10
        num = num // 10
        rev = rev * 10 + pop

    if rev >= 2 ** 31 - 1 or rev <= -2 ** 31:
        return 0

    if neg_input:
        return -rev
    else:
        return rev

