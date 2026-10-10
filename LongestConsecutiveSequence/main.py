class solution:
    def LCS(self,nums:List[int])->int:
        visit=set(nums)
        count=0
        for i in visit:
            score=0
            if i-1 in visit:
                continue
            prev=i+1 
            score+=1 
            while prev in visit:
                score+=i 
                prev+=1 
            count=max(count,score)
        return count 
