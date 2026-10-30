So Brute Force Approach
  Convert to List (basically in string problem treating as list helps #pattern) then to check for condition of anagram sort both list if they turn out to be same then yes. O(n2)

Better Approach 
  When trying to see if two things are following some common property try to see what underlying fact must always be true and then check for the validity of it. In case of anagrams, the fact is the frequency count will be exact same.

Optimised Approach
  Instead of making two frequency counter, just make one and remove elements from it using the second word if there is an existence of character in second word and not in frequency map then we will say false

