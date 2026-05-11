def Pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
n = 4
Pattern3(n)


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

No extra data structures used.

Space: O(1)
'''