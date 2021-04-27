# Sequential search

from typing import List, Optional, TypeVar

T = TypeVar('T')

def sequential(array:List[T], key:T) -> Optional[int]:
    """Do a sequential search for a given key KEY in a list ARRAY.  Return the index
    of KEY in ARRAY, or None if KEY isn't in ARRAY."""
    idx:int = 0
    found:bool = False
    while (not found) and (idx < len(array)): 
        if array[idx] == key:
            found = True
        else:
            idx = idx + 1
    if not found:
        return None
    return idx


def binsearch(array:List[T], key:T) -> Optional[int]:
    """Do a binary search for a given key KEY in a list ARRAY.  Return the index
    of KEY in ARRAY, or None if KEY isn't in ARRAY."""
    # Pre:
    # array is sorted in increasing order
    mid:int = (len(array)-1) // 2
    #print(mid, key, array)
    result:Optional[int] = None

    # Base cases
    # Check for an empty array *before* trying to look into the array, to avoid the IndexError
    if len(array) == 0: # key is just not here
        result = None
    elif key == array[mid]: # Found it!
        result = mid
    # Recursive cases
    elif key < array[mid]: # type: ignore
        # key < array[mid]; look left
        # array[:mid] contains elements 0 through (mid-1)
        result = binsearch(array[:mid], key)
    elif key > array[mid]: # type: ignore
        # key > array[mid]; look right
        # array[mid+1:] contains elements mid+1 through the end
        result = binsearch(array[mid+1:], key)
        if result is not None:
            # Need to adjust the returned index
            result = result + (mid+1)
    return result

# Binary search
# Items:   1 2 4 8 16 32
# Lookups: 1 2 3 4  5  6