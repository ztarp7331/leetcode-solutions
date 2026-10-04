class Solution: 
    def scheduledCourses(self, courses :List[List[int]])->int:
        courses.sort(key=lambda x: x[1])
        heap=[]
        maxTime=0
        for dureation,deadline in courses:
            heapq.heappush_max(heap,dureation)
            maxTime+=dureation
            if maxTime>deadline:
                biggestTime=heapq.heappop_max(heap)
                maxTime-=biggestTime
        return len(heap)

