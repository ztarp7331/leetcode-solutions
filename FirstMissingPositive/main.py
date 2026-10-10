class Solution:
    def firstMissing(self,nums:List[int])->int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1 # in case of whole array gets sorted by cycle sort 
