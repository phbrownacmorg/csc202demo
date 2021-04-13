from typing import List
from LList import LList

def sum_python_list(numlist:List[int]) -> int:
    """Sum integers on a Python list."""
    # Pre: all the values on numlist are integers
    result:int = 0
    for k in numlist:
        result = result + k
    return result

def sum_LList(numlist:LList[int]) -> int:
    """Sum integers on an LList."""
    # Pre: all the values on numlist are integers
    result:int = 0 # Value for an empty list; handles the base case
    if not numlist.isEmpty():
        # Sum is the value of this node plus the sum of the rest of the list
        result = numlist._data + sum_LList(numlist._next) # type: ignore
    return result

def strrev(s:str) -> str:
    """Reverse a string, recursively."""
    if len(s) < 2: # Base case
        result = s
    else: # Recursive case
        # Swap the first and last characters and then reverse what's between them
        result = s[-1] + strrev(s[1:-1]) + s[0]
    return result

def gcd(a:int, b:int) -> int:
    """Find the greatest common divisor of two integers a and b, recursively."""
    result:int = b
    if b == 0: # Base case
        result = a
    else: # Recursive case
        result = gcd(b, a % b)
    return abs(result)
