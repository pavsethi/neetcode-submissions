class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = [0] * len(arr)
        for i in range(len(arr)):
            distances[i] = [abs(arr[i] - x), i]
        distances.sort()
        res = []
        l = 0
        while len(res) < k:
            res.append(arr[distances[l][1]])
            l += 1
        res.sort()
        return res
        