# Demonstrate applications of a stack
# Peter Brown <peter.brown@converse.edu>, 2021-03-18

from typing import List
from Stack import Stack

# ---------------------- BALANCED DELIMITERS --------------------------

def balancedDelims(inputStr:str) -> bool:
    balanced:bool = True
    leftDelims:str = '({[<'
    rightDelims:str = ')}]>'
    stack = Stack[str]()
    for c in inputStr:
        if c in leftDelims:
            idx:int = leftDelims.find(c)
            stack.push(rightDelims[idx])
        elif c in rightDelims:
            balanced = not stack.isEmpty() and (c == stack.pop())
        if not balanced:
            break
    return balanced and stack.isEmpty()

def checkForBalanced() -> None:
    """Read a string and decide whether it contains balanced delimiters."""
    print('Single-character delimiters are these: (){}[]<>')
    inputStr:str = input('Please enter a string containing single-character delimiters:')
    print('The string \"' + inputStr + '\" is', end='')
    if not balancedDelims(inputStr):
        print(' NOT', end='')
    print(' balanced.')

# --------------------- CONVERTING A NUMBER TO ANOTHER BASE -----------------------------

digits:str='0123456789abcdefghijklmnopqrstuvwxyz'

def baseConvert(number:int, base:int) -> str:
    """Return a string equal to NUMBER expressed in base BASE."""
    # Pre:
    assert number >= 0 and 2 <= base <= len(digits)
    result:str = ''
    s:Stack[str] = Stack[str]()

    n:int = number
    while n != 0:
        s.push(digits[n % base]) # Push the digit
        n = n // base

    while not s.isEmpty():
        result = result + s.pop()
    
    if result == '':
        result = '0'

    return result

def changeBases() -> None:
    """Read an integer in base 10, and convert it to another base."""
    number:int = int(input('Please enter a non-negative integer (assuming base 10): '))
    base:int = int(input('What base (from 2 to ' + str(len(digits)) + ') should the number be converted to? '))
    print(number, 'in base 10 =', baseConvert(number, base), 'in base', base)

# ---------------------------------- MAIN ---------------------------------------------

def main(args:List[str]) -> int:
    checkForBalanced()
    changeBases()
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
