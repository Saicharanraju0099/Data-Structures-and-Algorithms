def brute(nums):
    n = len(nums)
    non_zeros = [num for num in nums if num != 0]   # keep all non-zero values
    zeros = n - len(non_zeros)                      # count how many zeroes
    result = non_zeros + [0] * zeros                # append the right number of zeroes
    
    for i in range(n):                              # copy back into nums
        nums[i] = result[i]
    
    return nums


def optimal(nums):
    pointer = 0
    for i in range(len(nums)):
        if(nums[i]!= 0):
            nums[pointer],nums[i] = nums[i], nums[pointer]
            pointer += 1
    return nums

nums = [0, 1, 0, 3, 12]
print("Brute force",brute(nums))
print("Optimal",optimal(nums))


##1.brute(nums)

'''How it works:

Builds a new list non_zeros containing only the non-zero elements ([1,3,12]).

Figures out how many zeros are missing (zeros = n - len(non_zeros) → 5 - 3 = 2).

Creates a result list by concatenating non_zeros with that many zeros ([1,3,12,0,0]).

Copies the values from result back into the original list nums.

Time Complexity:

List comprehension to filter non-zeros → O(n)

Concatenation with zeros → O(n)

Copying result back into nums → O(n)
Total = O(n)

Space Complexity:

Extra list non_zeros (up to size n)

Extra list result (size n)
So that's O(n) space.'''

##2.optimal(nums)

'''How it works:

Keeps a pointer that tracks the position of the next non-zero.

Iterates over nums once:

If nums[i] isn't zero, it swaps it with the value at nums[pointer] and then increments pointer.

Zeros automatically end up shifted to the right.

Step-by-step for [0, 1, 0, 3, 12]:

i=0: nums[0] is zero → do nothing.

i=1: nums[1]=1, swap with nums[pointer=0] → [1,0,0,3,12], pointer=1

i=2: nums[2]=0 → skip

i=3: nums[3]=3, swap with nums[pointer=1] → [1,3,0,0,12], pointer=2

i=4: nums[4]=12, swap with nums[pointer=2] → [1,3,12,0,0], pointer=3

Done.

Time Complexity:

Single loop through the list → O(n)

Space Complexity:

No extra storage except a few variables (pointer) → O(1)'''