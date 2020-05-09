# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log(m + n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    new_list = (nums1 + nums2)
    new_list.sort()

    if len(new_list) % 2 == 1:
        m = new_list[int(len(new_list) / 2)]
        return float(m)
    else:
        m = new_list[int(len(new_list) / 2)]
        n = new_list[int((len(new_list) / 2) - 1)]
        return float(m + n) / 2


print(findMedianSortedArrays(
    [1, 1, 99, 2, 34, 5, 4, 1, 3, 5, 4], [2, 4, 3, 1, 43, 32, 12, 3]))
