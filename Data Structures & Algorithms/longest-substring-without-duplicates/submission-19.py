class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        maxLen = 0
        while r <= len(s) - 1:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1
            maxLen = max(len(seen), maxLen)
        return maxLen