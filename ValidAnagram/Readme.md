# Valid Anagram 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
## My Solution
  The most optimal approach to solving this question is first checking if the length of both s and t is same or not.
  After that just make a frequency hashmap of one of the words and compare the second word freq count with that hashmap by using  subtractive method. if count.get(characterInT,0)==0 means that the character is in word t but the count of it in word s is 0 hence mismatch

