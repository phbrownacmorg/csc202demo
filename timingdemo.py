# Code to time the exeuction of other code
# Peter Brown <peter.brown@converse.edu>, 3/4/2021

from typing import List
from stats import stdDev
from timeit import timeit
from random import random

def makeNumList(size:int) -> List[float]:
    result:List[float] = []
    for i in range(size):
        result.append(random())
    return result

def stdDev2(numlist:List[float]) -> float:
    xbar = sum(numlist) / len(numlist)
    return stdDev(numlist, xbar)

def main(args:List[str]) -> int:
    timeit(stmt='stdDev2(numlist)', setup="numlist = makeNumList(1000000)")
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)