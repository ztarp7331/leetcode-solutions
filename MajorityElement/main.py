class Solution:
    def majorityElement(self,nums:List[int])->int:
        candidate=None 
        count=0
        for i in range(len(nums)):
            if candidate==None:
                candidate=nums[i]
                count+=1
            elif candidate==nums[i]:
                count+=1
            else:
                count-=1
                if count==0:
                    candidate=None 
        return candidate
