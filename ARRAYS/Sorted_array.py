# Brute force Method
def brute_force(arr):
    n = len(arr)
    for i in range(n-1):
        if (arr[i] > arr[i+1]):
            return False
    return True

arr = [1,2,3,6,4,5]
print("Sorted?: ",brute_force(arr))

# optimal method
def optimal(arr):
    return all(arr[i]< arr[i+1] for i in range(len(arr)-1))

arr = [1,2,3,4]
print("Sorted?: ",optimal(arr))









## TIME AND SPACE COMPLEXITY FOR BRUTE FORCE METHOD

'''Time Complexity : 
Worst case: Array is already sorted → must check all n-1 pairs → O(n).

Best case: First two elements are out of order → return immediately → O(1).

Average case: Depends on data distribution, but still O(n) in big-O notation.'''

'''Space Complexity :

No extra storage except n and i → O(1).

This is an in-place check — doesn't modify or copy the array.'''

# TIME AND SPACE COMPLEXITY FOR OPTIMAL WAY
'''Time Complexity :
range(len(arr) - 1) → produces n-1 indices (O(n)).

For each index i, it checks arr[i] < arr[i+1] (O(1) per comparison).

all(...) stops early if it finds a False (best case O(1)), otherwise scans all pairs (worst case O(n)).

Worst case: O(n)
Best case: O(1) (if first pair fails)

Space Complexity : 
The generator expression (arr[i] < arr[i+1] for i in ...) is lazy → O(1) extra space.

No lists or intermediate arrays are built.

Space: O(1)'''