from typing import Generic, List, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Circular queue on top of a Python list.  The initial capacity of the queue can be adjusted.  Entries with a value of None
    are interpreted as being empty; thus, this queue can't store an actual None."""
    
    def _invariant(self) -> bool:
        valid:bool = self._capy == len(self._items)
        valid = valid and 0 <= self._head < self._capy
        valid = valid and 0 <= self._tail < self._capy
        valid = valid and self._items[self._head] is not None or (self._items[self._head] is None and self._tail == self._head)
        valid = valid and self._items[self._tail] is None or (self._items[self._tail] is not None and self._head == self._tail)
        return valid

    def __init__(self, capy:int = 4) -> None:
        """Make an empty queue with capacity CAPY.  The default for CAPY is intentionally set low."""
        # Pre:
        assert capy > 0
        self._items:List[T] = [None] * capy
        self._head:int = 0
        self._tail:int = 0
        self._capy = capy
        # Post:
        assert self._invariant()

    def isEmpty(self) -> bool:
        return self._items[self._head] == None

    def enqueue(self, newItem:T) -> None:
        """Add item NEWITEM to the tail of the queue."""
        # Pre:
        assert self._invariant()
        if self._items[self._tail] is None: # If room
            self._items[self._tail] = newItem
            self._tail = self._tail + 1
            if self._tail == self._capy:
                self._tail == 0
        else: # Need to grow the capacity
            raise NotImplementedError
        # Post:
        assert self._invariant()
    
    def dequeue(self) -> T:
        """Remove the item at the head of the queue, returning the popped item."""
        # Pre:
        assert self._invariant() and not self.isEmpty()
        returnValue:T = self._items[self._head]
        self._head = self._head + 1
        if self._head == self._capy:
            self._head = 0
        # Post:
        assert self._invariant()
        return returnValue


