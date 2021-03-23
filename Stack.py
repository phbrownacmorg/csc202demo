
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

