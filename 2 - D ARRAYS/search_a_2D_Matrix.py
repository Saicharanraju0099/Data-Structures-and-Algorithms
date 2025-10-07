# Leetcode 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/
# Write an efficient algorithm that searches for a value in an m x n matrix.
# Brute Force Approach
class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for col in row:
                if target == col:
                    return True
        return False

# Optimal Approach (Using Binary Search)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols
            middle_value = matrix[row][col]

            if middle_value == target:
                return True
            elif middle_value < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print("optimal:", Solution().searchMatrix(matrix, target))
print("Brute force:", Solution().searchMatrix(matrix, target))


### 1. BRUTE FORCE APPROACH
'''HOW IT WORKS:'''

'''Step-by-step explanation
The code defines a class Solution with a method searchMatrix.

It loops through every row of the matrix, and then every element (col) in each row.

If any element equals the target, it returns True (meaning the target was found).

If it finishes the entire matrix without finding the target, it returns False.

⏰ Time Complexity:

The algorithm checks every element in the matrix once.

If the matrix has m rows and n columns, there are m * n elements total.

So, Time Complexity = O(m * n).

💾 Space Complexity:

The algorithm only uses a few extra variables (row, col, and the target).

No additional data structures are created.

So, Space Complexity = O(1) (constant space).'''

### 2. OPTIMAL APPROACH (BINARY SEARCH)
'''HOW IT WORKS:'''

'''Step-by-step explanation

You first get the number of rows and columns.
Then you pretend that your entire 2D matrix is just one continuous sorted array of length rows * cols.
So low starts at the first element (index 0), and high starts at the last element.
matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
You mentally treat it like:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

2. The binary search loop:
while low <= high:
    mid = (low + high) // 2
You find the middle index of your virtual 1D array.

3. Converting the 1D index back to 2D:
row = mid // cols
col = mid % cols
This is where the clever mapping happens:

mid // cols gives you which row the middle element is in.

mid % cols gives you which column in that row.

For example, if cols = 4 and mid = 5 →
row = 5 // 4 = 1 and col = 5 % 4 = 1,
so it's the element at matrix[1][1].

4. Compare and adjust:
middle_value = matrix[row][col]

if middle_value == target:
    return True
elif middle_value < target:
    low = mid + 1
else:
    high = mid - 1
Classic binary search move:

If the middle value equals the target, you're done.

If it's smaller, search the right half.

If it's bigger, search the left half.

5. If not found:
return False
If the loop ends, the target doesn't exist in the matrix.

⏰ Time Complexity:
O(log(m * n))
Why?
You're doing binary search on a total of m * n elements.
Binary search always runs in logarithmic time with respect to the number of elements.
So:
Time = log(total elements) = log(m * n)

💾 Space Complexity:
O(1)
You're only using a few variables (low, high, mid, row, col), regardless of how big the matrix is.
No extra arrays, no recursion — constant space.:
'''
