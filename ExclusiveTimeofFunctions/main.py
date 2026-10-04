class Solution:
    def exclusiveFn(self, n:int,log:List[str])->List[int]:
        res=[0]*n 
        prevStamp=0
        stack=[]
        for log in logs:
            fniD,status,stamp=log.split(':')
            fniD=int(fniD)
            stamp=int(stamp)
            if status=="start":
                if stack:
                    res[stack[-1]]+=stamp-prevStamp
                stack.append(fniD)
                prev=stamp
            else:
                doneId=stack.pop()
                res[doneId]+=stamp-prevStamp
                prevStamp=stamp+1
        return res 

