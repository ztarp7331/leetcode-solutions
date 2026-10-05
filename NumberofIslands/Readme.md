# Number of islands
## Problem Statement
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
## Solution
i like doing it using BFS, although the implementation in code over in this sucks. but basically keep track of visited islands using a set. 
make a helper BFS function which basically traverses the whole island unit using directions, this helper function is only called when a new island is found (checked using visit set.)
Now within this helper function first we make a deque and add in visit set then popleft and traverse to all possible levels of the BFS.
