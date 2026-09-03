class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start, end = intervals[0]

        for i in intervals[1:]:
            s,e = i
            if s<=end:
                end = max(e,end)
            else:
                res.append([start,end])
                start = s
                end = e  
        res.append([start,end])


        return res          