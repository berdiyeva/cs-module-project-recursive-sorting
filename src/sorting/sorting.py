# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # $%$Start
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

    # Your code here
    # create a new merged arr
    # merged_arr = []
    # add items to it in order from arrA and arrB
    # a_index = 0
    # b_index = 0
    # while a_index < len(arrA) and b_index < len(arrB):
    #     if arrA[a_index] < arrB[b_index]:
    #         merged_arr.append(arrA[a_index])
    #         a_index += 1 
    #     elif arrA[a_index] >= arrB[b_index]:
    #         # append the element from the b arr
    #         # increment the b index
    #         merged_arr.append(arrB[b_index])
    #         b_index += 1
    #     # add the rest of the elements to merged 
    #     if b_index < len(arrB):
    #         merged_arr.extend(arrB[b_index:])
    #     if a_index < len(arrA):
    #         merged_arr.extend(arrA[a_index:])


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    print("Splitting ", arr)
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)

    return arr


   

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    # mid2 = mid + 1

    # if arr[mid] <= [mid2]:
    #     return
    pass
    


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
