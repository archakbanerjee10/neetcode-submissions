class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        erasecount = 0
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start < output[-1][1]:
                # Overlap! Keep the interval with the smaller end time to leave room for future intervals
                output[-1][1] = min(output[-1][1], end)
                erasecount += 1
            else:
                # No overlap
                output.append([start, end])

        return erasecount