class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        for s, e in intervals[1:]:
            prevEnd = ret[-1][1]
            if s <= prevEnd:
                #overlap
                ret[-1][1] = max(e, prevEnd)
            else:
                ret.append([s, e])
        return ret
            