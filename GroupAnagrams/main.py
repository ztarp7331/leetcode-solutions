from collections import defaultdict
class solution:
    def groupAnagram(self,strs:List[str])->List[str]:
        visit=defaultdict(list)
        for i in strs:
            visit["".join(sorted(i))].append(i)
        return list(visit.values())
