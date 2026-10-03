class Solution:
    def schedule(self,numCourses:int,prereq:List[List[int]])->bool:
        adjList=[[] for _ in range(numCourses)]
        indegree=[0 for _ in range(numCourses)]
        for u,v in range(prereq):
            adjList[u].append(v)
            indegree[v]+=1
        q=collections.deque()
        stack=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            curr=q.popleft()
            stack.append(curr)
            for i in adjList[curr]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return len(stack)==numCourses

