# Function to print pattern
def pattern2(n):

    # Outer loop for rows
    for i in range(n):

        # Inner loop for columns
        for j in range(i + 1):
            print("*", end="")

        # Move to next line
        print()


# Driver Code
n = 5
pattern2(n)





# TIME AND SPACE COMPLEXITY

'''
⏱ Time Complexity:

Outer loop runs n times.

Inner loop runs:
- 1 time in 1st row
- 2 times in 2nd row
- 3 times in 3rd row
...
- n times in nth row

Total operations:

1 + 2 + 3 + ... + n

Formula:

n(n + 1) / 2

Ignoring constants in Big-O:

✅ Time Complexity: O(n²)

Because total star printing grows quadratically.
'''


'''
🧠 Space Complexity:

No extra array or data structure is created.

Only loop variables are used:
- i
- j
- n

These require constant memory.

✅ Space Complexity: O(1)

Because the program uses fixed extra space.
'''