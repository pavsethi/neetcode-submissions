class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        counts = []
        for n, cnt in freq.items():
            counts.append([cnt, n])

        counts.sort()
        res = []
        while len(res) < k:
            res.append(counts.pop()[1])
        return res