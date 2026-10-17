class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freqList = []
        for n, cnt in freq.items():
            freqList.append([cnt, n])
        
        freqList.sort()
        # print(freqList)

        ret = []
        l = len(freqList) - 1
        while len(ret) < k:
            ret.append(freqList[l][1])
            l -= 1
        return ret