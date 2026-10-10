class Solution:
    def removeDuplicates(self,nums:List[int])->int:
        l=0
        l1=1
        while l1<len(nums):
            if nums[l]!=nums[l1]:
                l+=1
                nums[l]=nums[l1]
            l1+=1
        return l+1

