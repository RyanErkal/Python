# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

import collections


def subarraySum(A, K):
    count = collections.Counter()
    count[0] = 1
    ans = su = 0
    for x in A:
        su += x
        ans += count[su - K]
        count[su] += 1
    return ans


print(subarraySum([1, 1, 1], 2))
