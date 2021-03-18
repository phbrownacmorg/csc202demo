
from typing import Generic, List, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    """Class to represent a stack.  The stack is implemented as a list.  The back end
    of the list is the top of the stack."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._items:List[T] = []

    # QUERY METHODS
    def isEmpty(self) -> bool:
        """Returns True iff the stack is empty."""
        return len(self._items) == 0

    # MUTATOR METHODS
    def push(self, newItem:T) -> None:
        """Push item NEWITEM onto the stack."""
        # Pre: none
        self._items.append(newItem)
        # Post:
        assert not self.isEmpty()

    def pop(self) -> T:
        """Pop the stack, returning the popped item."""
        # Pre:
        assert not self.isEmpty()
        return self._items.pop()


def balancedDelims(inputStr:str) -> bool:
    balanced:bool = True
    leftDelims:str = """({[<"'"""
    rightDelims:str = """)}]>"'"""
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
    """Demonstrate applications of the Stack."""
    print('Single-character delimiters are these: (){}[]<>\'\'\"\"')
    inputStr:str = input('Please enter a string containing single-character delimiters:')
    print('The string \"' + inputStr + '\" is', end='')
    if not balancedDelims(inputStr):
        print(' NOT', end='')
    print(' balanced.')

def main(args:List[str]) -> int:
    checkForBalanced()
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)