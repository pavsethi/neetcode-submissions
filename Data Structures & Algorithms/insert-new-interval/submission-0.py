class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = [intervals[0]]
        for s, e in intervals[1:]:
            prevEnd = ret[-1][1]
            if s <= prevEnd:
                ret[-1][1] = max(e, prevEnd)
            else:
                ret.append([s, e])
        return ret