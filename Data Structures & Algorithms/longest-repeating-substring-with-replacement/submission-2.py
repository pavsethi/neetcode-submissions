class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            windowLen = r - l + 1
            if windowLen - max(freq.values()) <= k:
                res = max(windowLen, res)
            else:
                freq[s[l]] -= 1
                l += 1
        return res