# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

        # Check base case 
    if start >= end:
        mid = end + start // 2

        # Check if arr is empty
        if len(arr)== 0:
            return -1

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid
        
        # If element is smaller than mid, then it  
        # can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, start, mid-1, target)

        # Else the element can only be present  
        # in right subarray
        else:
            return binary_search(arr, mid+1, end, target)
    
    else:
        # Element is not present in the array 
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    pass