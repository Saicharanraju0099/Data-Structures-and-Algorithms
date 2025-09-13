
## BRUTE FORCE METHOD 
def brute(arr,k):
    n = len(arr)
    rotations = k % n
    print(f"n = {n}, k = {k}, rotations = {rotations}")
    for _ in range(rotations):
        last_element = arr.pop()
        arr.insert(0,last_element)
        print(arr,"\n-----------------------------------------------------------")
    return arr



# OPTIMAL METHOD
def optimal(arr,k):
    k = k % len(arr)
    print(f"k = {k}, arr[-k:] = {arr[-k:]},arr[:-k] = {arr[:-k]} ")
    return arr[-k:] + arr[:-k]

 
arr = [1,2,3,4,5]
k = 2
print("Bruteforce method",brute(arr,k))
print("Optimal",optimal(arr,k))


## Complexity Analysis
'''## Brute Force

Each pop() at the end is O(1).

Each insert(0, x) is O(n) because all elements shift right.

This is done k times.

Time complexity: O(k·n) (worst case O(n²) when k ≈ n).
Space complexity: O(1) (in-place, only a few variables used).

##Optimal

arr[-k:] → slice of size k → O(k).

arr[:-k] → slice of size n-k → O(n-k).

Concatenation → O(n).

Time complexity: O(n).
Space complexity: O(n) (because new arrays are created for slices and concatenation).'''