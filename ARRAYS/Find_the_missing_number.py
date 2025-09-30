## Brute Force Approach  
## Leetcode Problem: 268. Missing Number
## https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i
arr = [3,0,1]
print("Brute force",Solution().missingNumber(arr))           


## Optimal Approach
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n*(n+1)//2
        Actual_sum = sum(nums)
        return expected_sum - Actual_sum
arr = [3,0,1]
print("Optimal",Solution().missingNumber(arr))



### 1. BRUTE FORCE APPROACH
'''HOW IT WORKS:'''

'''Step-by-step explanation

Suppose:

nums = [3, 0, 1]


1.) Range to check:
len(nums) = 3, so range(len(nums)+1) = range(4) = [0, 1, 2, 3].
That's because the missing number can be anywhere between 0 and n.

2.)Loop check:
The loop goes through i = 0, 1, 2, 3.

i = 0 → 0 in nums? yes. Continue.

i = 1 → 1 in nums? yes. Continue.

i = 2 → 2 in nums? no!
→ return 2. ✅

3.)Answer: Missing number is 2.'''

'''Time Complexity

This solution is inefficient:

The for loop runs n+1 times.

if i not in nums scans the whole list each time (O(n)).

Total complexity = O(n²) in worst case.'''

'''Space complexity: O(1) → no extra data structures, just loop variables.'''

### 2. OPTIMAL APPROACH
'''HOW IT WORKS:'''
'''Step-by-step
Step 1: n = len(nums)

nums contains n numbers, but one is missing from the range 0...n.

Example: if nums = [3,0,1], then n = 3.

Step 2: expected_sum = n*(n+1)//2

Formula for sum of all integers from 0 to n.

If no number were missing, this would be the total.

Example:
For n = 3, numbers should be [0,1,2,3].
Sum = 3*4//2 = 6.

Step 3: Actual_sum = sum(nums)

Just add up the numbers that are actually present in the list.

Example: sum([3,0,1]) = 4.

Step 4: return expected_sum - Actual_sum

Missing number = what should have been there  
what is actually there.
Example: 6 - 4 = 2.✅'''

'''Efficiency

Time complexity: O(n) (just one pass to sum).

Space complexity: O(1) (no extra storage, just integers).

Much faster than the if i not in nums approach (which was O(n²)).'''




