def Pattern6(n):
    for i in range(0, n):
        for j in range(0, n - i):
            print(j + 1, end="")
        print()
n = 4
Pattern6(n)

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
