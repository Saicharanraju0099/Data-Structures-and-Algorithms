def Pattern10(n):
      for i in range(n):
            print(" " * (n - i - 1) + "*" * (2 * i + 1))
        
        # 2. Inverted Pyramid
      for J in range(n):
            print(" " * J + "*" * (2 * n - (2 * J + 1)))
n = 4
Pattern10(n)

'''
Time Complexity:

The pattern consists of two parts:
1. Top Pyramid
2. Inverted Pyramid

Top Pyramid:
- Outer loop runs n times
- Spaces print (n - i - 1) times
- Stars print (2*i + 1) times

Inverted Pyramid:
- Outer loop runs n times
- Spaces print J times
- Stars print (2*n - (2*J + 1)) times

Total operations:
n² operations overall

Worst Case: O(n²)
Best Case: O(n²)

Space Complexity:

No extra arrays or data structures are used.

Only loop variables and string operations are used.

Space: O(1)
'''