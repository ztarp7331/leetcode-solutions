class Solution:
    def render(self, numCourse:int, prereq:[List[int]])->List[int]:
        # So similar to Course Schedule-I but just need to print out the stack[::-1]
        adjList=[[]for _ in range(numCourse)]
        indegree=[0 for _ in range(numCourse)]
        for u,v in prereq:
            adjList[u].append(v)
            indegree[v]+=1
        q=collections.deque()
        stack=[]
        for i in range(numCourse):
            if indegree[i]==0:
                q.append(i)
        while q:
            curr=q.popleft()
            stack.append(curr)
            for i in adjList[curr]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(stack)==numCourse:
            return stack[::-1] 
        else:
            return -1
