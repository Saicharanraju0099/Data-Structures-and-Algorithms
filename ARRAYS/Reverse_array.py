def brute(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
    return arr

def optimal(arr):
    return arr[::-1]
arr = [1,2,3,4,5]
print("Reverse Array \n Brute force: ",brute(arr.copy()))
print("Reverse Array \n Optiaml: ",optimal(arr))








# TIME AND SPACE COMPLEXITY FOR BRUTE FORCE METHOD

'''⏱ Time Complexity:

The loop runs n//2 times.

Each iteration does a single swap, which is O(1).

So total operations = O(n/2), which simplifies to O(n).

✅ Time Complexity: O(n)
Because we still have to touch half the elements, and constant factors don't matter in Big-O.'''

'''🧠 Space Complexity:

You're not creating any extra array or data structure.

Just using the original array and few variables (n, i, and temp swap).

That's constant space.

✅ Space Complexity: O(1)
In-place operations always give that sweet O(1) extra space.'''

# TIME AND SPACE COMPLEXITY FOR OPTIMAL METHOD

'''✅ Optimal (using slicing [::-1])
⏱ Time Complexity:

Slicing creates a new reversed copy of the list.

It still touches every element once.

So ⏱ Time = O(n)

🧠 Space Complexity:

It creates a whole new array in memory, same size as original.

So 🧠 Space = O(n))'''