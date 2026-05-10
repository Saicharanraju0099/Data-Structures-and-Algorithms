## Function to print the pattern
def pattern(n):
    ## Outer loop to handle the number of rows
    for i in range(n):
        ## Inner Loop to handle the number of columns
        for j in range(n):
            print("*", end=" ")
        print()  # Move to the next line after printing each row
n = 4
pattern(n)






# TIME AND SPACE COMPLEXITY

'''
⏱ Time Complexity:

There are two loops.

Outer loop runs n times.
Inner loop also runs n times for every row.

So total operations become:

n x n = n²

✅ Time Complexity: O(n²)

Because for every row, we print n stars.
'''


'''
🧠 Space Complexity:

No extra array or data structure is used.

Only loop variables:
- i
- j
- n

These take constant memory.

✅ Space Complexity: O(1)

This is called constant extra space.
'''