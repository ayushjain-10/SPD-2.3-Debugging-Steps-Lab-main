"""
Exercise 4
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

def binary_search(arr, element, low=0, high=None):
      """Returns the index of the given element within the array by performing a binary search."""
      if high == None:
          high = len(arr) - 1
  
      if high < low:
        # Element is not present in the array
          return -1
  
      mid = (high + low) // 2
      
    # If element is present at the middle itself
      if arr[mid] == element: 
          return mid
  
      elif arr[mid] > element:
        # reruns the search with new valuers for low and high
          return binary_search(arr, element, low, mid-1)
  
      else: 
        # reruns the search with new valuers for low and high
          return binary_search(arr, element, mid+1, high)
        
if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7, 9], 7)
    print(answer)

# expected error: recursion error due to not changing the middle element it willl be looped to on the same mid the next iteration
#line 34 and 35 were the cause
# it should be mid-1 and mid +1 