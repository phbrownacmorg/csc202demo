# Code to time the exeuction of other code
# Peter Brown <peter.brown@converse.edu>, 3/4/2021

from typing import List
from stats import stdDev
from timeit import timeit
from random import random
from math import factorial

def makeNumList(size:int) -> List[float]:
    result:List[float] = []
    for i in range(size):
        result.append(random())
    return result

def stdDev2(numlist:List[float]) -> float:
    xbar = sum(numlist) / len(numlist)
    return stdDev(numlist, xbar)

def fact(n:int) -> int:
    """Find the factorial of the given positive integer N.  Complexity should be O(n), analytically.
    Results: t(1) ~= 0.0046
             t(10) ~= 0.008
             t(100) ~= 0.08
             t(1000) ~= 3.06
    That suggests that the complexity in practice may be less than linear.  
    (Going from n=10 to n=100, however, *is* linear.)
    """
    # Pre:
    assert n > 0
    result:int = 1
    for i in range(1,n+1):   # O(n)
        result = result * i  # O(1) (for result small enough to fit in an int, which is the usual case)
    return result

n = 1
def main(args:List[str]) -> int:
    print(timeit(stmt='factorial(n)', setup='', number=10000, globals=globals())) # type: ignore
    print(n, factorial(n))
    return 0

# math.factorial()
# t(1000) ~= 0.55
# t(100) ~= 0.015   1/5 t(1000)
# t(10) ~= 0.00085  1/18 t(100)
# t(1) ~= 0.00062   3/4 t(10)

if __name__ == '__main__':
    import sys
    main(sys.argv)