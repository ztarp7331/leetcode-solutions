class Solution:
    def topK(self,nums:List[int],k:int)-> List[int]:
        count =Counter(nums)
        res=[]
        buckets=[[]for _ in range(len(nums)+1)]
        for item,freq in count.items():
            buckets[freq].append(item)
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k: 
                    return res
