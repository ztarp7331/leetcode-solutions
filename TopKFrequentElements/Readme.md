# Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
## My solution
Well One approach is to make a counter sort it descending order and return k keys
But this is sub-optimal as sorting takes O(nlogn) time.
We can use bucket sort
Its a sorting technique which doesnt use comparison but sorts!
In a general bucket sort you make a table such that 
| Item | Count 
| ------------- |
| i | The count 

But for this problem we will be a little unusual and use | Coutn | Item[List]
| ------------- |
| count upto n | Item in a list which  have this count

This goes on till [0,len(list)] 
After that you iterate from the back and add each element till length of result ==k 
Solution in @main.py 
