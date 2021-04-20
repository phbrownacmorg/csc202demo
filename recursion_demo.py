from typing import List, Tuple
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

def slowexp(a:float, b:int) -> float:
    """Find a**b recursively, where b is a natural number.  
    O(n) algorithm.
    
    a ** b = 1 if b = 0
           = a * (a ** (b-1)) if b > 0
    """
    # Pre:
    assert b >= 0
    result:float = 1 # Already handles base case
    if b > 0: # Recursive case
        result = a * slowexp(a, b - 1)
    return result

def fastexp(a:float, b:int) -> float:
    """Find a**b recursively, where b is a natural number.
    This algorithm runs faster, in O() time.
    
    a ** b = 1 if b == 0
           = (a ** (b//2)) ** 2 if b > 0 and b is even
           = a * (a ** (b//2)) ** 2 if b > 0 and b is odd

    How many function calls?
    b  calls
    0  1
    1  2
    2  3
    3  3
    4  4
    5  4
    6  4
    7  4
    8  5
    9  5
    10 5
    11 5
    12 5
    13 5
    14 5
    15 5
    16 6

    O(lg n) algorithm
    """
    # Pre:
    assert b >= 0
    result:float = 1 # Already handles base case
    if b > 0: # Recursive cases
        halfexp:float = fastexp(a, b // 2)
        if (b % 2 == 0):  # b is even
            result = halfexp * halfexp
        else:             # b is odd
            result = a * halfexp * halfexp
    return result

def baseconv(x:int, base:int) -> str:
    """Express the given integer X in the given base BASE.  Return the result as a string.
    
    x and b are natural numbers.

    baseconv(x, base) = digits[x] if x < base
                      = baseconv(x // base, base) + digits[x % base] if x >= base

    Example: 233 in base 8
    baseconv(233, 8) = baseconv(233 // 8, 8) + '1'
                     = baseconv(29, 8) + '1'
                     = baseconv(29 // 8, 8) + '5' + '1'
                     = baseconv(3, 8) + '5' + '1'
                     = '3' + '5' + '1'
                     = '351'
    """
    # Pre:
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    assert x >= 0 and base > 1 and base < len(digits)
    result:str = digits[x % base] # Already handles base case
    if x >= base:
        result = baseconv(x // base, base) + result
    return result

def slowfib(n:int) -> int:
    """Calculate and return the n'th Fibonacci number, recursively.

    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n > 1

    n:      0 1 2 3 4  5  6  7  8   9 ...
    fib(n): 0 1 1 2 3  5  8 13 21  34 ...
    calls:  1 1 3 5 9 15 25 41 67 109  O(2**n)

    This is unusably slow for large n.
    """
    # Pre:
    assert n >= 0
    result:int = n # Base cases: n==0, n==1
    if n > 1: # Recursive case
        result = slowfib(n-1) + slowfib(n-2)
    return result

def fibonacci(n:int) -> int:
    """Calculate and return the n'th Fibonacci number, recursively.

    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n > 1

    n:      0 1 2 3 4  5  6  7  8  9 ...
    fib(n): 0 1 1 2 3  5  8 13 21 34 ...
    calls:  1 1 3 4 5  6  7  8  9 10 ... O(n) 
    """
    # Pre:
    assert n >= 0
    result:int = n # Base cases: n==0, n==1
    if n > 1: # Recursive case
        result = fastfib(n)[1]
    return result

def fastfib(n:int) -> Tuple[int, int]:
    """Calculate and return the n'th and (n-1)'st Fibonacci numbers, recursively.

    fastfib(1) = (0, 1)
    fastfib(n) = (fastfib(n-1)[1], fastfib(n-1)[0] + fastfib(n-1)[1]) for n > 1

    n:      1 2 3 4 5 6  7  8  9 ...
    fib(n): 1 1 2 3 5 8 13 21 34 ...
    calls:  1 2 3 4 5 6  7  8  9 ... O(n)  
    """
    # Pre:
    assert n >= 1
    # Base case:
    result:Tuple[int, int] = (0, 1)
    if n > 1:
        prev:Tuple[int, int] = fastfib(n-1)
        result = (prev[1], prev[0] + prev[1])
    return result
