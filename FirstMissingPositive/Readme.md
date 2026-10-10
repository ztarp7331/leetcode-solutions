# First Missing Positive
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## My solution
  One way is to use a hashset but it is O(n) which is not so fancy
  Other way is to **cycle sort** -> nums[i] value shud be at index nums[i]-1 if tht is not the case u swap and make it that way.
  do this for the whole array and you do a second pass to get any value which doesnt follow this principle that will be our missing positive integer.
@main.py 

