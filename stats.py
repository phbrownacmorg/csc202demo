from math import sqrt
from typing import List

def getNumbers() -> List[float]:
    """Reads a list of numbers from the keyboard, and returns it."""
    # Pre: none
    numList:List[float] = []

    while True:
        inStr:str = input('Please enter a number, or enter something else to stop: ')
        try:
            numList.append(float(inStr))
        except ValueError: # Non-number entered
            break
        # Loop invariant
        assert len(numList) > 0 and numList[-1] == float(inStr)

    # Post: return value contains a list of numbers entered at the keyboard
    return numList

def mean(nums:List[float]) -> float:
    """Finds the mean of a list of numbers."""
    # pre: nums is a list of numbers, and
    assert(len(nums) > 0)
    # Post: return value is the mean of the list nums
    return sum(nums) / len(nums)

def stdDev(nums:List[float], xbar:float) -> float:
    """Finds the standard deviation of the given list of numbers."""
    # Pre: nums is a list of numbers, and
    assert len(nums) > 0 and xbar == mean(nums)

    sumSq:float = 0
    for num in nums:
        dev:float = num - xbar
        sumSq += dev**2
        # Loop invariant
        assert sumSq >= 0

    # Post: return value is the standard deviation of nums
    return sqrt(sumSq / (len(nums) - 1))

def median(nums:List[float]) -> float:
    """Finds the median of a given list of numbers."""
    # Pre: nums is a list of numbers, and
    assert len(nums) > 0

    # Make a shallow copy to avoid a side effect
    sorted:List[float] = nums[:]
    sorted.sort()

    # Initially, just assume nums has an odd length
    midpt:int = len(sorted) // 2
    result:float = sorted[midpt]
    if len(sorted) % 2 == 0: # Even length; no middle element
        result = (sorted[midpt] + sorted[midpt - 1]) / 2

    # Post: return value is the median of nums
    return result

def main(args:List[str]) -> int:
    print('This program computes mean, median, and standard deviation of a list of numbers.')
    data:List[float] = getNumbers()
    print('numbers: ', data)
    
    xbar:float = mean(data)
    std:float = stdDev(data, xbar)
    med:float = median(data)
    print('Mean:', xbar, 'Median:', med, 'standard deviation:', std)

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)