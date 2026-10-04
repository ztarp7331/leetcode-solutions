# Exclusive Time of Function
## Problem
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n - 1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

## Solution
  a.Use a stack to keep track of which is the top element in the stack
  b. If there is no element in the stack then just directly push and also keep track of a prevStamp which tells the last Start time in the stack
  c. In case the log ends then u can subtract current stamp from prevStamp and update the prevStamp to stamp +1 
Solution is in @main.py
