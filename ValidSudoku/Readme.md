# Valid Sudoku 
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
## Solution

  The best approach, simple and optimal is to iterate over the whole matrix exactly once.
  Put every valid element into a resulting array with 3 tuples such that you cover the three cases -> (i,element),(element,j)
  and (i//3,j//3, element)
this covers the validity.
Then we can check if any element is duplicate by comparing the length of it to its set.
