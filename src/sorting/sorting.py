# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    return sorted(arrA + arrB)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    a = []
    b = []
    a = arr[:int(len(a)/2)]
    b = arr[int(len(a)/2):]
    arr = merge(a, b)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
