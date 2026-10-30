class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# Try and Except Version
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while nums:
            try:
                nums.remove(val)
                i += 1
            except:
                break
        return i
