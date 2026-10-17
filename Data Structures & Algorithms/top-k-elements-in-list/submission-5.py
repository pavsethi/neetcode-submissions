class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        heap = []
        for n in freq.keys():
            heapq.heappush(heap, (freq[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res