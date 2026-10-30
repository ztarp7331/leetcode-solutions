class Solution:
    def validAnagram(self,s1:str,s2:str)->bool:
        freq={}
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            freq[s1[i]]=freq.get(s1[i],0)+1
        for j in range(len(s2)):
            if freq.get(s2[j],0)==0:
                return False 
            freq[s2[j]]=freq.get(s2[j],0)-1
        return True 
