# Course Schedule - I 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# My solution
## Using Topo Sort (Kahn's Algorithm)
So There are other ways to solve Course Schedule but I feel the easiest to grasp is how indegrees collapsing to zero leads to proper following of node A coming only after Node B ( corresponding to definition of TopoSort)

### The solution is in main.py :D 

