class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the list
        # go through intervals
        # check if interval.start <= prevInterval.end:
        #   if it is: merge
        # else: add interval to list

        intervals.sort()
        merged = [intervals[0]]
        for s, e in intervals[1:]:
            prevEnd = merged[-1][1]
            if s <= prevEnd:
                merged[-1][1] = max(prevEnd, e)
            else:
                merged.append([s, e])
        return merged