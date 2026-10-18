class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x, y = points[i]
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(distances, [distance, i])

        ret = []
        for _ in range(k):
            dist, i = heapq.heappop(distances)
            ret.append(points[i])
        return ret
        