class Solution:
    def arraySum(self, nums):
        # Start from index 0
        return self.sum(nums, 0)

    def sum(self, nums, left):
        # Base case: out of bounds
        if left >= len(nums):
            return 0
        # Add current element and recurse
        return nums[left] + self.sum(nums, left + 1)

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3] 
    result = solution.arraySum(nums)
    print(result)
 
    