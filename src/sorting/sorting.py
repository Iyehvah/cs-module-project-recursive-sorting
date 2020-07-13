# TO-DO: complete the helper function below to merge 2 sorted arrays
# THIS IS THE ITERATIVE WAY
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    a = 0 #left pointer
    b = 0 #right pointer

    for i in range(elements):
        #if we are out of elements on the left
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        #if we are out of elements on the right
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        #if the left is smaller
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        #if the right is smaller
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
#this is the RECURSIVE WAY and i think the run time is 0(n log n)
def merge_sort(arr):
    # Your code here
    #base case here
    #if our array length is greater than 1 run this code but if its not dont run the code
    if len(arr) > 1:
        # creating our mid point here by dividing the length of our array by 2 
        mid = len(arr)//2
        # the left our our array will be spliced from our mid point to the left
        left = arr[:mid]
        # the right of our array will be spliced from our mid point to the right.
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

