from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(list)
        for i in strs:
            hashMap["".join(sorted(i))].append(i)
        return list(hashMap.values())
