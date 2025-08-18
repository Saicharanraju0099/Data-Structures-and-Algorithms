def brute(arr):
    unq = []
    for num in arr:
        if num not in unq:
            unq.append(num)
    return unq

def optimal(arr):
    return list(set(arr))
array = [1,2,3,4,4,5,2]
print("Unique elements \n Brute Force",brute(array))
print("Unique elements \n Optimal",optimal(array))






# SPACE AND TIME COMPLEXITY FOR BRUTE METHOD 

'''⏱ Time Complexity

Let's analyze the worst-case time complexity:

The outer loop runs n times (for each element in arr).

For every element, you do if num not in unq:

The in operator on a list takes O(k) time, where k is the current length of unq.

In the worst case, unq could end up nearly as long as the input array so up to n.

Total time = O(1 + 2 + 3 + ... + n) ≈ O(n^2)

👉 Time Complexity: O(n²)

It's quadratic. Definitely not optimal, but works for small arrays.
'''

'''📦 Space Complexity

You're storing unique elements in a new list unq. In the worst case (if all elements were unique), unq will store n items.

So you're using O(n) extra space.

👉 Space Complexity: O(n)'''



