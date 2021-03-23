from typing import Generic, List, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Simple list-based queue.  The end of the list is the tail of the queue."""

    def __init__(self) -> None:
        """Make an empty queue."""
        self._items:List[T] = []

        # QUERY METHODS
    def isEmpty(self) -> bool:
        """Returns True iff the queue is empty."""
        return len(self._items) == 0

    # MUTATOR METHODS
    def enqueue(self, newItem:T) -> None:
        """Add item NEWITEM to the tail of the queue."""
        # Pre: none
        self._items.append(newItem)
        # Post:
        assert not self.isEmpty()

    def dequeue(self) -> T:
        """Remove the item at the head of the queue, returning the popped item."""
        # Pre:
        assert not self.isEmpty()
        return self._items.pop(0)

