# Implementation of theTowers of Hanoi

from typing import List

def moveRing(towers:List[List[int]], start:int, end:int) -> None:
    ring:int = towers[start].pop()
    towers[end].append(ring)
    print(towers)

def hanoi(towers:List[List[int]], numrings:int, start:int, end:int, middle:int) -> None:
    # Pre:
    assert len(towers) == 3 and numrings > 0 \
        and 0 <= start <= 2 and 0 <= end <= 2 and 0 <= middle <= 2 \
        and start != middle and start != end and middle != end
    # Base case
    if numrings == 1:
        moveRing(towers, start, end)
    else: # Recursive case
        hanoi(towers, numrings - 1, start, middle, end)
        moveRing(towers, start, end)
        hanoi(towers, numrings - 1, middle, end, start)

def main(args:List[str]) -> int:
    numrings:int = 3
    towers:List[List[int]] = [list(range(1, numrings+1)), [], []]
    # Put the rings on tower 0 into the correct order
    towers[0].reverse()

    print(towers)
    hanoi(towers, numrings, 0, 2, 1)

    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)