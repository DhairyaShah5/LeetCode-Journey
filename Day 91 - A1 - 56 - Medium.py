class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])  
        mergedIntervals = [intervals[0]]

        for intervalStart, intervalEnd in intervals:
            lastMergedEnd = mergedIntervals[-1][1]

            if intervalStart <= lastMergedEnd:
                mergedIntervals[-1][1] = max(lastMergedEnd, intervalEnd)
            else:
                mergedIntervals.append([intervalStart, intervalEnd])

        return mergedIntervals