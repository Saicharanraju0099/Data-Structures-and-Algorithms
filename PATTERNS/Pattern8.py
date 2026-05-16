def Pattern8(n):
    for i in range(0, n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0, (2 * n - 1) - (2 * i)):
            print("*", end="")
        print()
n = 7
Pattern8(n)

'''
Time Complexity:

Outer loop runs n times.

For each row:
- Spaces loop runs i times
- Stars loop runs (2*n - 1 - 2*i) times

Total operations:
n² operations overall

Worst Case: O(n²)
Best Case: O(n²)

Space Complexity:

No extra arrays or data structures used.

Only loop variables are used.

Space: O(1)
'''