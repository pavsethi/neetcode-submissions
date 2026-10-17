class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            windowLen = r - l + 1
            if windowLen - max(count.values()) <= k:
                res = max(res, windowLen)
            else:
                count[s[l]] -= 1
                l += 1
        return res