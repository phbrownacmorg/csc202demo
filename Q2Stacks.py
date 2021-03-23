from typing import Generic, List, TypeVar
from Stack import Stack


T = TypeVar('T')

class Queue(Generic[T]):
    """Queue based on two Stacks."""

    def __init__(self) -> None:
        """Make an empty queue."""
        self._inbox:Stack[T] = Stack[T]()
        self._outbox:Stack[T] = Stack[T]()

    # QUERY METHODS
    def isEmpty(self) -> bool:
        """Returns True iff the queue is empty."""
        return self._outbox.isEmpty() and self._inbox.isEmpty()

    # MUTATOR METHODS
    def enqueue(self, newItem:T) -> None:
        """Add item NEWITEM to the tail of the queue."""
        # Pre: none
        self._inbox.push(newItem)
        # Post:
        assert not self.isEmpty()

    def dequeue(self) -> T:
        """Remove the item at the head of the queue, returning the popped item."""
        # Pre:
        assert not self.isEmpty()

        if self._outbox.isEmpty():
            while not self._inbox.isEmpty():
                self._outbox.push(self._inbox.pop())
        return self._outbox.pop()
