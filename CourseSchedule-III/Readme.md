# Course Schedule - III 
## Problem Statement
  There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.
## Solution
So here we will be given a List of List which contains duration and deadline to finish a course.

1. So this can be solved in 3 steps 
    a. First sort the courses based on the last element or the end time  as we know we want to maximise the amount of courses, we should cover the courses whose end time is deadline is early 
    b. Now add the duration in the maxHeap which takes care of the order of items in the Heap, so when the totalTime > deadline for a course we can pop the course with highest duration and maybe fit 2 more courses in place of that one big ass course.
    c. return the length of the maxHeap
Check @main.py for the Solution  Code. 
