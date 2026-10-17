class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        # each index of freq is the bucket
        freq = {}
        count = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for n, cnt in freq.items():
            count[cnt].append(n)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res