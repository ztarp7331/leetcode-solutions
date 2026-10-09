# Two Sum 
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## solution
  Use a HashMap with array values as key and index as value 
  Add element to HashMap with each iteration and check if the diff is there if not append if it is there return the indices
Solution in @main.py 
