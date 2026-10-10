class Solution:
    def permutation(self,nums:List[int])->None:
        # In Place updating
        pivot=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i 
        if pivot==-1:
            nums.reverse()
            return
        nums[pivot+1]=nums[pivot+1:][::-1]
        for i in range(pivot+1,len(nums)):
            if nums[pivot]<nums[i]:
                nums[pivot],nums[i]=nums[i],nums[pivot]
                return
