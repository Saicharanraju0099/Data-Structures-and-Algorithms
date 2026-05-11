def Pattern7(n):
    for i in range(0, n):
        for j in range(0,(n - i - 1)):
            print(" ",end="")
        for j in range(0, i * 2 -1):
            print("*", end="")
        print()
n = 5
Pattern7(n)


'''
Time Complexity:

Outer loop runs n times.

For each row:
- Spaces loop runs (n - i - 1) times
- Stars loop runs (2*i + 1) times

Total operations:
n² operations overall

Worst Case: O(n²)
Best Case: O(n²)

Space Complexity:

No extra arrays or data structures used.

Only loop variables are used.

Space: O(1)
'''