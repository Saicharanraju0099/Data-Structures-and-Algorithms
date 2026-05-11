def Pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()
n = 4
Pattern4(n)


# TIME AND SPACE COMPLEXITY

'''
Time Complexity:

Outer loop runs n times.

Inner loop runs:
1 + 2 + 3 + ... + n times

Total operations:
n(n+1)/2

Worst Case: O(n²)
Best Case: O(n²)

Space Complexity:

No extra arrays or data structures used.

Only loop variables are used.

Space: O(1)
'''