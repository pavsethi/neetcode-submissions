class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        seen = set(nums)

        for n in seen:
            if (n - 1) not in seen:
                length = 0
                while (n + length) in seen:
                    length += 1
                maxLen = max(length, maxLen)
                    
        return maxLen