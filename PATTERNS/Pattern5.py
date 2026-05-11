def Pattern5(n):
    for i in range(0, n):
        for j in range(0,n - i):
            print("*", end="")
        print()
n = 5
Pattern5(n)



'''
Time Complexity:

Outer loop runs n times.

Inner loop runs:
n + (n-1) + (n-2) + ... + 1 times

Total operations:
n(n+1)/2

Worst Case: O(n²)
Best Case: O(n²)

Space Complexity:

No extra arrays or data structures used.

Only loop variables are used.

Space: O(1)
'''