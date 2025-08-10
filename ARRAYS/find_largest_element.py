def find_largest(arr):
    max_elem = arr[0]  #20,30,45,220
    for num in arr:
        if num > max_elem:  #10>10(false),#20>10(True),#30>20(True),#4>30(false),45>4(True),220>45(True),90>220(false)
            max_elem = num
    return max_elem

arr = [10,20,30,4,45,220,90]
print("largest element is: ",find_largest(arr))