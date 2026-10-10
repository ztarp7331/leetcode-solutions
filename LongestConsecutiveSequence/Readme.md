# Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
## My solution
  Best way is to check if i-1 is in the set(nums) if yes continue because i wont be the starting point of our consecutive line 
then we use a while loop until the prev is in x we keep updating the score 
@main.py 
