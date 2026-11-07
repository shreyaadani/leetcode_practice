class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0]*26
        for t in tasks:
            freq[ord(t)-ord('A')] += 1

        #max heap 
        pq = [-f for f in freq if f>0]
        heapq.heapify(pq)

        time = 0
        while pq:
            cycle = n+1
            store = []
            taskcnt = 0

            while cycle > 0 and pq:
                curr = -heapq.heappop(pq)
                if curr > 1:
                    store.append(-(curr - 1))
                taskcnt += 1
                cycle -= 1

            for x in store:
                heapq.heappush(pq,x)

            time += taskcnt if not pq else n+1        

        return time        

        