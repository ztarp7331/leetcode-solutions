#hashSet version
class Solution:
    def containsDuplicate(self,nums:List[int])->bool:
        num=set(nums)
        return len(num)==len(nums)
# heapsort version
class Solution:
    def heapify(self,arr,n,i):
        largest=i 
        left=2*i+1
        right=2*i+2
        if left<n  and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest=right
        if largest!=i:
            arr[largest],arr[i]=arr[i],arr[largest]
            self.heapify(arr,n,largest)
    def heapSort(self,arr:List[int]):
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return True 
        return False 

