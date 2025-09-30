## Brute Force Approach
## leetcode 169

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in set(nums):
            if nums.count(x) > len(nums) // 2:
                return x
            
# Optimal Approach

            count = 0
            x = None
            for num in nums:
               if count == 0:
                  x = num
                  count += 1 if num == x else -1
            return x
     
nums = [2,2,1,1,1,2,2]
print("Brute Force",Solution().majorityElement(nums))
print("Optimal",Solution().majorityElement(nums))

# Brute Force Approach
'''HOW IT WORKS:'''
'''
1.)set(nums)

nums could have repeated numbers.

set(nums) removes duplicates.

Example: if nums = [2,2,1,1,1,2,2], set(nums) will be {1, 2}.

2.)for x in set(nums):

We loop through each unique number in nums.

First iteration: x = 1

Second iteration: x = 2

3.)nums.count(x)

Counts how many times x appears in the original list.

Example: nums.count(2) = 4, nums.count(1) = 3.

4.)if nums.count(x) > len(nums) // 2:

len(nums) // 2 is half the size of the list (integer division).

In this case: len(nums) = 7, 7 // 2 = 3.

So any number appearing more than 3 times is the majority element.

5.)return x

As soon as we find such a number, return it.

In this example: 2 appears 4 times, which is > 3 → return 2.

✅ Time Complexity: O(n^2) (because count() itself loops over the list)
✅ Space Complexity: O(n) (for the set)'''

## Optimal Approach

'''HOW IT WORKS:'''
'''
1.)count = 0 and x = None

x will track the candidate for majority element.

count tracks the “balance” of how many times we’ve seen this candidate relative to other numbers.

2.)for num in nums:

Loop through each number in the array.

3.)if count == 0:

If count drops to 0, pick the current number as the new candidate.

Initially, count is 0, so the first number (2) becomes the candidate.

4.)count += 1 if num == x else -1

If the current number matches our candidate (x), we increase count by 1.

If it doesn’t match, we decrease count by 1.

This balances out the candidate against other numbers.

5.)return x

At the end of the loop, x is guaranteed to be the majority element.

✅ Time Complexity: O(n) (single pass)
✅ Space Complexity: O(1) (no extra space used)'''