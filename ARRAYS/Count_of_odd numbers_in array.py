class Solution:
    # Function to count the odd numbers in an array 
    def countOdd(self, arr, n):
        count = 0
        # Iterate through the array
        for num in arr:
        # Check for odd values and increment
            if num % 2 != 0:
                count += 1
        return count
        
# Main method
if __name__ == "__main__":
    # Creating an instance of Solution class
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    
    # Function call to count the odd numbers in an array 
    count = sol.countOdd(arr, n)
    print("Count of odd numbers:", count)


