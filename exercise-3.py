"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i] 
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j] : # should have declared j >= 0
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

# expected error: IndexError: list index out of range
# assumption: line 27 would cause the error as since we did not declare that j should be greater than 0
# this would cause the iteration to run on an index which does not exist therefore causing an error

