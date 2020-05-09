# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:

    def lengthOfLongestSubstring(self, string):
        """
        Time:  O(n)
        Space: O(k)
        [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
                print(left, right, longest)
            else:
                chars.remove(string[left])
                left += 1
                print(left, right, longest)
        return longest


x = Solution()
print(x.lengthOfLongestSubstring("aabb123456"))
