class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        if not intervals:
            return [newInterval]
        elif newInterval[0] < intervals[0][0]:
            inserted.append(newInterval)
            inserted.extend(intervals)
        else:
            inserted = [intervals[0]]
            for s, e in intervals[1:]:
                if inserted[-1][0] <= newInterval[0] <= s:
                    inserted.append(newInterval)
                inserted.append([s,e])
        if len(inserted) == len(intervals):
            # value needs to be inserted at the end
            inserted.append(newInterval)

        ret = [inserted[0]]
        for s, e in inserted[1:]:
            prevEnd = ret[-1][1]
            if s <= prevEnd:
                ret[-1][1] = max(e, prevEnd)
            else:
                ret.append([s,e])
        return ret
        
        