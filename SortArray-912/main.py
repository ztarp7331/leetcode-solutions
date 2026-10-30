# Merge Sort
class Solution:
    def merge(self, leftSide: list[int], rightSide: list[int]) -> list[int]:
        i = 0
        j = 0
        x = []
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                x.append(leftSide[i])
                i += 1
            else:
                x.append(rightSide[j])
                j += 1

        while i < len(leftSide):
            x.append(leftSide[i])
            i += 1
        while j < len(rightSide):
            x.append(rightSide[j])
            j += 1
        return x

    def mergeSort(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        leftArray = nums[:mid]
        rightArray = nums[mid:]
        leftArray = self.mergeSort(leftArray)
        rightArray = self.mergeSort(rightArray)
        merged = self.merge(leftArray, rightArray)
        return merged


# Heap Sort
import heapq


class Solution1:
    def heapSort(self, nums: list[int]) -> list[int]:
        heapq.heapify(nums)
        arr = []
        while nums:
            arr.append(heapq.heappop(nums))
        return arr
