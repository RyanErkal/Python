# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Just to explain the parts of the formatting string:
#
# {} places a variable into a string
# 0 takes the variable at argument position 0
# : adds formatting options for this variable (otherwise it would represent decimal 6)
# 08 formats the number to eight digits zero-padded on the left
# b converts the number to its binary representation

# If you're using a version of Python 3.6 or above, you can also use f-strings:


def rangeBitwiseAnd(m, n):
    i = 0
    while m != n:
        m >>= 1  # shift bits right
        n >>= 1  # shift bits left
        i += 1
    return n << i


print(rangeBitwiseAnd(5, 7))
