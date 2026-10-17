class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            windowLen = r - l + 1
            if windowLen - max(freq.values()) <= k:
                maxLen = max(maxLen, windowLen)
            else:
                freq[s[l]] -= 1
                l += 1
        return maxLen