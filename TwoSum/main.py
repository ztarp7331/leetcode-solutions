class solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        visit={""""numsValue:numsIndex"""}
        for i in range(len(nums)):
            if target-nums[i] in visit:
                return [i,visit[target-nums[i]]]
            visit[nums[i]]=i 
        return -1
