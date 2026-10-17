class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals by start value
        intervals.sort()
        ret = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = ret[-1][1]
            if start <= prevEnd:
                #overlap
                ret[-1][1] = max(prevEnd, end)
            else:
                ret.append([start, end])
        return ret
