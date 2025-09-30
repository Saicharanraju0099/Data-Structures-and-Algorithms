## Brute Force Approach

class Solution:
    def intersection(self, nums1, nums2):
        result = []
        m = len(nums1)
        n = len(nums2)
        if m > n:
            for num in nums1:
                if (num in nums2) and (num not in result):
                    result.append(num)
        else:
            for num in nums2:
                if (num in nums1) and (num not in result):
                    result.append(num)
        return result



## Optimal Approach
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print("Brute force Approach",Solution().intersection(nums1,nums2))
print("Optimal Approach",Solution().intersection(nums1,nums2))


### 1. BRUTE FORCE APPROACH
'''HOW IT WORKS:'''
'''making a class Solution .

intersection takes two lists: nums1 and nums2.

result will store the unique common elements.

m and n are just the lengths of the two lists

Loop through the longer array.
Doesn't actually save much work though — since the costly operation is num in nums2 or num in nums1, which is O(n) for lists (it searches linearly).

Inside the loop:

Check if the element exists in the other list.

Make sure it's not already in result (so no duplicates).

If both checks pass, append it to result.

👉🏻Step by step:

m = 3, n = 5, so m < n.

Code loops through nums2: [9,4,9,8,4]

Check each:

9 → is in nums1 → not yet in result → add → result = [9]

4 → is in nums1 → not yet in result → add → result = [9,4]

Next 9 → is in nums1, but already in result → skip

8 → not in nums1 → skip

Last 4 → in nums1, but already in result → skip

Final answer: [9,4]

⏱️ Time Complexity

You loop over one list (nums1 or nums2), and for every element you do two checks:

num in nums2 (or num in nums1) → linear search → O(n) in the worst case.

num not in result → another linear search in result → worst case O(k), where k is the size of the intersection (at most min(m, n)).

So in the worst case, for each of the max(m, n) iterations, you're doing an O(n) check + an O(k) check.

Rough bound: O(m x n) in the worst case.

The num not in result check doesn't add much asymptotically, since k ≤ min(m, n) ≤ n. So the bottleneck is really the num in numsX check.

👉 Final Time Complexity: O(m x n)

💾 Space Complexity

You create a result list to store the intersection.

In the worst case, if all elements are common, result can hold up to min(m, n) elements.

👉 Final Space Complexity: O(min(m, n))'''

## 2. OPTIMAL APPROACH
'''HOW IT WORKS:'''
'''set(nums1) → makes a set out of nums1.
Example: [4,9,5] → {4,9,5}
(sets automatically remove duplicates and store unique values only).

set(nums2) → {9,4,8}
Notice how duplicates like the extra 9 and 4 are gone.

& → this is the set intersection operator in Python.
{4,9,5} & {9,4,8} = {4,9}

list(...) → convert the set back into a list because the problem likely expects a list, not a set.

👉🏻Steps:

set(nums1) = {4, 9, 5}

set(nums2) = {9, 4, 8}

Intersection = {4, 9}

Convert to list = [4, 9]

⏱️ Time Complexity

Let's break it down:

set(nums1) → goes through nums1 once → O(m).

set(nums2) → goes through nums2 once → O(n).

Intersection & → goes through the smaller set and checks membership in the larger → O(min(m, n)) on average (because set membership check is O(1) on average, thanks to hashing).

list(...) → takes O(k), where k is the size of the intersection.

So total = O(m + n) time.

That's way better than O(m x n) from brute force.

💾 Space Complexity

set(nums1) takes O(m).

set(nums2) takes O(n).

Result set takes O(k), with k ≤ min(m, n).

Total = O(m + n) space.'''

