# Brute force way
def brute_force(arr):
    if(len(arr)<2):
        return "Need more array elements"
    sorted_array = sorted(arr,reverse=True)
    return sorted_array[1]

arr = [3,5,1,2,10,8,7]
print("Second largest array: ",brute_force(arr))

# Optimal way
def optimal(arr):
    largest = secondlargest=float("-inf")
    for num in arr:
        if(num > largest):
           secondlargest = largest 
           largest = num
        elif num > secondlargest and num != largest:
            secondlargest = num
    if (secondlargest != float("-inf")):
        return secondlargest
    return "Not found"

arr = [3,5,1,2,10,8,7]
print("Second largest array: ",optimal(arr))


# NOTES FOR TIME AND SPACE COMPLEXITY FOR BRUTE FORCE WAY

"""if (len(arr) < 2) → Checks if there are at least 2 elements. O(1)

sorted(arr, reverse=True) → Sorts the array in descending order. Python uses Timsort, which has:

Time Complexity: O(n log n) for sorting.

Space Complexity: O(n) (because sorted() creates a new list).

sorted_array[1] → Accessing by index is O(1)."""

"""Final Complexity :
Time: O(n log n) (because of sorting)

Space: O(n) (extra sorted array)"""

## TIME AND SPACE COMPLEXITY FOR OPTIMAL WAY

"""Complexity :
Time: O(n) (one pass through array)

Space: O(1) (only two variables regardless of array size)"""