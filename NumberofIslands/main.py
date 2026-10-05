 class Solution:
    def numIslands(self, grid:List[List[str]])-> int:
        if not grid:
            return 
        visit=set()
        from collections import deque
        q=deque()
        count=0
        rows=len(grid)
        cols=len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    q.append((r,c))
                    count+=1
                    while q:
                        row,col=q.popleft()
                        visit.add((row,col))
                        directions=[[0,1],[1,0],[-1,0],[0,-1]]
                        for dr,dc in directions:
                            r=row+dr 
                            c=col+dc 
                            if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit:
                                visit.add((r,c))
                                q.append((r,c))
        return count
