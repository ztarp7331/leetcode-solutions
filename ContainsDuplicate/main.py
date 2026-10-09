class Solution:
    def containsDuplicate(self,nums:List[int])--> bool:
        #O(n) Space Complexity
        visit=set()
        for i in nums:
            if i in visit:
                return True 
        return False 
        

        #O(1) Space Complexity
        nums.sort()
        prev=0
        for i in range(1,len(nums)):
            if nums[prev]==nums[i]:
                return True 
            prev+=1
        return False
