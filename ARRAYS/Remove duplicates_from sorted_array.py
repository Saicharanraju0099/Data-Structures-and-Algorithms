### 26. Remove Duplicates from Sorted Array

def remove_duplicates(nums):
    k = 1
    for i in range(1,len(nums)):
        if(nums[i] != nums[i-1]):
                nums[k] = nums[i]
                k += 1
        print(f"iteration(i) = {i},\nunique_elements(k) = {k},\nnums = {nums}\n ------------------------------")
    return k
nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
remove_duplicates(nums)
print(nums)
