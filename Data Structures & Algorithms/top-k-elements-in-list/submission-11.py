class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        counts = []
        for n, cnt in freq.items():
            counts.append([cnt, n])

        counts.sort()
        res = []
        i = len(counts) - 1
        while len(res) < k:
            res.append(counts[i][1])
            i -= 1
        return res