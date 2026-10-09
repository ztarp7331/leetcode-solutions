# Group Anagrams
  Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## My solution
  Use default dict to make a HashMap {sortedWord:[List of words corresponding to it]}
  Based on this just return HashMap.values()
solution in @main.py
