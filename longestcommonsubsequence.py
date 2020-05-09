# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some
# characters(can be none) deleted without changing the relative order of the remaining
# characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common
# subsequence of two strings is a subsequence that is common to both strings.
#
#
# # If there is no common subsequence, return 0.
#
# Time complexity: O(mn) and Space complexity: O(mn)


def longestCommonSubsequence(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # making 2D aray

    for row in range(1, m + 1):  # iterating through rows
        for col in range(1, n + 1):  # iterating through columns
            if s1[row - 1] == s2[col - 1]:
                memo[row][col] = 1 + memo[row - 1][col - 1]
            else:
                memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

    return memo[m][n]


print(longestCommonSubsequence("abcdefg", "xyzcde123"))
