class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
         return 0

        starts = []
        ends = []
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        
        starts.sort()
        ends.sort()

        s=e=0
        room = 0
        maxroom = 0
        while s<len(starts):
         if starts[s] >= ends[e]:
           room-=1
           e+=1
         else:
            s+=1
            room+=1 
            maxroom = max(room,maxroom)   

        return maxroom              


        